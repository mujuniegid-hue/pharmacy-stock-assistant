import os
import tempfile

from stock import load_stock


def write_temp(text):
    handle, path = tempfile.mkstemp(suffix=".csv")
    with os.fdopen(handle, "w", encoding="utf-8") as file:
        file.write(text)
    return path


results = []


def check(name, condition):
    print("PASS" if condition else "FAIL", "-", name)
    results.append(condition)


HEADER = "item,price_ugx,in_stock,last_updated\n"

# 1. A bad price row is skipped, good rows are kept
path = write_temp(HEADER + "Good item,1000,yes,2026-11-25\nBad price,1,500 UGX,yes,2026-11-25\nOther,2000,no,2026-11-25\n")
rows = load_stock(path)
check("bad rows skipped, good rows kept", [r["item"] for r in rows] == ["Good item", "Other"])

# 2. Blank in_stock and short rows do not crash
path = write_temp(HEADER + "Short row,1000\nWeird stock,500,maybe,2026-11-25\nFine,700,yes,2026-11-25\n")
check("short and odd rows skipped", [r["item"] for r in load_stock(path)] == ["Fine"])

# 3. Missing file gives a clear message
try:
    load_stock("does_not_exist.csv")
    check("missing file stops with message", False)
except SystemExit as error:
    check("missing file stops with message", "Cannot find" in str(error))

# 4. Wrong header gives a clear message
try:
    load_stock(write_temp("name,cost\nParacetamol,1500\n"))
    check("wrong header stops with message", False)
except SystemExit as error:
    check("wrong header stops with message", "header line" in str(error))

print()
print("ALL PASSED" if all(results) else "SOME FAILED")