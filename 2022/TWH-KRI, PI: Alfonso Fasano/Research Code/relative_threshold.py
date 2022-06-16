import json

import pandas as pd

# 3815, 3108, 4034
# open JSON file (redacted)
r = open('Report_Json_Session_Report_20220607T123108[1].json')

# can't straight-up read JSON object to a DataFrame due to ValueError: All arrays must be of same length
# df = pd.read_json('redacted')

# to combat this we convert the JSON object to a dictionary before converting it to a DataFrame, giving us control
d = json.load(r)

# converting the dictionary to a DataFrame using the indices we need
df = pd.DataFrame(d['DiagnosticData']['LFPTrendLogs'])

# get information on df
# df.info()

# initiate sum
sum = 0

# traverse through DataFrame
# iterate through non-null counts of column sensing_channel and print information
for i in range(0, int(df.count())):
    current = str(df.iloc[i][0][i]).split(' ')
    # local field potential (LFP)
    local_field_potential = int(current[3].split(',')[0])

    # add LFP to sum
    sum += local_field_potential

relative_threshold = sum/int(df.count())

# print relative_threshold
print("Relative threshold: " + str(relative_threshold))
