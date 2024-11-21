from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# データベース接続
def connect_db():
    conn = sqlite3.connect('game_data.db')
    return conn

# 保存完了画面のHTML
SUCCESS_HTML = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>保存完了</title>
    <style>
        body {
            margin: 0;
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to bottom right, #FFCC00, #0099FF, #FF66CC);
            color: #fff;
            text-align: center;
            padding-top: 20%;
        }

        h1 {
            font-size: 28px;
            margin-bottom: 10px;
        }

        p {
            font-size: 20px;
            margin-bottom: 30px;
        }

        a {
            text-decoration: none;
            color: #fff;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 5px;
            background: linear-gradient(to right, #FF6600, #FF0033);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            transition: background 0.3s ease, transform 0.2s ease;
        }

        a:hover {
            background: linear-gradient(to right, #FF0033, #FF6600);
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <h1>データが保存されました！</h1>
    <p>入力ありがとうございました。</p>
    <a href="/">もう一度データを入力する</a>
</body>
</html>
"""

# データ保存エンドポイント
@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.form
    print("受け取ったデータ:", data)  # デバッグ用

    try:
        # データベースに接続
        conn = connect_db()
        cursor = conn.cursor()

        # データを保存
        query = """
        INSERT INTO matches (game_mode, stage, team_tank, enemy_tank, role, character, time_of_day, result)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        values = (
            data['game_mode'],
            data['stage'],
            data['team_tank'],
            data['enemy_tank'],
            data['role'],
            data['character'],
            data['time_of_day'],
            data['result']
        )
        cursor.execute(query, values)
        conn.commit()
        conn.close()

        # 保存成功時にカラフルな画面を返す
        return render_template_string(SUCCESS_HTML), 200
    except Exception as e:
        print("エラー:", str(e))  # デバッグ用
        return "データの保存中にエラーが発生しました。", 500

if __name__ == '__main__':
    app.run(debug=True)


