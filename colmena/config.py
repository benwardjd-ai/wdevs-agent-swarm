"""Lee la configuración desde el archivo .env (nunca escribas claves en el código)."""
import os
from dotenv import load_dotenv

load_dotenv()  # carga las variables de .env en el entorno

MODO = os.getenv("MODO", "simulado").strip().lower()
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-haiku-5-5")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "700"))

if MODO not in ("simulado", "claude"):
    raise ValueError(f'MODO debe ser "simulado" o "claude", no "{MODO}"')
