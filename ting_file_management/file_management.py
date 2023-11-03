import sys

def txt_importer(path_file):
    if ".txt" not in path_file:
        return print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file) as file:
            content = file.read()
            lines = content.split("\n")
        return lines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
