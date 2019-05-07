#!/usr/bin/env python3

import psycopg2
from datetime import datetime

DBNAME = "news"

question1 = "What are the most popular three articles of all times?"
query1 = '''
SELECT title, count(*) as clicks
FROM articles JOIN log
ON CONCAT('/article/', articles.slug) = log.path
GROUP BY title
ORDER BY clicks DESC LIMIT 3;
'''
question2 = "Who are the most popular authors of all times ?"
query2 = '''
SELECT authors.name AS name, count(*) AS clicks
FROM articles
JOIN authors
ON articles.author = authors.id
JOIN log
ON CONCAT('/article/', articles.slug) = log.path
WHERE log.status = '200 OK'
GROUP BY name ORDER BY clicks DESC;
'''

question3 = "On which days more than 1% of the requests led to error?"
query3 = '''
SELECT * FROM (
SELECT total.day,
round(cast((100*fails.hits) AS numeric) / cast(total.hits AS numeric), 2)
AS error
    FROM (SELECT date(time) AS day, count(*)
    AS hits FROM log GROUP BY day) AS total
    INNER JOIN
    (SELECT date(time) AS day, count(*) AS hits
    FROM log
    WHERE status NOT LIKE '200 OK' GROUP BY day)
        AS fails on total.day = fails.day)
AS t WHERE error > 1.0;
'''


def get_query_results(sql_query):
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


def list_results(result):
    for i in range(len(result)):
        print("\t %s - %s views" % (result[i][0], result[i][1]))


def list_errors(err_resutlts):
    for i in err_resutlts:
        print(
            '\t{0} - {1}% errors'.format
            (datetime.strftime(i[0], '%A, %B %d, %Y'), i[1]))


if __name__ == '__main__':
    # code goes here
    result1 = get_query_results(query1)
    result2 = get_query_results(query2)
    result3 = get_query_results(query3)
    print(question1)
    list_results(result1)
    print("\n")
    print(question2)
    list_results(result2)
    print("\n")
    print(question3)
    list_errors(result3)
    print("\n")
