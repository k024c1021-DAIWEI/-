from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# リクエストログ
リクエストログ = []

# ホームページ
@app.route("/")
def index():
    備品リスト = ["タオル", "スリッパ", "お茶", "コーヒー", "飲料水", "アメニティ"]
    return render_template("index.html", 備品リスト=備品リスト)

# リクエスト受信エンドポイント
@app.route("/submit", methods=["POST"])
def submit_request():
    data = request.json
    社員番号 = data["社員番号"]
    部屋番号 = data["部屋番号"]
    必要備品 = data["必要備品"]

    # リクエストの処理（ログに記録）
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    リクエストログ.append({
        "timestamp": timestamp,
        "社員番号": 社員番号,
        "部屋番号": 部屋番号,
        "必要備品": 必要備品
    })

    # 成功メッセージを返す
    return jsonify({"message": "リクエストが送信されました！"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)