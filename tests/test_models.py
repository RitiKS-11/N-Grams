import pytest

from pkg.models import get_result, get_unigrams

@pytest.fixture
def fielpath():
    return 'all-data.csv'

def test_get_result(filepath):
    excepted_result = {'positive': {}, 'negative': {}, 'neutral': {'According': 1, 'Gran': 1, 'company': 2, 'plans': 2, 'move': 1, 'production': 1, 'Russia': 1, 'although': 1, 'growing': 1, 'Technopolis': 1, 'develop': 1, 'stages': 1, 'area': 1, 'less': 1, '100000': 1, 'square': 1, 'meters': 1, 'order': 1, 'host': 1, 'companies': 1, 'working': 1, 'computer': 1, 'technologies': 1, 'telecommunications': 1, 'statement': 1, 'said': 1}}

    assert get_result('all-data.csv') == excepted_result


if __name__ == "__main__":
    test_get_result('all-data.csv')