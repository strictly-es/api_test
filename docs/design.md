# チャットアプリ設計書

## 要件定義書

- **目的**: ユーザーが簡単にチャットを楽しむことができるアプリケーションを提供する。
- **機能**:
  - ユーザーがメッセージを入力し送信できる。
  - 相手がランダムな相槌を返す。
  - GUIはGradioを使用して構築する。

## 概略設計

- **フロントエンド**: Gradioを使用してユーザーインターフェースを構築。
- **バックエンド**: Pythonで相槌を生成するロジックを実装。

## 機能設計

- **メッセージ送信機能**:
  - ユーザーが入力したメッセージを送信する。
  - 送信されたメッセージを表示する。

- **相槌生成機能**:
  - いくつかの相槌パターンからランダムに選択して返信する。

## クラス構成

- **ChatApp**: チャットアプリ全体を管理するクラス。
  - `send_message(message: str) -> None`: メッセージを送信する。
  - `generate_reply() -> str`: ランダムな相槌を生成する。