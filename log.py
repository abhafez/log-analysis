# !/usr/bin/env python3

import psycopg2

DBNAME = "news"

question1 = "What are the most popular articles of all time?"
query1 = '''
SELECT title, count(*) as views
FROM articles
JOIN log
ON articles.slug = substring(log.path, 10)
GROUP BY title
ORDER BY views DESC LIMIT 3;
'''
question2 = "Who are the most popular article authors of all time?"
query2 = '''
SELECT authors.name, count(*) as views
FROM articles
JOIN authors
ON articles.author = authors.id
JOIN log
ON articles.slug = substring(log.path, 10)
WHERE log.status LIKE '200 OK'
GROUP BY authors.name ORDER BY views DESC;
'''

def get_queryResults(sql_query):
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(sql_query)
        results = c.fetchall()
        return results
    except psycopg2.DatabaseError:
        print("Something wrong connecting to database")
    finally:
        db.close()


result1 = get_queryResults(query1)
result2 = get_queryResults(query2)


def list_results(result):
    for i in range(len(result)):
        print("\t %s - %s views" % (result[i][0], result[i][1]))


print(question1)
list_results(result1)
print(question2)
list_results(result2)