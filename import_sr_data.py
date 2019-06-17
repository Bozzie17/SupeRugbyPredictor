# Import SupeRugby data from https://www.flashscore.com.au/rugby/world/super-rugby/
# Add info for predictor

# TODO find a free api to pull SR data

import pandas

df = pandas.read_csv('data.csv', index_col='Season')
winners = []
diffs = []
for index, row in df.iterrows():
    scores = row['Result'].split(':')
    diff = int(scores[0]) - int(scores[1])
    diffs.append(diff)
    if diff > 0:
        winners.append(row['Home Team'])
    elif diff == 0:
        winners.append("-")
    else:
        winners.append(row['Away Team'])
df['Winner'] = winners
df['Diff'] = diffs
df.to_csv('data_modified.csv')
