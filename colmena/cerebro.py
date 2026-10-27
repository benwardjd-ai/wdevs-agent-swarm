"""El "cerebro" de los agentes: genera texto a partir de instrucciones.

- Modo "simulado": respuestas de ejemplo, sin internet ni costo. Sirve para ver el flujo.
- Modo "claude": envía las instrucciones a un modelo real mediante la API de Anthropic.
"""
from colmena import config


def pensar(instrucciones: str, mensaje: str, rol: str) -> str:
    if config.MODO == "simulado":
        return _simular(rol, mensaje)
    return _preguntar_a_claude(instrucciones, mensaje)


def _preguntar_a_claude(instrucciones: str, mensaje: str) -> str:
    import anthropic  # librería oficial (SDK) de Anthropic

    cliente = anthropic.Anthropic()  # lee ANTHROPIC_API_KEY del entorno
    try:
        respuesta = cliente.messages.create(
            model=config.CLAUDE_MODEL,
            max_tokens=config.MAX_TOKENS,
            system=instrucciones,                       # el rol del agente
            messages=[{"role": "user", "content": mensaje}],
        )
    except anthropic.AuthenticationError:
        raise SystemExit("❌ Clave inválida: revisa ANTHROPIC_API_KEY en tu archivo .env")
    except anthropic.APIConnectionError:
        raise SystemExit("❌ Sin conexión con la API: revisa tu internet")
    except anthropic.APIStatusError as e:
        raise SystemExit(f"❌ La API respondió con error {e.status_code}: {e.message}")
    return "".join(b.text for b in respuesta.content if b.type == "text").strip()


# Respuestas de ejemplo para el modo simulado (NO son inteligencia artificial)
_EJEMPLOS = {
    "investigador": "- Público: estudiantes universitarios con poco presupuesto.\n"
                    "- Problema: los libros nuevos son caros y se usan un semestre.\n"
                    "- Riesgo: confianza entre desconocidos al intercambiar.",
    "estratega": "Propuesta: app de intercambio de libros por campus.\n"
                 "1. Publicar un libro con foto y materia.\n"
                 "2. Intercambio en puntos seguros dentro de la universidad.\n"
                 "3. Calificaciones entre usuarios para generar confianza.",
    "evaluador": "VEREDICTO: APROBADO\n- Claridad: buena.\n- Viabilidad: alta para un piloto.\n"
                 "- Mejora sugerida: definir cómo se validan las calificaciones.",
    "redactor": "RESUMEN FINAL\nIdea: app de intercambio de libros entre estudiantes.\n"
                "Por qué: reduce costos y reutiliza libros.\n"
                "Primer paso: piloto en un solo campus con 50 usuarios.",
}


def _simular(rol: str, mensaje: str) -> str:
    return _EJEMPLOS.get(rol, f"(simulación) {rol} procesó: {mensaje[:60]}…")
