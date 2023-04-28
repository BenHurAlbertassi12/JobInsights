from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    for job in read_brazilian_file("tests/mocks/brazilians_jobs.csv"):
        keys = set()
        for key in job.keys():
            keys.add(key)
            # adiciona as key ao conjunto keys

    assert keys == {"title", "salary", "type"}
    # assert para comparar os resultados
