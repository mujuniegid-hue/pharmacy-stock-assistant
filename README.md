# Kampala Pharmacy Assistant

A chat assistant that answers routine pharmacy questions (opening hours, services, prescription requirements) using only information the pharmacy provides. It does not give medical advice or guess.

Built with Python and the Google Gemini API as a client-ready deliverable. The business name, AI model and messages are set in a config file, and the pharmacy's information lives in a plain text file, so no code changes are needed for a new client.

## What is included
- `chat.py`: the assistant (runs in the terminal)
- `config.json`: settings (business name, model, messages)
- `system_prompt.txt`: the pharmacy's hours, services and rules
- `.env.example`: template for the API key
- `SETUP_GUIDE.md`: full setup and troubleshooting steps
- `SERVICE_DESCRIPTION.md`: client-facing description and pricing

## How to run
1. Install Python 3.10 or newer.
2. Create and activate a virtual environment, then install the libraries:
   ```
   python -m venv venv
   venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and paste your Gemini API key after `GEMINI_API_KEY=`.
4. Edit `config.json` and `system_prompt.txt` for your pharmacy.
5. Start the assistant:
   ```
   python chat.py
   ```
   Type your question, or `quit` to exit.

See `SETUP_GUIDE.md` for detailed steps and troubleshooting.

## Important
The hours, services and prescription details in `system_prompt.txt` are **placeholders** for demonstration. A pharmacy owner must verify every fact before real use.