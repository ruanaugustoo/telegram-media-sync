from pathlib import Path
from config import Config
from database import JsonDatabase
from telegram_service import TelegramService

def main():
    try:
        Config.validate()
    except ValueError as e:
        print(e)
        return

    target_dir = Path(Config.TARGET_DIRECTORY)
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"❌ Error: Target directory '{target_dir}' is invalid or does not exist.")
        return

    db = JsonDatabase("sent_media.json")
    telegram = TelegramService(Config.TELEGRAM_BOT_TOKEN, Config.TELEGRAM_CHAT_ID)

    all_extensions = Config.SUPPORTED_VIDEO_EXTENSIONS.union(Config.SUPPORTED_IMAGE_EXTENSIONS)

    print(f"🔍 Scanning directory: {target_dir.resolve()}\n")

    processed_count = 0
    skipped_count = 0
    failed_count = 0

    for file_path in target_dir.rglob("*"):
        if file_path.is_file() and file_path.suffix.lower() in all_extensions:
            file_key = str(file_path.resolve())

            if db.is_sent(file_key):
                skipped_count += 1
                continue

            print(f"📤 Sending new file: {file_path.name}...")

            caption = file_path.stem

            success = telegram.send_media(file_path, caption)

            if success:
                db.mark_as_sent(file_key)
                processed_count += 1
            else:
                failed_count += 1
                print(f"⚠️ {file_path.name} was NOT added to the history because sending failed.\n")

    print("==================================================")
    print("Processing complete!")
    print(f"   • Newly sent: {processed_count}")
    print(f"   • Already sent (skipped): {skipped_count}")
    print(f"   • Temporary failures: {failed_count}")
    print("==================================================")

if __name__ == "__main__":
    main()