"""
Organiza a pasta Downloads: move cada ficheiro para uma subpasta
conforme a extensão (Imagens, Videos, Musica, Documentos, ...).

Uso:
    python organizar_downloads.py            # organiza de verdade
    python organizar_downloads.py --teste    # só mostra o que faria, não move nada
"""

import shutil
import sys
from pathlib import Path


PASTA = Path(r"E:\downloads")

# Categoria -> extensões que lhe pertencem
CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".heic"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm"],
    "Musica": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".odt", ".xls", ".xlsx", ".csv", ".ppt", ".pptx"],
    "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programas": [".exe", ".msi", ".dmg", ".deb", ".appimage"],
    "Codigo": [".py", ".js", ".ts", ".html", ".css", ".json", ".sql"],
}

# Ficheiros com extensões que não estão na lista vão para aqui
PASTA_OUTROS = "Outros"


def descobrir_categoria(ficheiro: Path) -> str:
    """Devolve o nome da pasta de destino para um ficheiro."""
    extensao = ficheiro.suffix.lower()  # ".JPG" -> ".jpg"
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria
    return PASTA_OUTROS


def caminho_livre(destino: Path) -> Path:
    """Se já existir um ficheiro com o mesmo nome, acrescenta (1), (2)..."""
    if not destino.exists():
        return destino
    contador = 1
    while True:
        novo = destino.with_name(f"{destino.stem} ({contador}){destino.suffix}")
        if not novo.exists():
            return novo
        contador += 1


def organizar(pasta: Path, modo_teste: bool = False) -> None:
    if not pasta.exists():
        print(f"A pasta {pasta} não existe.")
        return

    movidos = 0
    for item in pasta.iterdir():
        # Ignora pastas e ficheiros ocultos (ex: .DS_Store)
        if item.is_dir() or item.name.startswith("."):
            continue

        categoria = descobrir_categoria(item)
        pasta_destino = pasta / categoria
        destino = caminho_livre(pasta_destino / item.name)

        if modo_teste:
            print(f"[teste] {item.name} -> {categoria}/")
        else:
            pasta_destino.mkdir(exist_ok=True)  # cria a pasta se não existir
            shutil.move(str(item), str(destino))
            print(f"{item.name} -> {categoria}/{destino.name}")
        movidos += 1

    print(f"\nTotal: {movidos} ficheiro(s) {'a mover' if modo_teste else 'movidos'}.")


if __name__ == "__main__":
    modo_teste = "--teste" in sys.argv
    organizar(PASTA, modo_teste)