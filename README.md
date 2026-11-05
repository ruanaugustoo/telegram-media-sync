# Telegram Media Sync 🚀

A Python automation tool that recursively scans directories (including subfolders), finds new photos and videos, and automatically sends them to a Telegram chat or channel. It uses each filename as the caption and prevents duplicates with a local JSON database.

## 🛠️ Technologies
- Python 3.x
- `requests` (HTTP requests to the Telegram API)
- `python-dotenv` (environment variable management)

## 🧰 Features

- 📁 **Recursive scanning:** Finds images and videos at any subfolder depth.
- 🏷️ **Clean captions:** Uses the filename without its extension (e.g., `vacation_2026`) as the Telegram caption.
- 🛡️ **Duplicate prevention:** Records files in the local JSON database (`sent_media.json`) only after the API confirms delivery, making the process resilient to network failures and timeouts.
- 🔄 **Path normalization:** Works across Windows, Linux, and macOS.

## 📦 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/telegram-media-sync.git
   cd telegram-media-sync
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the `.env` file:**
   Copy the example file and add your credentials:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` (use the `-100` prefix for channels and supergroups), and `TARGET_DIRECTORY`.

5. **Run the script:**
   ```bash
   python main.py
   ```
