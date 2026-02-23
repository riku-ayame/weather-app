##1 Webアプリを作る
import streamlit as st
import numpy as np
import pandas as pd
# 1. アプリのタイトルとテキスト
st.title("波形シミュレーター ⚡️")
st.write("スライダーを動かして、リアルタイムで波形を変化させてみましょう！")
# 2. ユーザーが操作できるスライダー（最小1Hz、最大10Hz、初期値5Hz）
freq = st.slider("周波数 (Hz)", min_value=1, max_value=10, value=5)
# 3. データの作成（2-2でやったNumpyの活用）
t = np.linspace(0, 1, 500) # 0秒から1秒まで500個のデータ
y = np.sin(2 * np.pi * freq * t) # サイン波の計算
# Pandasの表（データフレーム）に変換
df = pd.DataFrame({
    "Time": t,
    "Amplitude": y
})
# 4. Streamlit専用の超簡単グラフ描画！
st.line_chart(df, x="Time", y="Amplitude")



##2 アプリの起動
#Streamlitは、いつもの右上の「▶︎」ボタンでは起動できません。
#Webサーバーを立ち上げる必要があるため、ターミナルから専用のコマンドで呼び出します。
#streamlit run ファイル名.py