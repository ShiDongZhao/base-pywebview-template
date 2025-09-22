import webview



class Api:
    pass

api = Api()

window = webview.create_window(
    "图片下载工具",
    # "http://localhost:5173/",
    "./web/index.html",
    width=800,
    height=720,
    resizable=True,
    confirm_close=True,
    text_select=False,
    js_api=api,
    localization={
        "global.quitConfirmation": "确定关闭?",
    },
)


def on_closed():
    import os
    os._exit(0)  # 强制终止所有进程


# 修改事件绑定方式
window.events.closed += on_closed  # 使用 events 属性绑定关闭事件

webview.start()
