import pandas as pd

# load stock performance data
meta_pf = pd.read_csv('performance_data/pf_meta.csv')
apple_pf = pd.read_csv('performance_data/pf_apple.csv')
goog_pf = pd.read_csv('performance_data/pf_goog.csv')
msft_pf = pd.read_csv('performance_data/pf_msft.csv')
pfs = [meta_pf, apple_pf, goog_pf, msft_pf]

# load articles and models
articles = pd.read_csv('news_data/guardian_data.csv')
roberta = pd.read_csv('roberta.csv')
rul = pd.read_csv('rule_based.csv')
spacy = pd.read_csv('spacy_scores.csv')
models = [rul, spacy, roberta]

# create dummy lists
final = []
percs = []

# loop over performance data
for i in range(len(pfs)):
    # create more dummy variables to store data
    mat = []
    perc = []
    
    # loop over models
    for k in range(len(models)):
        # filter appropriate articles
        filtered = models[k][models[k].index.isin(pfs[i]['index'])]

        # find number of matches
        matches = 0
        for l in range(len(filtered)):
            if filtered['scores'].iloc[l] == pfs[i]['price_changes'].iloc[l]:
                matches += 1
        
        # add data to dummy variables
        mat.append([matches, len(filtered)])
        perc.append(matches/len(filtered))

    final.append(mat)
    percs.append(perc)

# print results
print(final)
print(percs)