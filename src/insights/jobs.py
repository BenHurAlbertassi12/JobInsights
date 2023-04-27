from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def get_unique_job_types(path: str) -> List[str]:
    read_list = read(path)
    job_types = {job: ["job_type"] for job in read_list}
    #  notas_por_genero = {genre: [] for genre in game_genres}
    #  retirado do lecture/cs/1.2

    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
