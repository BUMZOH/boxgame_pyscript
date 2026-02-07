import random
from js import setTimeout, document

# 定数の宣言
GAME_TURNS = 30
INTERVAL = 1000 # unit=ms
WIDTH = 50      # モグラサイズ

# info要素の取得
info = document.getElementById("info")
# Canvasの取得
canvas = document.getElementById("canvas")
context = canvas.getContext("2d")

# ゲーム全体の流れを辞書型変数で管理
game = {
    "turns": GAME_TURNS,
    "score": 0,
    "mx": 0,    # モグラx座標
    "my": 0,    # モグラy座標
    "hide": True,   # モグラが隠れているか
}

def next_turn():
    """次のターンの処理を行う関数"""
    if game["turns"]<=0:
        game_over()
        return
    game["turns"] -= 1
    update_mogura()
    update_screen()
    # 次回のタイマーをセット
    setTimeout(next_turn, INTERVAL)


def update_mogura():
    """モグラの状態を変更する関数"""
    game["hide"] = not game["hide"]
    if not game["hide"]:
        game["mx"] = random.randint(0, canvas.width - WIDTH)
        game["my"] = random.randint(0, canvas.height - WIDTH)


def update_screen():
    """ ゲーム画面の更新処理 """
    context.clearRect(0, 0, canvas.width, canvas.height)
    # 背景画像描画
    hatake_img = document.getElementById("hatake_img")
    context.drawImage(hatake_img, 0, 0, canvas.width, canvas.height)

    if not game["hide"]:
        # context.fillStyle = "brown"
        # context.fillRect(game["mx"], game["my"], WIDTH, WIDTH)
        mogura_img = document.getElementById("mogura_img")
        context.drawImage(mogura_img, game["mx"], game["my"], WIDTH, WIDTH)
    info.innerText = (f"スコア: {game['score']}点 /"
                       f"残り時間: {game['turns']}")
    

def game_over():
    """ゲーム終了時の処理"""
    info.innerText = f"モグラ叩き終了: スコア{game['score']}"
    document.getElementById("start_button").disabled = False

