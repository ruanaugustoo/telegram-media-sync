from pathlib import Path
import requests

class TelegramService:
    def __init__(self, bot_token: str, chat_id: str):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"

    def send_media(self, file_path: Path, caption: str) -> bool:
        """
        Send media to the Telegram API.
        Return True only when Telegram confirms receipt (HTTP 200 and ok: true).
        """
        ext = file_path.suffix.lower()
        
        if ext in {".mp4", ".mov", ".avi", ".mkv"}:
            url = f"{self.base_url}/sendVideo"
            file_key = "video"
        elif ext in {".jpg", ".jpeg", ".png", ".heic"}:
            url = f"{self.base_url}/sendPhoto"
            file_key = "photo"
        else:
            print(f"⚠️ Unsupported extension: {file_path.name}")
            return False

        try:
            with open(file_path, "rb") as file_handle:
                files = {file_key: file_handle}
                data = {
                    "chat_id": self.chat_id,
                    "caption": caption
                }
                
                response = requests.post(url, data=data, files=files, timeout=60)
                
                if response.status_code == 200:
                    result = response.json()
                    if result.get("ok"):
                        print(f"✅ Sent successfully: {file_path.name}")
                        return True
                    else:
                        print(f"❌ Telegram API error ({file_path.name}): {result.get('description')}")
                        return False
                else:
                    print(f"❌ HTTP {response.status_code} error while sending {file_path.name}: {response.text}")
                    return False

        except requests.exceptions.Timeout:
            print(f"⏰ Connection timed out while sending {file_path.name} (it will be retried on the next run)")
            return False
        except requests.exceptions.RequestException as e:
            print(f"🚨 Network/connection error while sending {file_path.name}: {e}")
            return False
        except Exception as e:
            print(f"🚨 Unexpected error while processing {file_path.name}: {e}")
            return False