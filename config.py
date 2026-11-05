import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    TARGET_DIRECTORY = os.getenv("TARGET_DIRECTORY")
    
    SUPPORTED_VIDEO_EXTENSIONS = {".mp4", ".mov", ".avi", ".mkv"}
    SUPPORTED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".heic"}
    
    @classmethod
    def validate(cls):
        if not cls.TELEGRAM_BOT_TOKEN or not cls.TELEGRAM_CHAT_ID or not cls.TARGET_DIRECTORY:
            raise ValueError("Error: Required environment variables are not configured in the .env file.")

if __name__ == "__main__":
    Config.validate()