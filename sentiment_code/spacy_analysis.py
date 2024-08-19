import spacy
import asent
import pandas as pd

# read artcle data
data = pd.read_csv('news_data/guardian_data.csv')

# load spacy pipeline
nlp = spacy.blank('en')
nlp.add_pipe('sentencizer')

# add the rule-based sentiment model
nlp.add_pipe('asent_en_v1')

# create dict to store final scores
f_scores = {'scores': []}

for i in range(len(data)):
    # perform analysis on article
    doc = nlp(data['article'].iloc[i])

    # check scores
    positive = doc._.polarity.positive
    negative = doc._.polarity.negative
    neutral = doc._.polarity.neutral
    values = [negative, neutral, positive]
    
    # find best score
    max_index = values.index(max(values))
    
    # check if max index is 0 or 2, which stand for negative and positive labels
    if max_index == 0:
        f_scores['scores'].append('0')
    # check if index is one meaning neutral score. If that is the case then check if the score is above
    # 66% or else assign the second highest label
    elif max_index == 1:
        if  max(values) < 0.66:
            sorted_list = sorted(values, reverse=True)
            second_highest_index = values.index(sorted_list[1])
            if second_highest_index == 0:
                f_scores['scores'].append('0')
            else:
                f_scores['scores'].append('2')
        else:
            f_scores['scores'].append('1')
    elif max_index == 2:
        f_scores['scores'].append('2')
        
# save all data to csv
df = pd.DataFrame(f_scores)
df.to_csv('spacy_scores.csv', index=False)
    
    