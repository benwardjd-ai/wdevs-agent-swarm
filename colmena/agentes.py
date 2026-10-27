"""Un agente = un nombre + unas instrucciones (su rol) + el cerebro que genera respuestas."""
from colmena.cerebro import pensar


class Agente:
    def __init__(self, nombre: str, instrucciones: str):
        self.nombre = nombre
        self.instrucciones = instrucciones

    def trabajar(self, tarea: str) -> str:
        """Recibe una tarea en texto y devuelve su resultado en texto."""
        return pensar(self.instrucciones, tarea, rol=self.nombre)


# Los cuatro especialistas de la colmena
investigador = Agente("investigador",
    "Eres un investigador de negocios. Analiza la idea en máximo 3 viñetas: "
    "público objetivo, problema que resuelve y un riesgo principal. Sé concreto.")

estratega = Agente("estratega",
    "Eres un estratega de producto. Con base en la investigación, propone una solución "
    "en máximo 3 pasos numerados. No inventes cifras.")

evaluador = Agente("evaluador",
    "Eres un evaluador crítico. Revisa la propuesta con estos criterios: claridad, "
    "viabilidad y riesgos. Empieza tu respuesta con 'VEREDICTO: APROBADO' o "
    "'VEREDICTO: MEJORAR' y luego explica en máximo 3 viñetas.")

redactor = Agente("redactor",
    "Eres un redactor. Une todo en un resumen final de máximo 5 líneas, "
    "claro para alguien que no es experto.")
