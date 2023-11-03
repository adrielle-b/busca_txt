from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file_list = [
        instance.search(i)['nome_do_arquivo'] for i in range(len(instance))
    ]

    if path_file not in file_list:
        lines = txt_importer(path_file)
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines
        }
        instance.enqueue(data)
        print(data, file=sys.stdout)

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
