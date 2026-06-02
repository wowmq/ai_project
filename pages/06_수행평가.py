import streamlit as st
import json

# 페이지 기본 설정
st.set_page_config(page_title="MBTI Game Recommender", page_icon="🎮")

st.title("✨ MBTI별 찰떡 게임 추천소 ✨")
st.write("내 MBTI를 선택하면, 너한테 딱 어울리는 레전드 게임 3개를 추천해줄게! 🔥")

# 컴파일 에러를 원천 차단하기 위해 데이터를 JSON 문자열로 격리 처리!
raw_json = """
{
    "ISTJ": [
        {"name": "\\uc2a4\\ud0c0\\ub4c0\\ubc38\\ub9ac", "style": "\\uaf3c\\uaf3c\\ud55c \\uacc4\\ud68d\\uacfc \\ub8e8\\ud2f4\\uc774 \\ud575\\uc2ec! \\ub18d\\uc7a5\\uc744 \\uacbd\\uc601\\ud558\\uba70 \\uccb4\\uacc4\\uc801\\uc73c\\ub85c \\uc131\\uc7a5\\ud558\\ub294 \\uc7ac\\ubbf8", "mode": "\\uc194\\ub85c (\\uba40\\ud220 \\uac00\\ub2a5)", "emoji": "\\ud83d\\udc68\\u200d\\ud83c\\udf3e"},
        {"name": "\\ud329\\ud1a0\\ub9ac\\uc624", "style": "\\ucui1c\\uc801\\uc758 \\ud6a8\\uc728\\uc744 \\uc263\\uc544 \\uacf5\\uc7a5\\uc744 \\uc790\\ub3d9\\ud654\\ud558\\ub294 \\ub450\\ub1cc \\ud480\\uac00\\ub3d9 \\uc2dc\\ubbac\\ub808\\uc774\\uc158", "mode": "\\uc194\\ub85c (\\uba40\\ud220 \\uac00\\ub2a5)", "emoji": "\\ud83c\\udfed"},
        {"name": "\\ud48b\\ubcbc\\ub9e4\\ub2c8\\uc800", "style": "\\ubc29\\ub300\\ud55c \\ub370\\uc774\\ud130\\ub9bc \\ubd84\\uc11d\\ud558\\uace0 \\uad6c\\ub2e8\\uc744 \\uad00\\ub9ac\\ud558\\ub294 \\ubcc8\\uaca9 \\uacfc\\ubab0\\uc785 \\uacbd\\uc601 \\uac8c\\uc784", "mode": "\\uc194\\ub85c \\uc804\\uc6a9", "emoji": "\\ud83d\\udccb"}
    ],
    "ISFJ": [
        {"name": "\\ubaa8\\uc5ec\\ubd10\\uc694 \\ub3d9\\ubc3c\\uc758 \\uc232", "style": "\\uc8fc\\ubcc0\\uc744 \\uac00\\uafb8\\uace0 \\uc8fc\\ubbfc\\ub4e4\\uc744 \\uac59\\ub9ac\\ub294 \\ub530\\ub73b\\ud55c \\ud790\\ub9e5 \\uc2a4\\ud0c0\\uc77c", "mode": "\\uc194\\ub85c (\\uba40\\ud220 \\uac00\\ub2a5)", "emoji": "\\ud83c\\udf43"},
        {"name": "\\uc5b8\\ud328\\ud0b9", "style": "\\uc774\\uc0bf\\uc9짐\\uc744 \\uc815\\ud574\\uc9c4 \\uc790\\ub9ac\\uc5d0 \\ud428\\ubd84\\ud788 \\uc815\\ub9ac\\ud558\\uba70 \\ub9c8\\uc7
