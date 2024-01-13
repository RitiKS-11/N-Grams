from collections import defaultdict

from pkg.main import generate_n_grams, get_training_data, clean_data, train_and_test_split

def get_result(filepath):
    result = []

    train_data, test_n = train_and_test_split(filepath)
    cleaned_data = clean_data(train_data)

    for data in cleaned_data:
        result.append(data)
    
    res = get_unigrams(result)
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

def get_bigrams(result):
    postive_sentiments = defaultdict(int)
    negative_sentiments = defaultdict(int)
    neutral_sentiments = defaultdict(int)

    for row in result:
        if row['sentiment'] == 'positive':
            for word in generate_n_grams(row['news'],2):
                postive_sentiments[word] += 1

    for row in result:
        if row['sentiment'] == 'negative':
            for word in generate_n_grams(row['news'],2):
                negative_sentiments[word] += 1

    for row in result:
        if row['sentiment'] == 'neutral':
            for word in generate_n_grams(row['news'],2):
                neutral_sentiments[word] += 1


    return {'positive':dict(postive_sentiments), 'negative':dict(negative_sentiments), 'neutral':dict(neutral_sentiments)}


def get_trigrams(result):
    postive_sentiments = defaultdict(int)
    negative_sentiments = defaultdict(int)
    neutral_sentiments = defaultdict(int)

    for row in result:
        if row['sentiment'] == 'positive':
            for word in generate_n_grams(row['news'],3):
                postive_sentiments[word] += 1

    for row in result:
        if row['sentiment'] == 'negative':
            for word in generate_n_grams(row['news'],3):
                negative_sentiments[word] += 1

    for row in result:
        if row['sentiment'] == 'neutral':
            for word in generate_n_grams(row['news'],3):
                neutral_sentiments[word] += 1


    return {'positive':dict(postive_sentiments), 'negative':dict(negative_sentiments), 'neutral':dict(neutral_sentiments)}


def sort_result(result):
    sorted_positive = dict(sorted(result['positive'].items(), key=lambda item: item[1], reverse=True))
    sorted_negative = dict(sorted(result['negative'].items(), key=lambda item: item[1], reverse=True))
    sorted_netural = dict(sorted(result['neutral'].items(), key=lambda item: item[1], reverse=True))
    return {'positive':sorted_positive, 'negative':sorted_negative, 'neutral':sorted_netural}

