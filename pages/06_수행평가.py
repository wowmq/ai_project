import streamlit as st
import csv

# 페이지 설정
st.set_page_config(page_title="MBTI 게임 추천소 v2", page_icon="🎮", layout="wide")

st.title("✨ MBTI별 찰떡 게임 추천소 ✨")
st.write("내 MBTI를 선택하면, 너의 성향에 딱 맞는 레전드 게임 3개를 장르별로 추천해줄게! 🚀")

# CSV 파일에서 안전하게 데이터 읽어오기
mbti_games = {}
with open('games.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        mbti = row['mbti']
        if mbti not in mbti_games:
            mbti_games[mbti] = []
        mbti_games[mbti].append(row)

mbti_list = sorted(list(mbti_games.keys()))
user_mbti = st.selectbox("너의 MBTI는 뭐야? 선택해봐! 👇", mbti_list)

if user_mbti:
    games = mbti_games[user_mbti]
    st.divider()
    st.subheader(f"✨ [{user_mbti}] 유형을 위한 추천 게임 Top 3! ✨")
    st.write("너의 성향에 맞춰서 재미 보장하는 게임들로 3개 꽉꽉 채워왔어 ✌️")
    st.write("")

    cols = st.columns(3)
    for i, game in enumerate(games):
        with cols[i]:
            with st.container(border=True):
                st.markdown(f"### {game['emoji']} {game['name']}")
                st.write(f"**🧐 스타일:** {game['style']}")
                st.write(f"**👥 플레이 방식:** {game['mode']}")
                
    st.success("이 중에 너의 취향을 저격한 게임이 분명히 있을 거야! 친구들이랑 공유해서 같이 골라봐! 🎮🔥")
