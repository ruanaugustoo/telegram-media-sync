# 0001. Local JSON History Storage

## Context
The application needs to track media (photos and videos) already sent to Telegram to prevent duplicates in future runs.

## Decision
Use a local JSON file (`sent_media.json`) to store the absolute paths or identifiers of processed files.

## Rationale
- **Simplicity:** For the initial scope and moderate file volumes, JSON can be read and written quickly without introducing complex external dependencies.
- **Transparency:** Makes it easy to manually inspect and debug the send history without requiring a database client.
- **Portability:** Works across operating systems without requiring a database installation.

## Consequences
- Reading and writing the entire file may become inefficient as the media collection grows significantly.
- The storage can later be migrated to **SQLite** by refactoring the `JsonDatabase` class without changing the interface used by `main.py`.