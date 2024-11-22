from flask import Flask, request, jsonify, render_template_string
import sqlite3

app = Flask(__name__)

# データベースパス
DATABASE = "game_data.db"

# 成功メッセージをHTMLで作成
SUCCESS_HTML = """
<!DOCTYPE html>
<html lang="en">
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
        # フォームから送信されたデータを取得
        data = request.form
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

        # データを挿入
        cursor.execute("""
            INSERT INTO matches (game_mode, stage, team_tank, enemy_tank, role, character, time_of_day, result)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (game_mode, stage, team_tank, enemy_tank, role, character, time_of_day, result))

        # 変更を保存して接続を閉じる
        conn.commit()
        conn.close()

        # 成功時のメッセージを返す
        return render_template_string(SUCCESS_HTML), 200

    except Exception as e:
        print("エラー:", str(e))  # デバッグ用
        return "データの保存中にエラーが発生しました。", 500

# アプリケーションのエントリーポイント
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

