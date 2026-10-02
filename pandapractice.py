print("Hello, world! 23 September")
import pandas as pd

file_path = r"C:\Users\babua\PycharmProjects\pythonproject02\practice_tables.xlsx"

# Load all sheets at once
dfs = pd.read_excel(file_path, sheet_name=None)

movies_domestic = dfs['Movies'].sort_values(by='Domestic', ascending=False)
#print(movies_domestic)

movies_foreign = dfs['Movies'].sort_values(by='Foreign', ascending=False)
#print(movies_foreign.head())


movies = dfs['Movies']
high_domestic = movies[movies['Domestic']>300_000_000] 
#print(high_domestic)
block_busters = movies[movies['worldwide']>1000000000]
#print(block_busters)
top = movies[movies['Rank']<=5]
#print(top)

filtered = movies[movies['Foreign'] > 500_000_000]
result = filtered.sort_values(by='Foreign', ascending=False)
#print(result)
filtered = movies[movies['worldwide']>900000000]
sorted_filtered = filtered.sort_values(by='worldwide', ascending=False)
#print(sorted_filtered)

result = movies[
    (movies['Domestic'] > 300_000_000) &
    (movies['Foreign'] > 500_000_000)
].sort_values(by='worldwide', ascending=False)

#print(result)
result2=movies[
    (movies['Domestic']>300_000_000) &
    (movies['worldwide']>500_000_000)          
].sort_values(by='Domestic', ascending=False)
#print(result2)

result = movies[movies['Movie_name'].str.contains("World")] \
             .sort_values(by='Foreign', ascending=False)

#print(result)
result = movies[movies['Domestic'] < 200_000_000] \
             .sort_values(by='Foreign', ascending=False) \
             .head(5)

#print(result)

athletes = dfs['Athletes']
#print(athletes.keys())
#print(athletes.head())

group_by_sport = athletes.groupby('sport')['Endorsement'].sum()
result3 = group_by_sport[group_by_sport > 100] \
              .sort_values(ascending=False)
#print(result3)

avg_salary = athletes.groupby('sport')['Salary and winnings'].mean()

sorted_avg_salary = avg_salary.sort_values(ascending=False)

print(sorted_avg_salary)








