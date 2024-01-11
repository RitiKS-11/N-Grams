import os, csv


STOPWORDS = ["a", "about", "above", "after", "again", "against", "all", "am", 
             "an", "and", "any", "are", "aren't", "as", "at", "be", "because", 
             "been", "before", "being", "below", "between", "both", "but", "by", 
             "can't", "cannot", "could", "couldn't", "did", "didn't", "do", 
             "does", "doesn't", "doing", "don't", "down", "during", "each", 
             "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", 
             "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", 
             "here", "here's", "hers", "herself", "him", "himself", "his", "how", 
             "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", 
             "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", 
             "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", 
             "once", "only", "or", "other", "ought", "our", "ours	ourselves", 
             "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", 
             "she's", "should", "shouldn't", "so", "some", "such", "than", 
             "that", "that's", "the", "their", "theirs", "them", "themselves", 
             "then", "there", "there's", "these", "they", "they'd", "they'll", 
             "they're", "they've", "this", "those", "through", "to", "too", 
             "under", "until", "up", "very", "was", "wasn't", "we", "we'd", 
             "we'll", "we're", "we've", "were", "weren't", "what", "what's", 
             "when", "when's", "where", "where's", "which", "while", "who", 
             "who's", "whom", "why", "why's", "with", "won't", "would", 
             "wouldn't", "you", "you'd", "you'll", "you're", "you've", 
             "your", "yours", "yourself", "yourselves"]


def train_and_test_split(filepath):
    with open(filepath, encoding="ISO-8859-1") as file:
        lines = file.readlines()
        total_lines = len(lines)

    training_lines = int(total_lines * 0.6)
    testing_lines = int(total_lines - training_lines)

    testing_data = get_testing_data(filepath, testing_lines)
    training_data = get_training_data(filepath, training_lines)

    return (training_data, testing_data)



def get_training_data(filepath, training_lines):
    training_data = []
    line_count = 0

    with open(filepath, encoding="ISO-8859-1") as file:
        reader = csv.DictReader(file, fieldnames=['sentiment', 'news'])
        for line in reader:
            if line_count > training_lines:
                break

            training_data.append(line)
            line_count += 1
            
    return training_data


def get_testing_data(filepath, testing_lines):
    testing_data = []

    with open(filepath, encoding="ISO-8859-1") as file:
        lines = file.readlines()
        line_count = len(lines) - testing_lines
        reader = csv.DictReader(lines, fieldnames=['sentiment', 'news'])

        for index, line in enumerate(reader, start=1):
            if index > line_count+1:
                testing_data.append(line)
                
    return testing_data

def remove_punctuation(text):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    if type(text) == float:
        return text
   
    ans = ''
    for i in text:
        if i not in punctuation:
            ans += i
    return ans


def remove_stopwords(text):
    if text.lower() not in STOPWORDS:
        return text
    return ''


def clean_data(data):
    for row in data:
        news_words = row['news'].split(' ') 
        removed_stopwords = [remove_stopwords(word) for word in news_words]
        clean_words = [remove_punctuation(word) for word in removed_stopwords]
        news = ' '.join(clean_words)
        row['news'] = news
    
    print(data)
    return data

    
def generate_n_grams(news, ngram):
    pass
        


