import MySQLdb

con = MySQLdb.connect(
    host="localhost",
    user="root",
    password="Yuki0307",
    db="順位")
cur = con.cursor()

cur.execute("""
                CREATE TABLE senshu.list
            (id MEDIUMINT NOT NULL AUTO_INCREMENT,
             name VARCHAR(30),
             teamename CHAR(1),
             PRAIMARY KEY(id))
            """)

con.commit()

con.close()