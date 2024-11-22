from flask import Flask, request, jsonify
import sqlite3
import traceback

app = Flask(__name__)

# データベースのパス
DATABASE = 'game_data.db'

# 成功時のHTMLメッセージ
SUCCESS_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Success</title>
</head>
<body style="background-color: #e0f7fa; text-align: center;">
    <h1>データが正常に保存されました！</h1>
</body>
</html>
"""

@app.route('/save_data', methods=['POST'])
def save_data():
    try:
        # JSONデータの取得
        data = request.get_json()
        game_mode = data['game_mode']
        stage = data['stage']
        team_tank = data['team_tank']
        enemy_tank = data['enemy_tank']
        role = data['role']
        character = data['character']
        time_of_day = data['time_of_day']
        result = data['result']

        # データベースに接続
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # データ挿入のSQL
        insert_query = """
        INSERT INTO game_data (game_mode, stage, team_tank, enemy_tank, role, character, time_of_day, result)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (game_mode, stage, team_tank, enemy_tank, role, character, time_of_day, result))

        # 変更を保存して接続を閉じる
        conn.commit()
        conn.close()

        return SUCCESS_HTML, 200
    except Exception as e:
        print("エラー:", str(e))
        traceback.print_exc()
        return "データの保存中にエラーが発生しました。", 500

# アプリケーションのエントリーポイント
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


