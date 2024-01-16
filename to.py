import MySQLdb

con = MySQLdb.connect(
    host="localhost",
    user="root",
    password="Yuki0307",
    db="japan_series"
)
cur = con.cursor()

cur.execute("""
    CREATE TABLE japan_series_list
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        game_number INT,
        hanshin_tigers_score INT,
        orix_buffaloes_score INT
    )
""")