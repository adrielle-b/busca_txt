from ting_file_management.priority_queue import PriorityQueue
import pytest


mock_data = [
    {
        "nome_do_arquivo": "file1.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["line_1", "line_2", "line_3", "line_4"]
    },
    {
        "nome_do_arquivo": "file2.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [
            "line_1", "line_2", "line_3", "line_4", "line_5", "line_6"
            ]
    },
    {
        "nome_do_arquivo": "file3.txt",
        "qtd_linhas": 7,
        "linhas_do_arquivo": [
            "line1", "line2", "line3", "line4", "line5", "line6", "line7"
            ]
    },
    {
        "nome_do_arquivo": "file4.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": ["line_1", "line_2"]
    }
]


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    for data in mock_data:
        priority_queue.enqueue(data)

    assert priority_queue.__len__() == len(mock_data)
    assert priority_queue.search(0) == mock_data[0]
    assert priority_queue.dequeue() == mock_data[0]
    assert priority_queue.__len__() == len(mock_data) - 1
    assert priority_queue.search(0) == mock_data[3]

    with pytest.raises(IndexError):
        priority_queue.search(5)
