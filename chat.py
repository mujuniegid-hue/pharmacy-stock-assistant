import json

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

BUSINESS_NAME = config["business_name"]
MODEL = config["model"]
EXIT_WORD = config["exit_word"]
GOODBYE_MESSAGE = config["goodbye_message"]
ERROR_MESSAGE = config["error_message"]
SHOW_DEBUG = config["show_debug"]
with open("system_prompt.txt", "r", encoding="utf-8") as file:
 SYSTEM_PROMPT = file.read().replace("{business_name}", BUSINESS_NAME)

client = genai.Client()
history = []

print(f"{BUSINESS_NAME} Assistant (type '{EXIT_WORD}' to exit)")

while True:
    user_input = input("\nYou: ")

    if user_input.strip().lower() == EXIT_WORD.lower():
        print(GOODBYE_MESSAGE)
        break

    if not user_input.strip():
        continue

    history.append(
        types.Content(role="user", parts=[types.Part(text=user_input)])
    )

    reply = ""

    try:
        stream = client.models.generate_content_stream(
            model=MODEL,
            contents=history,
            config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
        )

        print("Bot: ", end="", flush=True)

        for chunk in stream:
            if chunk.text:
                print(chunk.text, end="", flush=True)
                reply += chunk.text

        print()

    except Exception as error:
        history.pop()
        print("/n" + ERROR_MESSAGE)
        if SHOW_DEBUG:
          print("(Details:", error, ")")
        continue

    if not reply:
        history.pop()
        print("Sorry, I could not produce an answer. Please try again.")
        continue

    history.append(
        types.Content(role="model", parts=[types.Part(text=reply)])
    )
if SHOW_DEBUG:
    print(f"[debug: {len(history)} messages stored]")