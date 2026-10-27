"""Punto de entrada: python main.py "tu idea de negocio"."""
import sys
from colmena import config
from colmena.coordinador import Coordinador

OBJETIVO_EJEMPLO = "Una app para que estudiantes intercambien libros usados"

if __name__ == "__main__":
    objetivo = " ".join(sys.argv[1:]) or OBJETIVO_EJEMPLO
    print(f"⚙️  Modo: {config.MODO}" + ("  (respuestas de ejemplo, sin IA)" if config.MODO == "simulado" else f"  ·  modelo: {config.CLAUDE_MODEL}"))
    Coordinador().ejecutar(objetivo)
    print("\n✅ Colmena terminada")
