# Maxfiy kalitlar bu faylda EMAS, `.env` faylida saqlanadi.
# `.env.example` faylidan nusxa olib, `.env` deb nomlang va qiymatlarni yozing.
# `.env` .gitignore ga kiritilgan — uni hech qachon GitHub'ga yuklamang.
import os
from pathlib import Path


def _load_env(path: Path) -> None:
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


_load_env(Path(__file__).with_name(".env"))

ADMIN_BOT_TOKEN = os.getenv("ADMIN_BOT_TOKEN", "")
STUDENT_BOT_TOKEN = os.getenv("STUDENT_BOT_TOKEN", "")

# Saytga real vaqt sinxronizatsiyasi uchun GitHub Fine-grained token.
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GITHUB_OWNER = os.getenv("GITHUB_OWNER", "ibotovdavron0-maker")
GITHUB_REPO = os.getenv("GITHUB_REPO", "sofi-ollohyor")
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH", "main")
SHOW_FULL_STUDENT_NAMES = os.getenv("SHOW_FULL_STUDENT_NAMES", "false").lower() == "true"
