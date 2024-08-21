import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('dash_visits.csv', index_col='record_id')
print(data.head(3))
group = data.groupby('source_topic').agg({'visits': ['sum', 'count', 'mean']})
print(group)
data['source_topic'].value_counts().plot(kind='bar', ylabel='visits')
plt.show()
