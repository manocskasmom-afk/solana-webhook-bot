from flask import Flask, request
import traceback

app = Flask(__name__)


@app.route("/")
def home():
    return "Webhook is running!", 200


@app.route("/webhook", methods=["POST"])
def webhook():

    try:
        # Get JSON sent by Helius
        data = request.get_json(force=True)

        # Helius sends a list of transactions
        if not isinstance(data, list):
            data = [data]

        print("\n====================================================")
        print(f"📡 Received {len(data)} transaction(s)")
        print("====================================================")

        for tx in data:

            tx_type = tx.get("type", "UNKNOWN")
            source = tx.get("source", "UNKNOWN")
            signature = tx.get("signature", "")

            print("\n----------------------------------------------------")
            print("Transaction Type :", tx_type)
            print("Source           :", source)
            print("Signature        :", signature)

            if tx_type != "SWAP":
                print("⏩ Not a swap. Ignoring.")
                continue

            print("✅ SWAP DETECTED")

            token_transfers = tx.get("tokenTransfers", [])

            if len(token_transfers) == 0:
                print("No token transfers found.")
                continue

            print(f"\nFound {len(token_transfers)} token transfers:\n")

            for transfer in token_transfers:

                mint = transfer.get("mint", "")
                amount = transfer.get("tokenAmount", 0)
                sender = transfer.get("fromUserAccount", "")
                receiver = transfer.get("toUserAccount", "")

                print("----------------------------------------")
                print("Mint   :", mint)
                print("Amount :", amount)
                print("From   :", sender)
                print("To     :", receiver)

                # Ignore wrapped SOL
                if mint == "So11111111111111111111111111111111111111112":
                    print("Type   : Wrapped SOL")
                else:
                    print("Type   : TOKEN")
                    print("🎯 POSSIBLE TOKEN FOR COPY TRADING")

        print("\n✅ Webhook processed successfully.\n")

        return "OK", 200

    except Exception:

        print("\n❌ ERROR INSIDE WEBHOOK")
        traceback.print_exc()

        return "ERROR", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    