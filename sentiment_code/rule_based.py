import pandas as pd

# read guardian data
data = pd.read_csv('news_data/guardian_data.csv')
# read lexicon data
lexicon = pd.read_csv('lexicon_data/lexicon.csv')
#get all words to lower case
lexicon = lexicon.apply(lambda x: x.map(lambda y: y.lower() if isinstance(y, str) else y))
contractions = pd.read_csv('lexicon_data/contractions.csv')

# create a function which would replace all contractions insde the articles
def replace_contractions(text):
    contractions_dict = contractions.set_index('contractions')['full_forms'].to_dict()
    for contraction, full_form in contractions_dict.items():
        text = text.replace(contraction, full_form)
    return text

# create temporary dict to store tokenized data
tokenized_data = {
    'date': [],
    'artlicles': []
}

# tokenize the data
for i in range(len(data)):
    date = data['date'].iloc[i]
    article = data['article'].iloc[i]
    
    # replace contractions
    article = replace_contractions(article)
    
    # add data
    tokenized_data['date'].append(date)
    tokenized_data['artlicles'].append(article.split())

sentiments = []

# get sentiment
for k, article in enumerate(tokenized_data['artlicles']):
    
    # set values for keeping coutn of words
    pozitives = 0
    negatives = 0
    
    # loop over all words and check
    for word in article:
        # check how many of the pozitive and negative words are in the article
        # make all words to lower case to match with lexicon
        if lexicon['positive'].isin([word.lower()]).any():
            pozitives += 1
        elif lexicon['negative'].isin([word.lower()]).any():
            negatives += 1

    sentiments.append([pozitives, negatives])

# store final scores
final_sentiments = {
    'score': []
}

for i in range(len(sentiments)):
    # subtract positive from negative
    p_n = sentiments[i][0] - sentiments[i][1]
    
    # if p_n above when then add postive label, if below -1 negative, else neutral
    if p_n > 1:
        final_sentiments['score'].append(2)
    elif p_n < -1:
        final_sentiments['score'].append(0)
    else:
        final_sentiments['score'].append(1)
        
# save data to csv
df = pd.DataFrame(final_sentiments)
df.to_csv('rule_based.csv', index=False)

