# Pharmacy Stock Assistant

A command-line chat assistant for a pharmacy. It answers routine questions (opening hours, services) and, new in this version, **price and stock questions answered only from the pharmacy's own stock list**. If an item is not on the list, it does not guess: it asks the customer to confirm with staff.

Built with Python and the Google Gemini API for AI Masterclass 2, Week 7: Building the Core. This is a practice client project. It is a copy of `pharmacy-assistant-client-package`, which is kept unchanged as a reference.

## What I built

The core feature is a **stock lookup**:

1. The pharmacy keeps its items in `stock.csv` (item, price in UGX, in stock yes/no, date last checked).
2. When a customer asks a question, `stock.py` finds matching items by name.
3. The matching entries are sent to the AI with that one question, with the instruction to answer only from them.
4. If nothing matches, the AI is told not to state any price or availability, and to ask the customer to confirm with staff.

The assistant still refuses to give medical advice.

## Files

- `chat.py`: the assistant (runs in the terminal)
- `stock.py`: loads and checks `stock.csv`, finds matching items
- `stock.csv`: the stock list (the pharmacy edits this in Excel or Google Sheets)
- `config.json`: business name, model name and messages
- `system_prompt.txt`: the pharmacy's hours, services and rules
- `test_stock.py`, `test_bad_data.py`: automatic tests
- `.env.example`: template for the API key

## How to run

1. Install Python 3.10 or newer.
2. Create and activate a virtual environment, then install the libraries:

   ```
   python -m venv venv
   venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and paste your Gemini API key after `GEMINI_API_KEY=`. Never share or upload this file.
4. Edit `config.json`, `system_prompt.txt` and `stock.csv` for your pharmacy.
5. Start the assistant:

   ```
   python chat.py
   ```

   Type your question, or `quit` to exit.

If you see a "model not found" error, the model name in `config.json` is out of date. Model names change over time, so check Google's current model list.

## Stock file format

The first line must be exactly:

```
item,price_ugx,in_stock,last_updated
```

- `price_ugx`: plain number only, for example `1500` (not `1,500` or `1500 UGX`)
- `in_stock`: `yes` or `no`
- `last_updated`: a date such as `2026-11-25`

Rows that break these rules are skipped with a warning when the program starts. The assistant restarts to pick up edits to the file.

## Tests

```
python test_stock.py
python test_bad_data.py
```

Both end with `ALL PASSED`. I also ran real conversations covering a price question, an out-of-stock item, an unknown item, opening hours, a medical advice question, a follow-up question and a misspelled medicine name. Every answer was safe: the assistant either answered from the stock list or asked the customer to confirm with staff.

## Known limits

- Matching is by whole words from the item name. A misspelled medicine name does not match, so the assistant asks the customer to confirm with staff. This is deliberate: no answer is safer than a wrong one.
- A follow-up like "how much is it?" has no item name to search for. In my test the assistant said it could not confirm the price and asked the customer to check with staff, even though the price had been given in the previous answer.
- A word shared by several items (for example "500mg") returns all of them.
- The stock list is read once when the program starts, so the assistant must be restarted after the file is edited.
- The assistant gives no medical advice and cannot check physical shelves.

## Important

All prices, stock levels, hours and services in this project are **made-up placeholders** for demonstration. A pharmacy owner must supply and verify the real information before real use.