# Sentiment Analysis of Tech News Data for Stock Prediction

This project explores the relationship between news sentiment and stock price movements in the tech sector. Using a combination of sentiment analysis techniques and financial data, it investigates the predictive power of media sentiment on stock performance.

## Project Goals

- **Analyze News Sentiment**: Utilize dictionary-based methods, machine learning models (e.g., RoBERTa, Ascent, SpaCy), and APIs to extract and assess sentiment from tech-related news articles.
- **Correlate with Stock Prices**: Align sentiment data with historical stock prices to identify potential patterns and predictive relationships.
- **Compare Model Performance**: Evaluate and benchmark different sentiment analysis methods to determine the most effective approach.

## Key Features

### 1. News Data Acquisition
- Data sourced from The Guardian API, providing comprehensive and up-to-date news coverage.
- Preprocessing to clean and structure the data for sentiment analysis.

### 2. Sentiment Analysis
- Implementation of various sentiment analysis models:
  - **Dictionary-Based Methods**: Establishing baseline analyses.
  - **Machine Learning Models**: Advanced sentiment scoring using RoBERTa, Ascent, and SpaCy.
- Comparative analysis of model performances on metrics such as precision, recall, and contextual relevance.

### 3. Data Alignment
- Integration of sentiment data with stock price fluctuations to identify trends and potential causative factors.

### 4. Insights
- Quantitative analysis of the impact of positive and negative sentiment on stock trends.
- Research on correlations and patterns to refine investment decision-making tools.

## Tools and Technologies

- **Languages**: Python (primary), Pandas for data manipulation.
- **APIs**: The Guardian API for news data extraction.
- **NLP Frameworks**: SpaCy, RoBERTa, and Ascent for sentiment analysis.
- **Visualization Tools**: Matplotlib and Seaborn for graphical representation of results.

## Results and Findings

- Preliminary results show little correlation between the stocks' values and the sentiment scores.
- The models' results are vastly different with no two models agreeing more than 50% of the time.
  
## Future Directions

- Incorporating robust models like BERT-based transformers fine-tuned for financial contexts.
- Expanding the dataset to include a broader range of industries for increased generalizability.
- Deployment of the project as a web-based dashboard or application for real-time stock sentiment predictions.

---
