import MySQLdb

con = MySQLdb.connect(
    host="localhost",
    user="root",
    password="Yuki0307",
    db="account"
)
cur = con.cursor()

cur.execute("""
    CREATE TABLE a_list
    (
        id MEDIUMINT NOT NULL AUTO_INCREMENT,
        name VARCHAR(30),
        text VARCHAR(30),
        email VARCHAR(30),
        password VARCHAR(30),
        PRIMARY KEY(id)
    )
""")
con.commit()

con.close()