# 🐝 wdevs-agent-swarm

**Una colmena de agentes de IA en Python, construida desde cero.**
Proyecto de la serie de Reels de **BenwardDevs**: 4 episodios para aprender a construir, entender y reutilizar un sistema multiagente.

Un **coordinador** recibe una idea de negocio y la lleva, en orden, por cuatro agentes especializados:

```
Idea → 🔎 Investigador → 🧠 Estratega → 🧪 Evaluador ──APROBADO──→ ✍️ Redactor → Resumen final
                              ↑              │
                              └── MEJORAR ───┘   (máximo 1 revisión)
```

| Agente | Qué recibe | Qué entrega |
|---|---|---|
| Investigador | la idea | público, problema y un riesgo principal |
| Estratega | idea + investigación | propuesta en 3 pasos |
| Evaluador | la propuesta | `VEREDICTO: APROBADO` o `VEREDICTO: MEJORAR` + observaciones |
| Redactor | todo lo anterior | resumen final de máximo 5 líneas |

---

## 📺 Episodios

| # | Episodio | Qué aprendes |
|---|---|---|
| 1 | Prepara tu entorno | Python, terminal, entorno virtual, pip y `.env` |
| 2 | Construye la colmena | Agente vs función vs coordinador, y el código completo |
| 3 | Cómo funciona por dentro | Librerías, SDK, flujo de datos y personalización *(próximamente)* |
| 4 | Usa y reutiliza la colmena | Importar agentes en otros programas, límites y seguridad *(próximamente)* |

---

## ⚙️ Requisitos

- **Python 3.10 o superior** (probado con 3.13): [python.org](https://www.python.org/downloads/). En Windows marca **"Add python.exe to PATH"** al instalar.
- Una terminal: **PowerShell** (Windows) o **Terminal** (macOS/Linux).
- *(Solo para IA real)* una clave de API de Anthropic. Mira [Usar IA real](#-usar-ia-real-modo-claude).

---

## 🚀 Instalación

**Windows (PowerShell)**
```powershell
git clone https://github.com/benwardjd-ai/wdevs-agent-swarm.git
cd wdevs-agent-swarm
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```
> Si PowerShell dice que la ejecución de scripts está deshabilitada, ejecuta una sola vez
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a activar el entorno.

**macOS / Linux**
```bash
git clone https://github.com/benwardjd-ai/wdevs-agent-swarm.git
cd wdevs-agent-swarm
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

¿No usas Git? Pulsa **Code → Download ZIP**, descomprímelo y sigue desde `python -m venv .venv`.

---

## ▶️ Ejecutar

Con el entorno activo (verás `(.venv)` al inicio de la línea):

```bash
python main.py
python main.py "Una tienda en línea de plantas"
```

Si al final ves **`✅ Colmena terminada`**, todo funcionó.

---

## 🔀 Dos modos

El modo se elige en el archivo `.env`, sin tocar el código:

| `MODO=` | Qué hace | Costo |
|---|---|---|
| `simulado` *(por defecto)* | Usa **respuestas de ejemplo predefinidas**. Sirve para ver el flujo. **No es IA.** | Gratis, sin internet |
| `claude` | Cada agente envía sus instrucciones a un modelo real de Anthropic | Pago por uso |

---

## 🤖 Usar IA real (modo `claude`)

1. Crea una cuenta en la **Claude Console**: [platform.claude.com](https://platform.claude.com), agrega crédito y genera una **clave de API**.
2. Abre tu archivo `.env` y edítalo:
   ```
   MODO=claude
   ANTHROPIC_API_KEY=tu-clave-aquí
   CLAUDE_MODEL=claude-haiku-5-5
   ```
3. Ejecuta `python main.py`.

**Sobre los costos:** la API de Anthropic se cobra **por separado** de las suscripciones a Claude (Pro, Max…). Cada ejecución hace entre 4 y 6 llamadas con un máximo de 700 tokens de salida cada una. Con `claude-haiku-5-5` el costo estimado es menor a un centavo de dólar por ejecución, pero los precios cambian: revisa siempre los precios vigentes y tu consumo en la consola.

---

## 📁 Estructura

```
wdevs-agent-swarm/
├── main.py              ← punto de entrada
├── requirements.txt     ← librerías: anthropic, python-dotenv
├── .env.example         ← plantilla de configuración (sin claves)
├── .gitignore           ← evita subir .venv y .env
└── colmena/
    ├── __init__.py      ← convierte la carpeta en un paquete importable
    ├── config.py        ← lee el archivo .env
    ├── cerebro.py       ← genera texto: simulado o con Claude
    ├── agentes.py       ← clase Agente y los 4 especialistas
    └── coordinador.py   ← orden de trabajo y paso de resultados
```

---

## ⚠️ Lo que este proyecto hace (y lo que no)

- ✅ Los agentes trabajan **en orden, uno por uno**. **No** trabajan en paralelo.
- ✅ El coordinador es el único que pasa información de un agente a otro. Los agentes **no hablan entre sí** ni comparten memoria.
- ✅ La segunda vuelta (estratega → evaluador) ocurre porque **está programada** en `coordinador.py`, con un máximo de 1 revisión.
- ✅ Los agentes **no tienen herramientas**: no navegan por internet ni ejecutan código; solo generan texto.
- ⚠️ La IA puede equivocarse o inventar datos. **Revisa siempre el resultado** antes de usarlo.

---

## 🔒 Seguridad

- **Nunca** publiques tu archivo `.env` ni pegues tu clave en el código, en videos o en capturas de pantalla.
- El `.gitignore` ya excluye `.env` y `.venv/`. Antes de cada `git push`, revisa con `git status` que no se vaya a subir el `.env`.
- Si alguna vez expones una clave, revócala en la consola y crea una nueva.

---

## 🛠️ Problemas comunes

| Mensaje | Solución |
|---|---|
| `python no se reconoce…` | Reinstala Python marcando "Add to PATH", o usa `py` en lugar de `python` |
| `No module named 'dotenv'` o `'anthropic'` | Activa el entorno `(.venv)` y repite `python -m pip install -r requirements.txt` |
| `No module named 'colmena'` | Ejecuta `python main.py` desde la carpeta `wdevs-agent-swarm` |
| `MODO debe ser "simulado" o "claude"` | Revisa que no haya errores de escritura en tu `.env` |
| `❌ Clave inválida…` | Copia de nuevo la clave en `.env`, sin espacios ni comillas |
| `❌ La API respondió con error…` | Revisa `CLAUDE_MODEL` y que tengas crédito en la consola |

---

Hecho con 🐝 por **BenwardDevs** · ¿Construiste algo con tu colmena? Cuéntalo en los comentarios de los Reels.
