# Setup Guide: Kampala Pharmacy Assistant

This guide takes you from nothing to a working assistant. It should take about 15 minutes.

## What you need
- A Windows computer with internet
- Python 3.10 or newer (download from https://www.python.org/downloads/ and tick "Add Python to PATH" during install)
- A free Gemini API key (from https://aistudio.google.com/apikey)

## Step 1: Open the project folder
Open PowerShell and go to the project folder:

```
cd "C:\path\to\kampala-pharmacy-bot"
```

## Step 2: Create and activate a virtual environment
A virtual environment keeps this tool's libraries separate from the rest of your computer.

```
python -m venv venv
venv\Scripts\Activate.ps1
```

You should see `(venv)` at the start of the line.
If Windows blocks the script, run this first, then try again:
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`

## Step 3: Install the libraries
```
pip install -r requirements.txt
```

## Step 4: Add your API key
1. Copy the file `.env.example` and rename the copy to `.env`
2. Open `.env` and replace `YOUR_KEY_HERE` with your real key
3. Save. Never share this file.

## Step 5: Edit your settings
Open `config.json` and change:
- `business_name`: your pharmacy's name
- `model`: leave as is unless told otherwise
- `show_debug`: keep `false`

## Step 6: Edit your pharmacy information
Open `system_prompt.txt` in Notepad. Update the opening hours, services and prescription rules so they are **100% correct**. The assistant only knows what is written here.

## Step 7: Run the assistant
```
python chat.py
```
You should see the heading and a `You:` prompt. Type a question. Type `quit` to exit.

## Before you go live checklist
- [ ] Opening hours checked by the owner
- [ ] Services list checked by the owner
- [ ] Prescription rules and processing time checked
- [ ] Tested with 3 questions: hours, an unlisted service, and a dosage question

## Troubleshooting
| Problem | What it means | What to do |
|---|---|---|
| `FileNotFoundError` | You are in the wrong folder | Use `cd` to enter the project folder |
| `JSONDecodeError` | Typo in `config.json` | Check commas and double quotes |
| Bot is silent or very slow | The AI model is busy | Change `model` in `config.json` to `gemini-3.5-flash-lite`, save, and run again |
| `503 UNAVAILABLE` | Model too busy | Wait a minute, or change the model as above |
| `404 NOT_FOUND` | Model name retired | Ask the developer for a current model name |
| `API key not valid` | Wrong key in `.env` | Re-copy the key, with no spaces |