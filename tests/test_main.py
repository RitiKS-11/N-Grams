import pytest 

from pkg.main import train_and_test_split, get_testing_data, get_training_data, clean_data, remove_punctuation, remove_stopwords

@pytest.fixture
def test_filepath():
    return 'test.csv'

@pytest.fixture
def test_data():
    return [
        {'sentiment':'neutral', 'news':'According to Gran , the company has no plans to move all production to Russia , although that is where the company is growing .'},
        {'sentiment':'neutral', 'news':'Technopolis plans to develop in stages an area of no less than 100,000 square meters in order to host companies working in computer technologies and telecommunications , the statement said .'}
    ]

def test_train_and_test_split(test_filepath):
    train_data, test_data = train_and_test_split(test_filepath)

    print(train_data)
    
    assert train_data == [
        {'sentiment':'neutral', 'news':'According to Gran , the company has no plans to move all production to Russia , although that is where the company is growing .'},
        {'sentiment':'neutral', 'news':'Technopolis plans to develop in stages an area of no less than 100,000 square meters in order to host companies working in computer technologies and telecommunications , the statement said .'}
    ]

    assert test_data == [
        {'sentiment':'negative', 'news':'The international electronic industry company Elcoteq has laid off tens of employees from its Tallinn facility ; contrary to earlier layoffs the company contracted the ranks of its office workers , the daily Postimees reported .'}
        ]


def test_clean_data(test_data):

    assert clean_data(test_data) == [
        {'sentiment': 'neutral', 'news': 'According  Gran   company   plans  move  production  Russia  although     company  growing '}, 
        {'sentiment': 'neutral', 'news': 'Technopolis plans  develop  stages  area   less  100000 square meters  order  host companies working  computer technologies  telecommunications   statement said '}
    ]


@pytest.mark.parametrize('punctuation_string, expected_reulst',[
    ('answer.', 'answer'),
    ('r.e.m.o.v.e', 'remove')
])
def test_remove_punctuation(punctuation_string, expected_reulst):
    assert remove_punctuation(punctuation_string) == expected_reulst


@pytest.mark.parametrize('stopword_string, expected_reulst',[
    ('a', ''),
    ('r.e.m.o.v.e', 'r.e.m.o.v.e')
])
def test_remove_stopwords(stopword_string, expected_reulst):
    assert remove_stopwords(stopword_string) == expected_reulst



if __name__ == "__main__":
    test_remove_punctuation('.a', 'a')