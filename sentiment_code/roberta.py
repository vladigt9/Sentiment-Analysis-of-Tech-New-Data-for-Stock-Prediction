from happytransformer import HappyTextClassification
import pandas as pd

# load articles
data = pd.read_csv('news_data/guardian_data.csv')

# create a function which splits the articles at each 10th dot
def split_on_every_nth_dot(s, n=10):
    parts = []
    current_part = []
    dot_count = 0
    
    for char in s:
        current_part.append(char)
        if char == '.':
            dot_count += 1
            if dot_count == n:
                parts.append(''.join(current_part))
                current_part = []
                dot_count = 0

    # Add the last part if any
    if current_part:
        parts.append(''.join(current_part))

    return parts

# load the distilroberta model
happ = HappyTextClassification(model_type='DISTILROBERTA', model_name='mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis', num_labels=3)

# create dictionary to store data
scores = {'scores': []}

# go over all articles
for i in range(len(data['article'])):
    
    # for the specific two articles 10th dot still creates too big articles so are adjusted to 8
    if i == 183 or i == 195:
        split_article = split_on_every_nth_dot(data['article'].iloc[i], 8)
    else:
        split_article = split_on_every_nth_dot(data['article'].iloc[i])
        
    # create temporary variables to store scores
    final_score = 0
    pos_scores = []
    neg_scores = []
    neu_scores = []
    
    # for each split part of the artciles check the results and add to the data
    for part in split_article:
        result = happ.classify_text(part)
        if happ.classify_text(part).label == 'positive':
            pos_scores.append(happ.classify_text(part).score)
        elif happ.classify_text(part).label == 'negative':
            neg_scores.append(happ.classify_text(part).score)
        elif happ.classify_text(part).label == 'neutral':
            neu_scores.append(happ.classify_text(part).score)
    
    
    # get the summ of all, positive, negative and neutral scores
    pos_fin = sum(pos_scores)
    neg_fin = sum(neg_scores)
    neu_fin = sum(neu_scores)
    
    # subtract positive from negative
    med = pos_fin - neg_fin

    # check value of med, if positive subtract the neutral score, if negative add the neutral
    if med > 0:
        f = med - neu_fin/2
        
        # if the new score is positive then article is given positive label
        # else neutral
        if f < 0:
            final_score = 1
        else:
            final_score = 2
    elif med<0:
        f = med + neu_fin/2
        
        # if the new score is negative then article is given negative label
        # else neutral
        if f > 0:
            final_score = 1
        else:
            final_score = 0
    else:
        final_score = 1  
    
    # add final scores
    scores['scores'].append(final_score)

# create df and then save it
df = pd.DataFrame(scores)

df.to_csv('roberta.csv', index=False)
