# Explanations of Files and Folders

### `data_code/` folder
- Contains 2 files:
  - One for extracting data from the Guardian API.
  - One for extracting data from Yahoo Finance (yfinance).

### `index_data/` folder
- Contains all the data from Yahoo Finance in CSV format.

### `lexicon_data/` folder
- Contains all the data for the simple rule-based approach used in the report.

### `news_data/` folder
- Contains a single CSV file storing data from the Guardian API.

### `performance_data/` folder
- Contains data related to the performance of the stocks.

### `results_code/` folder
- Contains the following Python files:
  - `performance.py`: Analyzes and saves the stock performance after the publication of an article.
  - `sent_comparison.py`: Generates a bar chart showing the total number of labels for each model.
  - `sent_match.py`: Investigates how many times labels match.
  - `sentiment_perf.py`: Finds the number of times model labels match with stock labels.

### `sentiment_code/` folder
- Contains three files, one for each model, explaining in detail how the models work.

### Model Data Files
- `roberta.csv`, `rule_based.csv`, `spacy_scores.csv`: Store data for the models.

### `fig.png`
- A bar chart generated from the code.
