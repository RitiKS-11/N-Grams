from collections import defaultdict

from pkg.main import generate_n_grams, get_training_data, clean_data

def get_result(filepath):
    result = []

    train_data = get_training_data(filepath, 1)
    cleaned_data = clean_data(train_data)

    for data in cleaned_data:
        result.append(data)
    
    res = get_unigrams(result)
    print(res)
    
    return res


def get_unigrams(result):
    postive_sentiments = defaultdict(int)
    negative_sentiments = defaultdict(int)
    neutral_sentiments = defaultdict(int)

    for row in result:
        if row['sentiment'] == 'positive':
            for word in generate_n_grams(row['news'],1):
                postive_sentiments[word] += 1

    for row in result:
        if row['sentiment'] == 'negative':
            for word in generate_n_grams(row['news'],1):
                negative_sentiments[word] += 1

    for row in result:
        if row['sentiment'] == 'neutral':
            for word in generate_n_grams(row['news'],1):
                neutral_sentiments[word] += 1


    return {'positive':dict(postive_sentiments), 'negative':dict(negative_sentiments), 'neutral':dict(neutral_sentiments)}




