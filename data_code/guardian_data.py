import requests
import pandas as pd

# create temporary data stach dict
dic = {
    'date': [],
    'article': []
}

# run through all first 9 months, making sure to keep with the amount of days
for m in range(1, 10):
    if m == 2:
        for i in range(2, 29):
            # create request based on the month
            if i < 10:
                url = f'https://content.guardianapis.com/search?page-size=100&from-date=2023-0{m}-0{i-1}&to-date=2023-0{m}-0{i}&section=technology&show-fields=bodyText&api-key=XXX'
            if i == 10:
                url = f'https://content.guardianapis.com/search?page-size=100&from-date=2023-0{m}-0{i-1}&to-date=2023-0{m}-{i}&section=technology&show-fields=bodyText&api-key=XXX'
            else:
                url = f'https://content.guardianapis.com/search?page-size=100&from-date=2023-0{m}-{i-1}&to-date=2023-0{m}-{i}&section=technology&show-fields=bodyText&api-key=XXX'
            
            # get response from api
            response = requests.get(url)
            
            # select only the date and article
            for k in range(len(response.json()['response']['results'])):
                dic['date'].append(response.json()['response']['results'][k]['webPublicationDate'])
                dic['article'].append(response.json()['response']['results'][k]['fields']['bodyText'])
    
    # do same based on months
    elif m%2 == 0 or m==9:
        for i in range(2, 31):
            if i < 10:
                url = f'https://content.guardianapis.com/search?page-size=100&from-date=2023-0{m}-0{i-1}&to-date=2023-0{m}-0{i}&section=technology&show-fields=bodyText&api-key=XXX'
            if i == 10:
                url = f'https://content.guardianapis.com/search?page-size=100&from-date=2023-0{m}-0{i-1}&to-date=2023-0{m}-{i}&section=technology&show-fields=bodyText&api-key=XXX'
            else:
                url = f'https://content.guardianapis.com/search?page-size=100&from-date=2023-0{m}-{i-1}&to-date=2023-0{m}-{i}&section=technology&show-fields=bodyText&api-key=XXX'
            
            response = requests.get(url)
            for k in range(len(response.json()['response']['results'])):
                dic['date'].append(response.json()['response']['results'][k]['webPublicationDate'])
                dic['article'].append(response.json()['response']['results'][k]['fields']['bodyText'])
                
    else:
        for i in range(2, 32):
            if i < 10:
                url = f'https://content.guardianapis.com/search?page-size=100&from-date=2023-0{m}-0{i-1}&to-date=2023-0{m}-0{i}&section=technology&show-fields=bodyText&api-key=XXX'
            if i == 10:
                url = f'https://content.guardianapis.com/search?page-size=100&from-date=2023-0{m}-0{i-1}&to-date=2023-0{m}-{i}&section=technology&show-fields=bodyText&api-key=XXX'
            else:
                url = f'https://content.guardianapis.com/search?page-size=100&from-date=2023-0{m}-{i-1}&to-date=2023-0{m}-{i}&section=technology&show-fields=bodyText&api-key=XXX'
    
        response = requests.get(url)
        for k in range(len(response.json()['response']['results'])):
            dic['date'].append(response.json()['response']['results'][k]['webPublicationDate'])
            dic['article'].append(response.json()['response']['results'][k]['fields']['bodyText'])

     
# create df with the data   
df = pd.DataFrame(dic)

# find only articles for the following companies
words_to_find = ['Apple', 'Microsoft', 'Meta', 'Alphabet', 'Google']

# create regex for them
pattern = '|'.join(words_to_find)
regex_pattern = fr'(?i){pattern}'

# Filter articles
df = df[df['article'].str.contains(regex_pattern)]

# save data
df.to_csv('news_data/guardian_data.csv', index=False)
