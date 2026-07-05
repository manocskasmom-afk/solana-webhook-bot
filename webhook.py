from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/")
def home():
    return "Webhook is running", 200


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    print("\n==============================")
    print("📡 RAW HELIUS EVENT")
    print("==============================")

    print(json.dumps(data, indent=2))

    # -----------------------------
    # STEP 1: SAFE EXTRACTION
    # -----------------------------
    event_type = data.get("type", "UNKNOWN")

    print("\n🔍 EVENT TYPE:", event_type)

    # -----------------------------
    # STEP 2: DETECT SWAP
    # -----------------------------
    swap_event = None

    if "events" in data and data["events"]:
        swap_event = data["events"].get("swap")

    if swap_event:
        print("\n🔁 SWAP DETECTED!")

        # Try extracting key info safely
        token_in = swap_event.get("tokenInputs", [{}])[0].get("mint", "UNKNOWN")
        token_out = swap_event.get("tokenOutputs", [{}])[0].get("mint", "UNKNOWN")

        print("🟢 TOKEN IN:", token_in)
        print("🔴 TOKEN OUT:", token_out)

        print("\n🚨 SIGNAL: TRADE DETECTED (POTENTIAL BUY/SELL)")
    else:
        print("\n⚪ No swap detected → ignoring")

    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)