def clean_dataframe(df):

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
    # '#yolo' -> 'yolo'
    clean_df['OriginalTweet'] = clean_df['OriginalTweet'].str.replace('#', ' ', regex=True)
    # Remove reference to twitter Users.
    #
    # Example: '@bbc'
    clean_df['OriginalTweet'] = clean_df['OriginalTweet'].str.replace('@[^ ]+', ' ', regex=True)

    clean_df = clean_df[clean_df['OriginalTweet'].str.contains('\w{3,}')]

    return clean_df