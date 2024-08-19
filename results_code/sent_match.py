import pandas as pd

# load data from models
rule = pd.read_csv('rule_based.csv')
roberta = pd.read_csv('roberta.csv')
spacy = pd.read_csv('spacy_scores.csv')

# create dummy variables
rul_rob = 0
rul_spac = 0
spac_rob = 0
alls = 0

for i in range(len(rule)):
    # check when models intercept and add one to the corresponding dummy variable
    if rule['scores'].iloc[i] == roberta['scores'].iloc[i]:
        rul_rob += 1
    if rule['scores'].iloc[i] == spacy['scores'].iloc[i]:
        rul_spac += 1
    if spacy['scores'].iloc[i] == roberta['scores'].iloc[i]:
        spac_rob += 1
    if spacy['scores'].iloc[i] == roberta['scores'].iloc[i] and rule['scores'].iloc[i] == roberta['scores'].iloc[i]:
        alls += 1
        
# print results
print(rul_rob, rul_spac, spac_rob, alls)
print(rul_rob / len(rule), rul_spac/ len(rule), spac_rob/ len(rule), alls/ len(rule))