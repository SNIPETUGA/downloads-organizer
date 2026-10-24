# Downloads Organizer

A small Python script that cleans up a messy Downloads folder by moving each file into a subfolder based on its type.

```
Downloads/
├── Imagens/      .jpg .png .gif .webp ...
├── Videos/       .mp4 .mkv .mov ...
├── Musica/       .mp3 .wav .flac ...
├── Documentos/   .pdf .docx .xlsx .csv ...
├── Comprimidos/  .zip .rar .7z ...
├── Programas/    .exe .msi .dmg ...
├── Codigo/       .py .js .ts .html .sql ...
└── Outros/       anything else
```

## Features

- Sorts files into categories by extension (case-insensitive: `.JPG` = `.jpg`)
- **Dry-run mode** (`--teste`) to preview what would happen without moving anything
- Never overwrites: if a file with the same name already exists, it renames it to `file (1).ext`, `file (2).ext`, ...
- Skips folders and hidden files
- No external dependencies — uses only the Python standard library

## Requirements

- Python 3.8+

## Usage

1. Set the folder to organize in `organizar_downloads.py`:
   ```python
   PASTA = Path(r"E:\downloads")
   ```
2. Preview first (recommended):
   ```bash
   python organizar_downloads.py --teste
   ```
3. Organize for real:
   ```bash
   python organizar_downloads.py
   ```

Example output:
```
foto.jpg -> Imagens/foto.jpg
relatorio.pdf -> Documentos/relatorio.pdf
setup.exe -> Programas/setup.exe

Total: 3 ficheiro(s) movidos.
```

## Customizing

Add or change categories by editing the `CATEGORIAS` dictionary:
```python
CATEGORIAS = {
    "Imagens": [".jpg", ".png", ...],
    "Livros": [".epub", ".mobi"],   # new category
}
```

## Built with

- `pathlib` — file paths
- `shutil` — moving files
- `sys` — command-line arguments

## Possible improvements

- Pass the folder path as a command-line argument instead of hardcoding it
- Add an undo option
- Run automatically on a schedule
