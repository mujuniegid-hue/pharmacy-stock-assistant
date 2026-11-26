import sys

from stock import (
    load_stock,
    find_items,
    has_item_words,
    build_stock_note,
    describe,
)

# A fixed test list. It does not change when the pharmacy edits stock.csv.
TEST_STOCK = [
    {"item": "Paracetamol 500mg (10 tablets)", "price_ugx": "1500",
     "in_stock": "yes", "last_updated": "2026-11-25"},
    {"item": "ORS sachet", "price_ugx": "1000",
     "in_stock": "yes", "last_updated": "2026-11-25"},
    {"item": "Amoxicillin 500mg (capsules x10)", "price_ugx": "6000",
     "in_stock": "no", "last_updated": "2026-11-25"},
    {"item": "Hand sanitizer 100ml", "price_ugx": "3500",
     "in_stock": "yes", "last_updated": "2026-11-25"},
]

results = []


def check(name, condition):
    """Print PASS or FAIL for one test and remember the result."""
    print(("PASS" if condition else "FAIL") + " - " + name)
    results.append(bool(condition))


def names(rows):
    """Return just the item names from a list of stock rows."""
    return [row["item"] for row in rows]


# --- finding items ---
check("finds paracetamol",
      names(find_items("do you have paracetamol?", TEST_STOCK))
      == ["Paracetamol 500mg (10 tablets)"])
check("finds a short name (ORS)",
      names(find_items("do you have ORS?", TEST_STOCK)) == ["ORS sachet"])
check("ignores capital letters",
      len(find_items("PARACETAMOL", TEST_STOCK)) == 1)
check("finds out-of-stock item",
      len(find_items("do you have amoxicillin?", TEST_STOCK)) == 1)
check("reports out of stock",
      "out of stock" in describe(find_items("amoxicillin", TEST_STOCK)[0]))

# --- things that must NOT match ---
check("unknown item returns nothing",
      find_items("do you have ibuprofen?", TEST_STOCK) == [])
check("misspelling returns nothing (safe)",
      find_items("paracetmol", TEST_STOCK) == [])
check("vague question returns nothing",
      find_items("how much is it?", TEST_STOCK) == [])
check("generic word alone does not match",
      find_items("do you have tablets?", TEST_STOCK) == [])
check("generic word plus real name still matches",
      len(find_items("paracetamol tablets", TEST_STOCK)) == 1)

# --- the note sent to the assistant ---
note = build_stock_note("how much is paracetamol?", TEST_STOCK)
check("note contains price", "1,500" in note)

note = build_stock_note("do you have amoxicillin?", TEST_STOCK)
check("note says out of stock", "out of stock" in note)

note = build_stock_note("do you have ibuprofen?", TEST_STOCK)
check("note refuses to guess when nothing matches",
      "No entry" in note and "UGX" not in note)
check("no-match note gives the exact sentence for staff",
      "please ask our staff to check the shelves or stock system" in note)

note = build_stock_note("do you have 500mg?", TEST_STOCK)
check("several matches: note asks for each one to be listed",
      "each one" in note)

note = build_stock_note("do you have hand cream?", TEST_STOCK)
check("note tells the assistant to check it is the same product",
      "same product" in note)

# --- best match (shared words) ---
check("specific question returns only the best match",
      names(find_items("paracetamol 500mg", TEST_STOCK))
      == ["Paracetamol 500mg (10 tablets)"])
check("ambiguous question returns all tied items",
      len(find_items("do you have 500mg?", TEST_STOCK)) == 2)

# --- follow-up memory ---
sanitizer = find_items("hand sanitizer", TEST_STOCK)

check("follow-up words are recognised as having no item",
      not has_item_words("how much is it?")
      and not has_item_words("is that one in stock?"))
check("question naming an item is recognised",
      has_item_words("do you have amoxil?"))

note = build_stock_note("how much is it?", TEST_STOCK, sanitizer)
check("follow-up uses the remembered item",
      "Hand sanitizer" in note and "3,500" in note)

note = build_stock_note("how much is it?", TEST_STOCK, [])
check("follow-up with nothing remembered refuses",
      "No entry" in note and "UGX" not in note)

note = build_stock_note("do you have amoxil?", TEST_STOCK, sanitizer)
check("unknown item never leaks the remembered item",
      "No entry" in note and "Hand sanitizer" not in note)

# --- the real stock file loads ---
check("real stock.csv loads and is not empty",
      len(load_stock("stock.csv")) > 0)

# --- final result ---
if all(results):
    print("\nALL PASSED")
else:
    print("\nSOME FAILED")
    sys.exit(1)