import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/save_data', methods=['POST'])
def save_data():
    try:
        # リクエストからJSONデータを取得
        data = request.get_json()
        game_mode = data["game_mode"]
        stage = data["stage"]
        team_tank = data["team_tank"]
        enemy_tank = data["enemy_tank"]
        role = data["role"]
        character = data["character"]
        time_of_day = data["time_of_day"]
        result = data["result"]

        # データベースに接続して保存
        conn = sqlite3.connect('game_data.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO matches (game_mode, stage, team_tank, enemy_tank, role, character, time_of_day, result)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (game_mode, stage, team_tank, enemy_tank, role, character, time_of_day, result))
        conn.commit()
        conn.close()

        # 成功メッセージを返す
        return jsonify({"message": "データが保存されました！"}), 200

    except Exception as e:
        print("エラー内容:", str(e))  # ← ここでエラー内容をログに出す
        return jsonify({"error": "データの保存中にエラーが発生しました。"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
