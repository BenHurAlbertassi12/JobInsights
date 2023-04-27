from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
    #  precisei fazer uma atualização no código
    #  constava o erro UnicodeDecodeError, fui na mentoria pediram para
    #  mudar para o linux, antes de mudar fiz umas buscas no google cheguei
    #  no stackoverflow com esta resposta, apos fazer alteração passou
    #  open(os.path.join(url,file), encoding = "utf8")
    #  https://pt.stackoverflow.com/questions/130168/unicodedecodeerror-utf-8


def get_unique_job_types(path: str) -> List[str]:
    read_list = read(path)
    return {job["job_type"] for job in read_list}

    #  notas_por_genero = {genre: [] for genre in game_genres}
    #  retirado do lecture/cs/1.2


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]

    # usei como base para resolução deste requisito
    # os exercicios do course, em req 4, solução,
    # aproximadamente na linha 12 a 15

    #  for book in books:
    #         for category in book["categories"]:
    #             if not categories.get(category):
    #                 categories[category] = 0
