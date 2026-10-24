"""Genera docs/index.html a partir de datos/cv.json y plantilla.html.

Uso: python construir.py
"""
import json
from pathlib import Path

raiz = Path(__file__).parent
datos = json.loads((raiz / "datos" / "cv.json").read_text(encoding="utf-8"))
plantilla = (raiz / "plantilla.html").read_text(encoding="utf-8")

# "</" dentro del JSON cerraría la etiqueta script
cuerpo = json.dumps(datos, ensure_ascii=False).replace("</", "<\\/")
salida = plantilla.replace("/*DATOS*/", cuerpo)

destino = raiz / "docs" / "index.html"
destino.write_text(salida, encoding="utf-8")
(raiz / "docs" / ".nojekyll").write_text("", encoding="utf-8")
print("Generado", destino, f"({len(salida) // 1024} KB)")
