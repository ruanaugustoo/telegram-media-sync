# 0002. File Handling, Formats, and Captions

## Context
The script needs to send both photos and videos using the appropriate Telegram API endpoints (`sendPhoto` and `sendVideo`).

## Decision
- Send files as binary streams using the `requests` library's `files` parameter.
- Filter files by known image extensions (`.jpg`, `.jpeg`, `.png`, `.heic`) and video extensions (`.mp4`, `.mov`, `.avi`, `.mkv`).
- Use only the filename **without its extension** (`file_path.stem`) as the media caption for a cleaner appearance in the Telegram chat.

## Consequences
- Omitting file extensions keeps the Telegram chat uncluttered.
- The code must distinguish file types and select the appropriate endpoint (`sendPhoto` or `sendVideo`).