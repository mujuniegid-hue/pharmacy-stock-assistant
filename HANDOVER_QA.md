# Handover: Five Questions and Answers

## 1. What if the assistant gives a customer the wrong price?

It only quotes prices from your `stock.csv` file and always says the "last checked" date. So the price it gives can only be as correct as that file. If an item is not on the list, it is built to say "please ask our staff" and not to guess. I tested this with unknown items, misspellings and attempts to trick it into a different price, and it never gave a wrong price in those tests. But it is an AI, and no AI can be promised to be right every time. Please keep the file up to date, and treat the assistant as a helper for staff, not a replacement for checking the shelf.

## 2. Does it give medical advice? Who is responsible?

No. It is told not to give medical advice or dosage and to send those questions to your pharmacist. I tested one dosage question and (fill in the result after retesting). It is not a medical device and does not replace a pharmacist. Responsibility for what customers are told stays with the pharmacy, so a staff member should be available to check and correct it.

## 3. What does it cost to run, and whose account is it on?

The assistant uses Google's Gemini service. Google charges by usage, and its prices and free limits change, so I will not quote a figure here. Please check Google's current pricing page. The service needs an API key, which is like a password for that account. Ideally the pharmacy creates its own account so that the pharmacy controls the key and the bill. The key is kept in a private `.env` file and must never be shared. Google's service is sometimes busy, and when that happens the assistant shows a "please try again" message.

## 4. What happens to what customers type? Is it private?

Each question is sent to Google's service to be answered, together with your stock entry for that question. The assistant itself does not save conversations to a file: the chat is held in the computer's memory and disappears when the window closes. But because the text goes to Google, customers and staff should not type personal details or private health information. Please check what data-protection rules apply to your pharmacy, and Google's terms for the plan you use.

## 5. What if something breaks, and what can be added later?

The README has a table for the common problems. For anything else, contact (your name and number). Support terms are: (write only what you can really offer, for example "questions answered by message within X working days for Y weeks after delivery"; anything beyond that is quoted separately). Changes you can make yourself: prices and stock (Part 3 of the README), and opening hours and services (Part 4). Things that need a developer: a version customers can use directly (a website or WhatsApp), live stock from a Google Sheet, and the other ideas in `BACKLOG.md`. Each of those is a separate piece of work with its own quote.