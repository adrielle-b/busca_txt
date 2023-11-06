def exists_word(word, instance):
    result_search = []

    for index in instance._queue:
        ocurrences = []

        for line_number, line in enumerate(index["linhas_do_arquivo"], 1):
            if word.lower() in line.lower():
                ocurrences.append({"linha": line_number})

        if ocurrences:
            result_search.append({
                "palavra": word,
                "arquivo": index['nome_do_arquivo'],
                "ocorrencias": ocurrences
            })
    return result_search


def search_by_word(word, instance):
    result_search = []

    for index in instance._queue:
        ocurrences = []

        for line_number, line in enumerate(index["linhas_do_arquivo"], 1):
            if word.lower() in line.lower():
                ocurrences.append({"linha": line_number, "conteudo": line})

        if ocurrences:
            result_search.append({
                    "palavra": word,
                    "arquivo": index["nome_do_arquivo"],
                    "ocorrencias": ocurrences,
                })
    return result_search
