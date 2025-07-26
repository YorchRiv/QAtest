from graphviz import Digraph

def generar_diagrama():
    dot = Digraph("Encuestas")
    
    # Nodos principales
    dot.node("Inicio", "Inicio (Usuario inicia sesión)")
    dot.node("CrearEncuesta", "Crear Encuesta")
    dot.node("EditarEncuesta", "Editar Encuesta")
    dot.node("GuardarBorrador", "Guardar como Borrador")
    dot.node("PublicarEncuesta", "Publicar Encuesta")
    dot.node("EnviarEncuesta", "Enviar Encuesta (Correo/SMS)")
    dot.node("RecibirNotificacion", "Recibir Notificación")
    dot.node("ResponderEncuesta", "Responder Encuesta")
    dot.node("AlmacenarRespuestas", "Almacenar Respuestas")
    dot.node("AnalizarResultados", "Analizar Resultados")
    dot.node("ExportarDatos", "Exportar a Excel/PDF")
    dot.node("Fin", "Fin (Usuario cierra sesión)")
    
    # Conexiones
    dot.edge("Inicio", "CrearEncuesta")
    dot.edge("CrearEncuesta", "EditarEncuesta")
    dot.edge("EditarEncuesta", "GuardarBorrador", label="¿Guardar como borrador?")
    dot.edge("EditarEncuesta", "PublicarEncuesta", label="¿Publicar encuesta?")
    dot.edge("PublicarEncuesta", "EnviarEncuesta")
    dot.edge("EnviarEncuesta", "RecibirNotificacion")
    dot.edge("RecibirNotificacion", "ResponderEncuesta")
    dot.edge("ResponderEncuesta", "AlmacenarRespuestas")
    dot.edge("AlmacenarRespuestas", "AnalizarResultados")
    dot.edge("AnalizarResultados", "ExportarDatos", label="¿Exportar reporte?")
    dot.edge("ExportarDatos", "Fin")
    dot.edge("AnalizarResultados", "Fin", label="No exportar")
    
    return dot

diagrama = generar_diagrama()
diagrama.render("diagrama_flujo_encuestas", format="png", cleanup=False)