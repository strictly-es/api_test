import pytest
from chat_app import ChatApp

def test_generate_reply():
    chat_app = ChatApp()
    reply = chat_app.generate_reply()
    assert reply in chat_app.replies

def test_send_message():
    chat_app = ChatApp()
    message = "こんにちは"
    reply = chat_app.send_message(message)
    assert reply in chat_app.replies

if __name__ == "__main__":
    pytest.main()