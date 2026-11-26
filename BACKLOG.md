# Backlog: what I would improve with more time

Ordered by importance. Effort figures are rough guesses, not measured.

## High priority

| # | Improvement | Why it matters | Rough effort |
|---|-------------|----------------|--------------|
| 1 | Detect words in a question that match nothing on the stock list | Today one shared word can match the wrong product (for example "hand cream" can match "hand sanitizer"). The assistant is told to double-check, but code should catch it | 1 day |
| 2 | Retry automatically when Google's service is busy | During testing the service returned "high demand" once. Staff must retype the question | 2 hours |
| 3 | Handle Ctrl+C and closing the window cleanly | (Fill in after the E11 and E12 results) | 1 hour |
| 4 | (Add any high or medium problem from the watched user test) | | |

## Medium priority

| # | Improvement | Why it matters | Rough effort |
|---|-------------|----------------|--------------|
| 5 | Alternative names for items (an "aliases" column) | Customers say "amoxil" or "sanitiser", the list says "Amoxicillin" or "sanitizer" | 3 hours |
| 6 | "Did you mean ...?" for misspellings | Today a misspelled name gets "please ask staff". A suggestion would be friendlier, but must never state a price for a guessed item | 1 day |
| 7 | Warn when a stock entry is old | A price last checked months ago should not be quoted without a caution | 3 hours |
| 8 | Low-stock warnings | Owner is told when an item is running out | Needs the owner's rules first |
| 9 | Save questions the assistant could not answer | Shows the owner what customers ask for that is not on the list | 3 hours |
| 10 | Check the `last_updated` date format when loading | Today any text is accepted | 1 hour |

## Low priority

| # | Improvement | Rough effort |
|---|-------------|--------------|
| 11 | Remove the "Bot:" prefix that appears before an error message | 30 minutes |
| 12 | Limit how much conversation history is sent, to save cost on long chats | 2 hours |
| 13 | One-click installer, so setup needs no typing | 1 to 2 days |

## Larger future projects (each needs its own plan and quote)

- A channel customers can use directly (a website chat or WhatsApp). Today the assistant is for staff at a computer.
- Reading stock from a live Google Sheet instead of a CSV file.
- Connecting to the pharmacy's existing stock or sales system.
- Real pharmacy data, supplied and verified by the owner. Everything now is a placeholder.
- Testing in Luganda and other local languages. One short Luganda question worked in testing, which is not enough to promise it.
- Checking local pharmacy regulations and data-protection rules before public use.