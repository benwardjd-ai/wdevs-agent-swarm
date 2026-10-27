"""El coordinador decide el orden de trabajo y pasa los resultados de un agente al siguiente.

Importante: los agentes NO hablan entre sí ni trabajan en paralelo.
El coordinador los llama uno por uno, en orden, y es el único que mueve la información.
"""
from colmena.agentes import investigador, estratega, evaluador, redactor


class Coordinador:
    def __init__(self, max_revisiones: int = 1, mostrar: bool = True):
        self.max_revisiones = max_revisiones
        self.mostrar = mostrar
        self.bitacora = []  # registro de qué hizo cada agente

    def _registrar(self, agente: str, resultado: str):
        self.bitacora.append({"agente": agente, "resultado": resultado})
        if self.mostrar:
            print(f"\n🐝 [{agente.upper()}]\n{resultado}")

    def ejecutar(self, objetivo: str) -> str:
        if self.mostrar:
            print(f"🎯 Objetivo: {objetivo}")

        hallazgos = investigador.trabajar(f"Idea a analizar: {objetivo}")
        self._registrar("investigador", hallazgos)

        propuesta = estratega.trabajar(f"Idea: {objetivo}\n\nInvestigación:\n{hallazgos}")
        self._registrar("estratega", propuesta)

        for intento in range(self.max_revisiones + 1):
            revision = evaluador.trabajar(f"Propuesta a revisar:\n{propuesta}")
            self._registrar("evaluador", revision)
            if "VEREDICTO: APROBADO" in revision.upper() or intento == self.max_revisiones:
                break
            # Si el evaluador pide mejoras, el coordinador vuelve a llamar al estratega
            propuesta = estratega.trabajar(
                f"Idea: {objetivo}\n\nPropuesta anterior:\n{propuesta}\n\n"
                f"Corrige según esta revisión:\n{revision}")
            self._registrar("estratega", propuesta)

        final = redactor.trabajar(
            f"Idea: {objetivo}\nInvestigación:\n{hallazgos}\n"
            f"Propuesta:\n{propuesta}\nRevisión:\n{revision}")
        self._registrar("redactor", final)
        return final
