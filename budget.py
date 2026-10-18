transaction = {
    "date": "2026-09-03",
    "description": "BP",
    "amount": -241.32
}

single_trancation = (f"Data: {transaction.get('date')}\n"
                     f"Opis: {transaction.get('description')}\n"
                     f"Kwota: {transaction.get('amount')}")

print(single_trancation)

categories = {
    "Fuel": ["ORLEN", "SHELL", "BP"],
    "Groceries": ["BIEDRONKA", "LIDL", "KAUFLAND"],
    "Subscriptions": ["NETFLIX", "SPOTIFY"]
}

def categorize_transaction(transaction, categories):
    description = transaction.get('description').upper()
    for key, value in categories.items():
        for keyword in value:
            if keyword in description:
                return key
    return "Uncategorized"


result = categorize_transaction(transaction, categories)
print(result)
