from stock import load_stock, find_items, describe
from stock import build_stock_note

stock = load_stock("stock.csv")
results = []


def check(name, condition):
    print("PASS" if condition else "FAIL", "-", name)
    results.append(condition)


found = find_items("Do you have paracetamol and how much is it?", stock)
check("finds paracetamol", len(found) == 1 and "Paracetamol" in found[0]["item"])

found = find_items("how much is ORS?", stock)
check("finds a short name (ORS)", len(found) == 1)

found = find_items("PARACETAMOL price", stock)
check("ignores capital letters", len(found) == 1)

found = find_items("Do you have amoxicillin?", stock)
check("finds out-of-stock item", len(found) == 1)
check("reports out of stock", "out of stock" in describe(found[0]))

check("unknown item returns nothing", find_items("Do you sell insulin?", stock) == [])
check("misspelling returns nothing (safe)", find_items("Do you have amoxicilin?", stock) == [])
check("vague question returns nothing", find_items("How much is it?", stock) == [])
note = build_stock_note("How much is paracetamol?", stock)
check("note contains price", "UGX 1,500" in note and "last checked" in note)
note = build_stock_note("Do you have amoxicillin?", stock)
check("note says out of stock", "out of stock" in note)
note = build_stock_note("Do you sell insulin?", stock)
check("note refuses to guess when nothing matches", "Do not state a price" in note)

print(describe(stock[0]))
print()
print("ALL PASSED" if all(results) else "SOME FAILED")