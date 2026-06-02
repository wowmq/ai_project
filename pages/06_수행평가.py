import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 게임 추천소", page_icon="🎮")

# 제목 부분
st.title("✨ MBTI별 찰떡 게임 추천소 ✨")
st.write("내 MBTI를 선택하면, 너한테 딱 어울리는 레전드 게임을 추천해줄게! 🔥")

# MBTI 데이터베이스
mbti_games = {
    "ISTJ": {"name": "스타듀밸리", "style": "꼼꼼한 계획과 루틴이 핵심! 농장을 경영하며 체계적으로 성장하는 재미 🌱", "mode": "솔로 (멀티 가능)", "emoji": "👨‍🌾"},
    "ISFJ": {"name": "모여봐요 동물의 숲", "style": "주변을 가꾸고 주민들을 챙기는 따뜻한 힐링 스타일 🍎", "mode": "솔로 (멀티 가능)", "emoji": "🍃"},
    "INFJ": {"name": "언더테일", "style": "심오한 스토리와 철학적인 선택! 내 선택에 따라 결말이 바뀌는 감성 게임 뼈", "mode": "솔로 전용", "emoji": "💀"},
    "INTJ": {"name": "팩토리오", "style": "최적의 효율을 찾아 공장을 자동화하는 두뇌 풀가동 시뮬레이션 ⚙️", "mode": "솔로 (멀티 가능)", "emoji": "🏭"},
    "ISTP": {"name": "마인크래프트", "style": "도구를 만들고 세상을 내 마음대로 개조하는 진정한 자유도! 🛠️", "mode": "솔로 & 멀티 모두 지원", "emoji": "⛏️"},
    "ISFP": {"name": "저니 (Journey)", "style": "아름다운 영상미와 음악을 즐기며 정처 없이 떠나는 예술적 경험 🌅", "mode": "솔로 (랜덤 만남 가능)", "emoji": "🧣"},
    "INFP": {"name": "스카이: 빛의 아이들", "style": "몽환적인 하늘을 날아다니며 평화를 전파하는 감성 끝판왕 ☁️", "mode": "솔로 & 멀티 모두 지원", "emoji": "✨"},
    "INTP": {"name": "포탈 (Portal) 시리즈", "style": "물리학 법칙을 이용해 공간을 넘나드는 천재적인 퍼즐 해결 🌀", "mode": "솔로 (2편은 멀티 가능)", "emoji": "🧪"},
    "ESTP": {"name": "에이펙스 레전드", "style": "빠른 속도감과 화려한 스킬! 전장을 휩쓰는 극한의 피지컬 게임 🔫", "mode": "멀티 전용", "emoji": "🏃"},
    "ESFP": {"name": "저스트 댄스", "style": "리듬에 몸을 맡기고 신나게 춤추며 에너지를 발산하는 파티형 게임 💃", "mode": "솔로 & 멀티 모두 지원", "emoji": "🪩"},
    "ENFP": {"name": "폴 가이즈", "style": "예측 불허한 상황 속에서 우당탕탕 순위 경쟁을 펼치는 꿀잼 서바이벌 🍬", "mode": "멀티 전용", "emoji": "👑"},
    "ENTP": {"name": "어몽 어스", "style": "화려한 말빨과 심리전으로 상대를 속이고 추리하는 전략 게임 🔪", "mode": "멀티 전용", "emoji": "🚀"},
    "ESTJ": {"name": "심시티 / 시티즈 스카이라인", "style": "도시를 건설하고 세금을 관리하며 완벽한 질서를 만드는 경영 게임 🏙️", "mode": "솔로 전용", "emoji": "📐"},
    "ESFJ": {"name": "잇 테이크 투", "style": "서로 협력하지 않으면 절대 깰 수 없는 찐 우정/커플 테스트 게임 🧸", "mode": "멀티 전용 (2인)", "emoji": "🤝"},
    "ENFJ": {"name": "더 심즈", "style": "캐릭터들의 관계를 만들고 인생을 설계하며 커뮤니티를 가꾸는 재미 🏠", "mode": "솔로 전용", "emoji": "💎"},
    "ENTJ": {"name": "리그 오브 레전드", "style": "승리를 위한 완벽한 오더와 전략적 판단으로 전장을 지배하는 스타일 ⚔️", "mode": "멀티 전용", "emoji": "🏆"},
}

# 사이드바나 메인화면에서 선택
mbti_list = sorted(list(mbti_games.keys()))
user_mbti = st.selectbox("너의 MBTI는 뭐야? 선택해봐! 👇", mbti_list)

if user_mbti:
    game = mbti_games[user_mbti]
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.header(f"{game['emoji']} {game['name']}")
    
    with col2:
        st.subheader(f"[{user_mbti}] 유형에게 딱이야!")
        st.write(f"**🧐 스타일:** {game['style']}")
        st.write(f"**👥 플레이 방식:** {game['mode']}")

    st.success(f"\"{user_mbti}\"인 너랑 완전 잘 어울릴 것 같지 않아? 이번 주말에 한 번 달려봐! 🚀")
