def start_button_on_click(event):
    """ 開始ボタンをクリックされたときの処理 """
    document.getElementById("start_button").disabled = True
    game["turns"] = GAME_TURNS
    game["score"] = 0
    next_turn()    


def canvas_on_click(event):
    """ canvasをクリックしたときの処理 """
    rect = canvas.getBoundingClientRect()
    click_x = event.clientX - rect.left
    click_y = event.clientY - rect.top
    if not game["hide"]:
        if (game["mx"] <= click_x <= game["mx"] + WIDTH and 
            game["my"] <= click_y <= game["my"] + WIDTH):
            game["score"] += 1
            game["hide"] = True

