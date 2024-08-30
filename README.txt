

Explanations of files and folders:

data_code folder contains 2 files. One of them is to extract the data from the guardian api, while the
other is to extract the data from yfinance

index_data folder contains all the data from yahoo finance in csv format

lexicon_data folder contains all the data for the simple rule-based approach used in the report

news_data folder contains a single csv file storing the data from the guardian api

performance_data folder contains the data of the performance of the stocks

results_code folder
    performance.py - the stock performance after publication of an article is analysed and saved

    sent_comparison.py - the barchart showing total number of labels for each model is generated

    sent_match.py - the amount of times labels match is investigated

    sentiment_perf.py - finds the number of times model labels match with stock labels

sentiment_code folder contains three files. One for each model. Each files explains in details how the models work.

roberta.csv, rule_based.csv, spacy_scores.csv store the data of the models

fig.png is the barchart generate from the code