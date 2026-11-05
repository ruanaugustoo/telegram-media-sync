# 0004. Network Resilience and Sync Atomicity

## Context
Temporary HTTP connection failures or Telegram API timeouts must not prematurely mark a file as sent or stop the script from running.

## Decision
- **Atomic history updates:** Call `db.mark_as_sent()` only after Telegram explicitly confirms success (`HTTP 200 OK` and `ok: true`).
- **Path normalization:** Convert all file paths to the operating system's normalized absolute format (`Path.resolve()`) to prevent duplicates caused by different separators or relative paths.
- **Exception handling:** Catch `requests.exceptions.Timeout` and `RequestException` without interrupting the scan of remaining files.

## Consequences
- Preserves the integrity of the JSON history, even with unstable connections.
- Files that fail to send are not marked as sent, allowing them to be retried automatically on the next run.