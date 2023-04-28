from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    return max([int(job["max_salary"])
                for job in read(path)
                if job["max_salary"].isnumeric()])

# https://www.w3schools.com/python/ref_string_isnumeric.asp#
# verifica se tudo o que ela recebe é numero


def get_min_salary(path: str) -> int:
    return min([int(job["min_salary"])
                for job in read(path)
                if job["min_salary"].isnumeric()])


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        max_salary = int(job["max_salary"])
        min_salary = int(job["min_salary"])

        if max_salary < min_salary:
            raise TypeError()
        # typeerror se o salario maximo for maior que o minimou
        # ou se não der para converter para inteiro
        # o exercicio só passou depois que fiz essa converção
        salary = int(salary)
        # converte o salary para inteiro

        return min_salary <= salary <= max_salary
    except (TypeError, KeyError, ValueError):
        #  marcações de erros do course "Lidando com exceções"
        #  keyerror https://docs.python.org/3/library/exceptions.html
        raise ValueError("Ta errada a bagaça")


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:

    salary_range = []
    for job in jobs:
        try:
            if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
                #  converte geral pra inteiro e compara
                salary_range.append(job)
                # add um trabalho na lista de trabalhos pelo salario comparado
        except (TypeError, ValueError):
            pass
    return salary_range
