import MySQLdb

con = MySQLdb.connect(
    host="localhost",
    user="root",
    password="Yuki0307",
    db="japan_series"
)
cur = con.cursor()

# 各試合の結果データ
game_results = [
    (1, 8, 0),
    (2, 0, 8),
    (3, 4, 5),
    (4, 4, 3),
    (5, 6, 2),
    (6, 1, 5),
    (7, 8, 0),
]

# プレースホルダーを使用して一括挿入
cur.executemany("""
    INSERT INTO japan_series_list (game_number, hanshin_tigers_score, orix_buffaloes_score)
    VALUES (%s, %s, %s)
""", game_results)

con.commit()

con.close()