import MySQLdb

con = MySQLdb.connect(
    host='localhost',
    user='root',
    password='Yuki0307',
    db='順位')
cur = con.cursor()
cur.execute("""
            CREATE TABLE 順位.list
    (id MEDIUMINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30),
    sex CHAR(1),
    PRIMARY KEY (id))
            """)

con.commit()

con.close()