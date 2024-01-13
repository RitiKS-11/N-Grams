import matplotlib.pyplot as plt

from pkg.models import get_result


def provide_result(filepath='all-data.csv'):
    result = get_result(filepath)

    positive = sum(result['positive'].values())
    negative = sum(result['negative'].values())
    neutral = sum(result['neutral'].values())

    return [positive, neutral, negative]


def sentiment_chart(result):

    labels = ['Positive', 'Neutral', 'Negative']

    plt.pie(result, labels=labels, explode=[0.2, 0, 0], shadow=True, startangle=90)
    plt.title('Sentiment Distribution')
    plt.legend(title='Sentiment', loc='upper right')
    plt.show()


def sentiment_bargraph(result):

    x = ['Positive', 'Neutral', 'Negative']
    y = result

    plt.title('Sentiment Distribution')
    plt.xlabel('Senitiments')
    plt.ylabel('Number of words')
    plt.bar(x,y)
    plt.show()


if __name__ == "__main__":
    result = provide_result()
    sentiment_bargraph(result)
    sentiment_chart(result)