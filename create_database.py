import sqlite3

# データベース名
DATABASE = 'game_data.db'

# データベース作成とテーブル作成
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# テーブル作成クエリ
create_table_query = """
CREATE TABLE IF NOT EXISTS game_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_mode TEXT NOT NULL,
    stage TEXT NOT NULL,
    team_tank TEXT NOT NULL,
    enemy_tank TEXT NOT NULL,
    role TEXT NOT NULL,
    character TEXT NOT NULL,
    time_of_day TEXT NOT NULL,
    result TEXT NOT NULL
);
"""
cursor.execute(create_table_query)

# 保存して接続を閉じる
conn.commit()
conn.close()

print("データベースを作成しました！")

