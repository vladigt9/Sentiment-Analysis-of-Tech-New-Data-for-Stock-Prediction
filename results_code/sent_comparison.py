import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# read models data
rule = pd.read_csv('rule_based.csv')
roberta = pd.read_csv('roberta.csv')
spacy = pd.read_csv('spacy_scores.csv')

# check total number of scores
rule_scores = rule['scores'].value_counts()
rule_scores = [rule_scores[0], rule_scores[1], rule_scores[2]]

rob_scores = roberta['scores'].value_counts()
rob_scores = [rob_scores[0], rob_scores[1], rob_scores[2]]

spacy_scores = spacy['scores'].value_counts()
spacy_scores = [spacy_scores[0], spacy_scores[1], spacy_scores[2]]

x_values = ['negative', 'neutral', 'positive']

# create df with the values for plotting
data = pd.DataFrame({'X': x_values, 'Rule-Based': rule_scores, 'Roberta': rob_scores, 'Ascent': spacy_scores})

# Melt the DataFrame to long format
data_melted = pd.melt(data, id_vars=['X'], var_name='Model', value_name='Y')

# Create the bar plot using seaborn
sns.barplot(data=data_melted, x='X', y='Y', hue='Model')

# Add title and labels
plt.title('Comparison of Total Sentiment Analysis Scores')
plt.xlabel('Sentiment Label')
plt.ylabel('Number of Articles')

# save plot
plt.savefig('fig.png', dpi=300)
# Show plot
plt.show()