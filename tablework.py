print("Hello, world!, 25 September")

import pandas as pd

file_path = r"C:\Users\babua\PycharmProjects\pythonproject02\practice_tables.xlsx"

tableworks_dfs = pd.read_excel(file_path, sheet_name="Books", header=0, skiprows=0)

#print(tableworks_dfs.head())
sortedbooks = tableworks_dfs.sort_index()
#print(sortedbooks)
sort_books_by_booktitle = tableworks_dfs.sort_values(by='Book_title', ascending=True)
top_ten_sorted = sort_books_by_booktitle.head(10)
#print(top_ten_sorted)
#print(tableworks_dfs.columns)
group_by_genre = tableworks_dfs[tableworks_dfs['Genre'] == 'Politics']
#print(group_by_genre)

grouped = tableworks_dfs.groupby('Genre')
politica_books= grouped.get_group('Politics')
#print(politica_books)

books_by_genre = tableworks_dfs.groupby('Genre')['Book_title'].apply(list)
print(books_by_genre)



