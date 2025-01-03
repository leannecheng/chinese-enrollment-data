# ============================================================================ #
#               Cantonese and Mandarin Enrollment for College Students         #
# ============================================================================ #
# Author: Leanne Cheng
# Description: Filtered data to create usable Chart.js visualizations
# ============================================================================ #

import pandas as pd
import sqlite3
import json

# read the data
df_full = pd.read_csv('Historical-language-enrollments-1958-2021.csv')

# create a dataframe for only Cantonese classes (code #174)
df_canto = df_full[df_full['LANG_CODE'] == 174]

# create a dataframe for Mandarin and Chinese (code #43 and #506)
df_mandarin = df_full[(df_full['LANG_CODE'] == 43) | (df_full['LANG_CODE'] == 506)]

# drop rows with NaN in column ALL LEVEL TOTAL
df_canto = df_canto.dropna(subset='ALL LEVEL TOTAL')
df_mandarin = df_mandarin.dropna(subset='ALL LEVEL TOTAL')

# keep only the necessary columns (Cantonese)
df_canto = df_canto[['SRVY_YEAR', 'ALL LEVEL TOTAL', 'GEOGRAPHY_CODE', 'INST_ID']]
df_canto['SRVY_YEAR'] = df_canto['SRVY_YEAR'].fillna(0).astype(int)
df_canto['ALL LEVEL TOTAL'] = df_canto['ALL LEVEL TOTAL'].fillna(0).astype(int)
df_canto['GEOGRAPHY_CODE'] = df_canto['GEOGRAPHY_CODE'].fillna(0).astype(int)
df_canto['INST_ID'] = df_canto['INST_ID'].fillna(0).astype(int)

df_canto.rename(columns={'ALL LEVEL TOTAL' : 'ENROLLMENT_TOTAL'}, inplace=True)

# keep only the necessary columns (Mandarin)
df_mandarin = df_mandarin[['SRVY_YEAR', 'ALL LEVEL TOTAL', 'GEOGRAPHY_CODE', 'INST_ID']]
df_mandarin['SRVY_YEAR'] = df_mandarin['SRVY_YEAR'].fillna(0).astype(int)
df_mandarin['ALL LEVEL TOTAL'] = df_mandarin['ALL LEVEL TOTAL'].fillna(0).astype(int)
df_mandarin['GEOGRAPHY_CODE'] = df_mandarin['GEOGRAPHY_CODE'].fillna(0).astype(int)
df_mandarin['INST_ID'] = df_mandarin['INST_ID'].fillna(0).astype(int)

df_mandarin.rename(columns={'ALL LEVEL TOTAL' : 'ENROLLMENT_TOTAL'}, inplace=True)

# ---------------------- Cantonese Database ------------------------------ #

conn = sqlite3.connect('cantonese.db')
c = conn.cursor()

# ----- One-time SQL commands, uncomment to use ----- #
'''
# c.execute("DROP TABLE cantonese")
# df_canto.to_sql('cantonese', conn, if_exists='replace', index=False)
# c.execute("PRAGMA table_info(cantonese)")

c.execute("""SELECT SRVY_YEAR, SUM(ENROLLMENT_TOTAL) AS total_enrollment_by_year FROM cantonese 
         GROUP BY SRVY_YEAR""")
'''

# ----- One-time Python to JSON file commands, uncomment to use ----- #
'''
# convert into a dictionary
canto_enroll_tuples = c.fetchall()
canto_enroll_dict = {row[0]: row[1] for row in canto_enroll_tuples}
print(canto_enroll_dict)

with open('cantonese_enrollment.json', 'w') as json_file:
    json.dump(canto_enroll_dict, json_file, indent=4)
'''
conn.commit()
conn.close()

# ------------------------- Mandarin Database ------------------------------ #

conn2 = sqlite3.connect('mandarin.db')
c2 = conn2.cursor()

# ----- One-time SQL commands, uncomment to use ----- #
'''
#df_mandarin.to_sql('mandarin', conn2, if_exists='replace', index=False)
#c2.execute("PRAGMA table_info(mandarin)")
c2.execute("""SELECT SRVY_YEAR, SUM(ENROLLMENT_TOTAL) AS total_enrollment_by_year FROM mandarin 
         GROUP BY SRVY_YEAR""")
'''

# ----- One-time Python to JSON file commands, uncomment to use ----- #
'''
mandarin_enroll_tuples = c2.fetchall()
# convert to a dictionary
mandarin_enroll_dict = {row[0]: row[1] for row in mandarin_enroll_tuples}
with open('mandarin_enrollment.json', 'w') as json_file:
    json.dump(mandarin_enroll_dict, json_file, indent=4)
'''

conn2.commit()
conn2.close()


