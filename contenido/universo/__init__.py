# Contenido de la sección Universo. Cada ficha: slug (es, en), título, resumen, palabras clave,
# foto de portada, datos (etiqueta es, etiqueta en, valor es, valor en) y el texto en castellano e inglés.
# Formato del texto: párrafos separados por línea en blanco, "## " subtítulo, "!foto clave | pie",
# "> " recuadro «¿Sabías que…?», "- " listas, tablas con |, "!sim nombre" simulador,
# [texto](@slug-de-otra-ficha) enlace interno, **negrita**.


def F(slug, titulo, resumen, claves, foto, es, en, datos=(), pie=None):
    return dict(slug=slug, titulo=titulo, resumen=resumen, claves=claves, foto=foto, es=es, en=en,
                datos=list(datos), pie=pie or titulo)
