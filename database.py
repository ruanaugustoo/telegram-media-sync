import json
from pathlib import Path

class JsonDatabase:
    def __init__(self, db_path: str = "sent_media.json"):
        self.db_path = Path(db_path)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not self.db_path.exists():
            self._save_data({"sent_files": []})

    def _load_data(self) -> dict:
        try:
            with open(self.db_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"sent_files": []}

    def _save_data(self, data: dict):
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def _normalize_path(self, file_path: str) -> str:
        """Return the absolute path normalized for the current operating system."""
        return str(Path(file_path).resolve())

    def is_sent(self, file_path: str) -> bool:
        data = self._load_data()
        normalized_path = self._normalize_path(file_path)
        return normalized_path in data.get("sent_files", [])

    def mark_as_sent(self, file_path: str):
        data = self._load_data()
        normalized_path = self._normalize_path(file_path)
        if normalized_path not in data["sent_files"]:
            data["sent_files"].append(normalized_path)
            self._save_data(data)