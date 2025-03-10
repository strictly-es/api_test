import gradio as gr
import random

class ChatApp:
    def __init__(self):
        self.replies = [
            "そうですね。",
            "なるほど。",
            "わかります。",
            "それは面白いですね。",
            "そうなんですか。"
        ]

    def send_message(self, message: str) -> str:
        return self.generate_reply()

    def generate_reply(self) -> str:
        return random.choice(self.replies)

def chat_interface(user_input):
    chat_app = ChatApp()
    return chat_app.send_message(user_input)

iface = gr.Interface(
    fn=chat_interface,
    inputs="text",
    outputs="text",
    title="チャットアプリ",
    description="メッセージを入力して送信してください。"
)

if __name__ == "__main__":
    iface.launch()