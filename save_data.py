from flask import Flask, request, jsonify, render_template_string
import sqlite3

app = Flask(__name__)

# データベースパス
DATABASE = "game_data.db"

# 成功メッセージ
SUCCESS_HTML = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
    <style>
        body {
            background-color: #f0f8ff;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        h1 {
            color: #4682b4;
        }
    </style>
</head>
<body>
    <h1>データが保存されました！</h1>
</body>
</html>
"""

@app.route('/save_data', methods=['POST'])
def save_data():
    try:
        # フォームデータ取得
        data = request.form
        game_mode = data.get('game_mode')
        stage = data.get('stage')
        team_tank = data.get('team_tank')
        enemy_tank = data.get('enemy_tank')
        role = data.get('role')
        character = data.get('character')
        time_of_day = data.get('time_of_day')
        result = data.get('result')

        # データベース接続
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # テーブルに挿入
        cursor.execute("""
            INSERT INTO matches (game_mode, stage, team_tank, enemy_tank, role, character, time_of_day, result)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (game_mode, stage, team_tank, enemy_tank, role, character, time_of_day, result))

        # 保存
        conn.commit()
        conn.close()

        # 成功レスポンス
        return render_template_string(SUCCESS_HTML), 200

    except Exception as e:
        print(f"エラー: {str(e)}")  # エラー出力
        return "データの保存中にエラーが発生しました。", 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
