import string
import re
from sklearn.datasets import fetch_20newsgroups

bunch = newsgroups_train = fetch_20newsgroups(subset='all')

re_punctuation = re.compile('[%s]' % re.escape(string.punctuation))
re_start = re.compile('[a-zA-Z]*: ')

result = []
for row in bunch.data:
    lines = row.split('\n')
    data = []

    for line in lines:
        if re_start.match(line):
            continue
        data.append(line)

    row = '\n'.join(data)
    row = re_punctuation.sub('', row)
    row = row.replace('\n', ' ').lower()
    result.append(row)


with open('./data/data.txt', 'w', encoding='utf8') as f:
    f.writelines(result)
