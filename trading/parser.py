SOL_MINT = "So11111111111111111111111111111111111111112"


def parse_swap(tx):
    """
    Extract useful information from a Helius SWAP transaction.
    """

    result = {
        "action": "UNKNOWN",
        "token": None,
        "token_amount": 0,
        "sol_amount": 0,
        "source": tx.get("source", "UNKNOWN")
    }

    transfers = tx.get("tokenTransfers", [])

    for transfer in transfers:

        mint = transfer.get("mint")
        amount = transfer.get("tokenAmount", 0)

        if mint == SOL_MINT:
            result["sol_amount"] = amount

        else:
            result["token"] = mint
            result["token_amount"] = amount
            result["action"] = "BUY"

    return result
