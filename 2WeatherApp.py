import streamlit as st
import requests
import pandas as pd

# 1. アプリのタイトルと説明
st.title("🌍 リアルタイムお天気ダッシュボード")
st.write("選択した都市の向こう1週間の気温予測をAPIから自動取得してグラフ化します。")

# 2. 都市の選択肢（辞書型で緯度・経度を管理）
cities = {
    "東京": {"lat": 35.6895, "lon": 139.6917},
    "大阪": {"lat": 34.6937, "lon": 135.5023},
    "京都": {"lat": 35.0116, "lon": 135.7681},
    "札幌": {"lat": 43.0621, "lon": 141.3544}, 
    "福岡": {"lat": 33.5902, "lon": 130.4017}
}

# st.selectbox でプルダウンメニューを作成
selected_city = st.selectbox("🌍 都市を選んでください", list(cities.keys()))

# 3. 選択された都市の座標を使ってAPI通信（４データ収集の復習！）
lat = cities[selected_city]["lat"]
lon = cities[selected_city]["lon"]
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&timezone=Asia%2FTokyo"

# データを取得してJSONに変換
response = requests.get(url)
data = response.json()

# 4. データをPandasの表（データフレーム）に変換
times = pd.to_datetime(data["hourly"]["time"]) # 時間をきれいなフォーマットに変換
temps = data["hourly"]["temperature_2m"]

# グラフを描きやすいように、時間を「インデックス（見出し）」にする
df = pd.DataFrame({"気温 (℃)": temps}, index=times)

# 5. UI（ユーザーインターフェース）パーツ（最高・最低気温を大きく表示）
max_temp = df["気温 (℃)"].max()
min_temp = df["気温 (℃)"].min()

# 画面を2つのカラム（列）に分割して、数字を目立たせる（st.metric）
#st.metric 一番見せたい重要な数字（KPI）を、リッチな見た目でドーンと表示するための専用パーツ
col1, col2 = st.columns(2)
col1.metric("🔥 期間中の最高気温", f"{max_temp} ℃")
col2.metric("❄️ 期間中の最低気温", f"{min_temp} ℃")

# 6. Streamlit専用のグラフ描画
st.line_chart(df)



##サーバーの一時停止
#ターミナルはStreamlitのアプリを動かすために「働きっぱなし」の状態です。
# まずはこれにストップをかけて、いつものコマンドが打てる状態に戻します。
#ターミナルをクリックして選択し、キーボードの Control キーと C キーを同時押し してください。
#Stopping... と出て、いつもの入力画面（% や $ のマーク）に戻れば成功です！



##設計図を作る
#自分のPCにはすでに pandas や streamlit がインストールされていますが、
# GitHubやインターネット上のサーバーは「このアプリを動かすために、どのライブラリが必要なのか」
# を知りません。
#その「必要な部品リスト」をまとめた設計図を作ります。
#requirements.txtを作成する