def clean_dataframe(df, tweet_option='remove_hash'):

    clean_df = df.copy()
    # Clean up whitespace.
    clean_df['OriginalTweet'] = clean_df['OriginalTweet'].str.replace('[\n\r]', ' ', regex=True)
    clean_df['OriginalTweet'] = clean_df['OriginalTweet'].str.replace(' +', ' ', regex=True)
    # Remove repeated question marks.
    clean_df['OriginalTweet'] = clean_df['OriginalTweet'].str.replace('\?+', '?', regex=True)
    clean_df['OriginalTweet'] = clean_df['OriginalTweet'].str.replace('(?:\? ?)+', '?', regex=True)
    # Remove URLs.
    clean_df['OriginalTweet'] = clean_df['OriginalTweet'].str.replace('http[^ ]*', ' ', regex=True)
    # Change ampercent sign and the xml entity to "and" word.
    clean_df['OriginalTweet'] = clean_df['OriginalTweet'].str.replace('(&amp;)|&', 'and', regex=True)
    # Change hashtags to normal words (remove the '#').
    #
    if tweet_option == 'remove_hash':
        # '#yolo' -> 'yolo'
        clean_df['OriginalTweet'] = clean_df['OriginalTweet'].str.replace('#', ' ', regex=True)
    elif tweet_option == 'remove_all':
        clean_df['OriginalTweet'] = clean_df['OriginalTweet'].str.replace('#\w+', ' ', regex=True)
    else:
        raise ValueError(f'invalid tweet option: {tweet_option}')
    # Remove reference to twitter Users.
    #
    # Example: '@bbc'
    clean_df['OriginalTweet'] = clean_df['OriginalTweet'].str.replace('@[^ ]+', ' ', regex=True)

    clean_df = clean_df[clean_df['OriginalTweet'].str.contains('\w{3,}')]
    label_dict = {
        'Extremely Negative': 0,
        'Negative': 0,
        'Neutral': 1,
        'Positive': 2,
        'Extremely Positive': 2
    }
    clean_df['SentimentCode'] = clean_df['Sentiment'].replace(label_dict)

    return clean_df



from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

nlp = English()


def featurize_text(text):
    text = nlp(text)
    filtered_text = list()
    for word in text:
        if (word.is_stop == False) and (word.is_punct == False):
            filtered_text.append(word.lemma)
    return filtered_text