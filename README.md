# Pharmacy Stock Assistant

A helper that answers customers' routine questions: opening hours, services, prescriptions, and **prices and stock for items on your own stock list**. If an item is not on your list, it does not guess. It asks the customer to check with your staff.

It does **not** give medical advice or dosage instructions. It sends those questions to the pharmacist.

**IMPORTANT:** The prices, stock, opening hours and services in this package are made-up examples. Before real use, the pharmacy owner must replace them with real, checked information (see Part 3 and Part 4).

---

## What is in this folder

| File | What it is for |
|------|----------------|
| `start.bat` | Double-click this to start the assistant |
| `stock.csv` | Your list of items, prices and whether they are in stock |
| `system_prompt.txt` | Your opening hours, services and prescription rules |
| `config.json` | Your pharmacy name and a few messages |
| `.env` | A private key that lets the assistant work. Never share it |
| Other files | Used by the program. You do not need to open them |

---

## Part 1: First-time setup (done once, by the person installing it)

1. Install Python (version 3.10 or newer) from python.org. During installation, tick the box "Add Python to PATH".
2. Open the project folder. Click the folder's address bar, type `powershell`, and press Enter. A blue window opens.
3. Type each line below, one at a time, pressing Enter after each. Wait for each to finish.

   ```
   python -m venv venv
   venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

4. In the folder, make a copy of the file `.env.example` and name the copy `.env`.
5. Open `.env` in Notepad. After `GEMINI_API_KEY=`, paste your key. Save and close the file. Do not share this file or upload it anywhere.
6. Open `config.json` in Notepad. Change `business_name` to your pharmacy's name. Save and close.
7. Double-click `start.bat`. If you see a welcome line with your pharmacy's name, setup worked. Type `quit` to close it.

If step 7 shows an error mentioning "model not found", the model name in `config.json` is out of date. Ask your developer to update it.

---

## Part 2: Using the assistant every day

1. Double-click `start.bat`. A black window opens.
2. Wait for the welcome line.
3. Type your question after `You:` and press Enter. Example: `how much is paracetamol?`
4. Read the answer after `Bot:`.
5. To finish, type `quit` and press Enter.

You can ask a follow-up straight after, such as "is it in stock?" or "how much is it?". The assistant remembers the last item you asked about. If the last question was about an item that is not on your list, it will not guess a price.

---

## Part 3: Updating prices and stock

Do this whenever a price or stock level changes. You do not need to restart the assistant. The next question picks up your changes.

1. Open `stock.csv` in Excel or Google Sheets.
2. Change what you need. Each row is one item. The columns are:
   - `item`: the name customers use, for example `Paracetamol 500mg (10 tablets)`
   - `price_ugx`: the price as a plain number, for example `1500`. Do not write `1,500` or `1500 UGX`
   - `in_stock`: write exactly `yes` or `no`
   - `last_updated`: the date you checked, for example `2026-11-26`
3. Do not change or delete the first row (`item,price_ugx,in_stock,last_updated`).
4. Save the file as **CSV (Comma delimited)**, with the same name `stock.csv`, in the same folder. If Excel asks "Keep using this format?", choose **Yes**.

Tips:
- The assistant tells customers the "last checked" date. Keep it honest and up to date.
- If you add a new item, give it a clear name. The assistant finds items by the words in the name.
- If a row has a mistake, the assistant skips that row and shows a warning when it starts. Look at the black window and fix the row.

---

## Part 4: Changing opening hours, services or the pharmacy name

1. Close the assistant if it is open (type `quit`).
2. To change hours, services or prescription rules: open `system_prompt.txt` in Notepad, edit the text, and save.
3. To change the pharmacy name: open `config.json` in Notepad, change `business_name`, and save.
4. Double-click `start.bat` again. Changes here only take effect after a restart.

Only change the words. Do not delete the line that contains `{business_name}`.

---

## Part 5: If something goes wrong

| What you see | What to do |
|--------------|------------|
| `Cannot find stock.csv` | The stock list is missing or renamed. Put a file called `stock.csv` back in the same folder as `start.bat` |
| `Stock file problem: ...` | The first row of `stock.csv` was changed. Put it back to `item,price_ugx,in_stock,last_updated` and save. The assistant keeps using the last good list until then |
| `Warning: skipping line ...` | One row has a mistake (such as a price with a comma). Fix that row and save |
| `Sorry, something went wrong. Please try again.` | The assistant could not reach the internet or the service was busy. Wait a minute and ask again |
| The assistant says "I cannot confirm that, so please ask our staff" | This is normal. The item is not on your list, or the assistant is not sure. A member of staff should check |
| The window closes immediately | Open `start.bat` again. If it keeps happening, contact the person who set it up |

---

## What the assistant cannot do

- It only knows what is in your `stock.csv` and `system_prompt.txt`. It cannot see your shelves.
- It needs an internet connection to answer.
- If a customer misspells a medicine name, or uses a brand name that is not on your list, it will usually say it cannot confirm. This is on purpose: no answer is safer than a wrong one.
- If a customer asks for a type or size that is not on your list (for example "hand cream" when you only list hand sanitizer), it may mention the item it found. Staff should confirm.
- It does not give medical advice. Please keep a member of staff available for customers who need the pharmacist.
- Prices and stock are only as correct as your `stock.csv`.

---

## Getting help

Set up and supported by: **Egidio K Ham**
Phone / WhatsApp: **0785376493**
Email: **mujunieggid@gmail.com**