# Chinese Enrollment Data Cleaning
This project showcases my data cleaning process for Chinese enrollment visualizations. 

**Link to project:** https://leannecheng.github.io/chinese-enrollment-tracker


<img width="950" alt="Screenshot 2025-01-04 105753" src="https://github.com/user-attachments/assets/ed79e02c-2684-4511-897e-d3a0021c4ebc" />

## How It's Made:

**Tech used:** Python, SQL, JSON

I downloaded the CSV file from the Modern Language Association's Language Enrollment Database and used the Pandas library to clean the data. Next, I utilized SQLite to create my own local database for Mandarin and Cantonese Enrollment and ran aggregate queries for later conversion into JSON files. The final JSON files contained the data required for Chart.js visualizations.

## Lessons Learned:

I wanted to explore all the languages I had been curious about, and I discovered the best way to figure out when to use certain tools is to figure out when *not* to use these tools. For example, I realized after I created the SQL databases that using Pandas on a static file would have been easier. 
