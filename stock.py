import csv
import re

# Words that carry no information about WHICH item the customer means.
IGNORE_WORDS = {
    "do", "you", "have", "how", "much", "is", "it", "the", "a", "an", "and",
    "of", "for", "what", "does", "cost", "are", "there", "any", "in", "stock",
    "sell", "i", "need", "want", "can", "get", "your", "price", "many",
    "available", "please", "me", "my", "to", "on", "with",
    "tablet", "tablets", "capsule", "capsules",
}


def load_stock(path="stock.csv"):
    """Read the stock CSV file, skip bad rows with a warning, return the good rows."""
    try:
        with open(path, newline="", encoding="utf-8-sig") as file:
            rows = list(csv.DictReader(file))
    except FileNotFoundError:
        raise SystemExit(f"Cannot find {path}. Put it in the same folder as chat.py.")

    needed = {"item", "price_ugx", "in_stock", "last_updated"}
    if not rows or not needed.issubset(rows[0].keys()):
        raise SystemExit(
            f"{path} must have the header line: item,price_ugx,in_stock,last_updated "
            "and at least one item."
        )

    good_rows = []
    for line_number, row in enumerate(rows, start=2):  # line 1 is the header
        problem = None
        if not (row["item"] or "").strip():
            problem = "the item name is empty"
        elif not (row["price_ugx"] or "").strip().isdigit():
            problem = f"price '{row['price_ugx']}' is not a plain number"
        elif (row["in_stock"] or "").strip().lower() not in ("yes", "no"):
            problem = f"in_stock '{row['in_stock']}' must be yes or no"
        elif not (row["last_updated"] or "").strip():
            problem = "last_updated is empty"

        if problem:
            print(f"Warning: skipping line {line_number} of {path}: {problem}.")
        else:
            good_rows.append(row)

    if not good_rows:
        raise SystemExit(f"No usable items found in {path}.")
    return good_rows

def split_words(text):
    """Turn text into a list of lowercase words, with punctuation removed."""
    return re.findall(r"[a-z0-9]+", text.lower())


def find_items(question, stock):
    """Return the stock rows whose item name shares a word with the question."""
    question_words = {w for w in split_words(question) if w not in IGNORE_WORDS}
    matches = []
    for row in stock:
        item_words = set(split_words(row["item"]))
        if question_words & item_words:
            matches.append(row)
    return matches


def describe(row):
    """Turn one stock row into a short sentence the assistant can use."""
    status = "in stock" if row["in_stock"].strip().lower() == "yes" else "out of stock"
    price = int(row["price_ugx"])
    return f'{row["item"]}: UGX {price:,}, {status} (last checked {row["last_updated"]})'


def build_stock_note(question, stock):
    """Create the extra instructions the assistant receives for this one question."""
    matches = find_items(question, stock)
    if not matches:
        return (
            "STOCK CHECK: No entry in the pharmacy's stock list matched this question. "
            "Do not state a price or availability for any medicine unless it already "
            "appears earlier in this conversation. If the customer is asking whether "
            "we have a medicine or what it costs, say you cannot confirm and ask them "
            "to please confirm with our staff."
        )
    lines = "\n".join("- " + describe(row) for row in matches)
    return (
        "STOCK CHECK: These entries from the pharmacy's own stock list match the "
        "customer's question:\n" + lines + "\n"
        "State price and availability ONLY from these entries, and always mention the "
        "'last checked' date. Do not suggest alternative medicines or give medical advice."
    )