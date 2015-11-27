def get_stop_words():
    '''
    return set of stopwords
    '''
    stopwords = []
    for word in open('stopwords.txt'):
        stopwords.append(word.strip())
    return set(stopwords)


def get_sentimental_word():
    '''
    return set of sentiment words
    '''

    words = []
    for word in open('sentiment_words.txt'):
        words.append(word.strip())
    return set(words)
