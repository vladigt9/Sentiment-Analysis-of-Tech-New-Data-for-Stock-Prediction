### Explanations of Files and Folders:

- **`data_code/`** folder contains 2 files:
  - One of them is to extract the data from the Guardian API.
  - The other is to extract the data from Yahoo Finance (yfinance).

- **`index_data/`** folder contains all the data from Yahoo Finance in CSV format.

- **`lexicon_data/`** folder contains all the data for the simple rule-based approach used in the report.

- **`news_data/`** folder contains a single CSV file storing the data from the Guardian API.

- **`performance_data/`** folder contains the data of the performance of the stocks.

- **`results_code/`** folder:
  - `performance.py` - The stock performance after publication of an article is analyzed and saved.
  - `sent_comparison.py` - The bar chart showing total number of labels for each model is generated.
  - `sent_match.py` - Investigates the amount of times labels match.
  - `sentiment_perf.py` - Finds the number of times model labels match with stock labels.

- **`sentiment_code/`** folder contains three files, one for each model. Each file explains in detail how the models work.

- **Model Data Files**:
  - `roberta.csv`, `rule_based.csv`, `spacy_scores.csv` store the data of the models.

- **`fig.png`** - The bar chart generated from the code.
