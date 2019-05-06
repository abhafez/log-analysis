# !/usr/bin/env python

import psycopg2

DBNAME = "news"

question1 = "What are the most popular articles of all time?"
query1 = '''
SELECT title, count(*) as views
FROM articles
JOIN log
On articles.slug = substring(log.path, 10)
GROUP BY title
ORDER BY views DESC LIMIT 3;
'''

def get_queryResults(sql_query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results

result1 = get_queryResults(query1)

print(question1)
print(result1)