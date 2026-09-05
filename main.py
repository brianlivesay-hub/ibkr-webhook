from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    try:
        data = request.json
        print("Received alert:", data)

        # Example: read the signal from TradingView
        signal = data.get("signal")
        ticker = data.get("ticker")

        # Placeholder logic (we will replace this with IBKR order code)
        if signal == "buy":
            print(f"Buying {ticker}")
        elif signal == "sell":
            print(f"Selling {ticker}")
        else:
            print("Unknown signal")

        return {"status": "ok"}, 200

    except Exception as e:
        print("Error:", e)
        return {"status": "error"}, 400

@app.route('/', methods=['GET'])
def home():
    return "Webhook is running!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
