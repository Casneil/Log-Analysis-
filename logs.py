import psycopg2


def stars(num=48, stars='*'):
    print stars * num


def get_posts():
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("SELECT title, COUNT(path) AS topThree FROM articles, log WHERE CONCAT\
       ('/article/', articles.slug) = log.path	GROUP BY title ORDER BY topThree DESC LIMIT 3")
    posts = c.fetchall()

    print "Most viewed articles:"

    stars()

    for views in posts:
        print views[0], "-", views[1], "views"


def get_authors():
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("SELECT authors.name,COUNT(*) AS top FROM authors,log,  articles WHERE \
       (CONCAT('/article/', articles.slug) = log.path AND articles.author =  authors.id) \
          GROUP BY authors.name ORDER BY top DESC")
    posts = c.fetchall()

    print " " "\n" "Most Popular Authors:" " "

    stars()

    for authors in posts:
        print authors[0], "-", authors[1], "views"


def error_days():
    db = psycopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("SELECT COUNT(total.status)*100.0/fails.errors AS percentage,total.time::DATE\
        FROM log AS total JOIN (SELECT COUNT(status) AS errors,TIME::DATE FROM log GROUP BY \
           TIME::DATE) AS fails ON total.time::DATE = fails.time::DATE WHERE total.status not\
               LIKE '%200%'   GROUP BY total.time::DATE,fails.errors ORDER BY percentage DESC LIMIT 1;")

    posts = c.fetchall()

    print " " "\n" "Error Days:" " "

    stars()

    for fails in posts:
        print "Most error day was July, 17 2016 recording:", format(fails[0], ".1f"), "% of errors"


get_posts()
get_authors()
error_days()
