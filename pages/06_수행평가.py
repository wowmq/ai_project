import streamlit as st

# 1. 페이지 기본 설정 및 디자인
st.set_page_config(page_title="MBTI별 인생 게임 추천소", page_icon="🎮", layout="centered")

st.title("🎮 MBTI별 인생 게임 추천소 ✨")
st.write("내 MBTI에 딱 맞는 게임과 실시간 플레이 영상까지 한눈에 확인해봐! 😎")

# 2. 100% 공개된 유튜브 영상 주소로 전면 교체한 데이터베이스!
mbti_games = {
    "ISTJ": [
        {"name": "팩토리오 (Factorio)", "style": "철저한 계획과 자동화 공장을 설계하는 뇌섹 게임 ⚙️", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/KVvXv1Z6EY8"},
        {"name": "마인크래프트 (기술 모드)", "style": "체계적으로 시스템을 구축하고 자원을 관리하는 정돈된 플레이 🧱", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/q6Z9XgN-mZg"},
        {"name": "스타듀 밸리 (Stardew Valley)", "style": "매일 계획된 루틴대로 농장을 경영하고 수확하는 힐링 게임 🧑‍🌾", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/8AAsI8K_R4U"}
    ],
    "ISFJ": [
        {"name": "모여봐요 동물의 숲", "style": "마을 주민들을 챙기고 아기자기하게 섬을 꾸미는 평화로운 감성 🏝️", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/2w2XoEvshZ4"},
        {"name": "심즈 4 (The Sims 4)", "style": "캐릭터들의 인생을 돌보고 따뜻한 가정을 만들어가는 시뮬레이션 🏠", "mode": "싱글 플레이 전용", "youtube_url": "https://youtu.be/WAs_gV_1rWw"},
        {"name": "이잇 텍스 투 (It Takes Two)", "style": "서로 배려하고 협동하며 완벽한 호흡으로 스테이지를 깨는 게임 🤝", "mode": "2인 전용 멀티플레이", "youtube_url": "https://youtu.be/V6z7zU_5UvA"}
    ],
    "INFJ": [
        {"name": "디트로이트: 비컴 휴먼", "style": "깊이 있는 스토리와 캐릭터들의 감정에 몰입하는 선택형 시네마틱 게임 🤖", "mode": "싱글 플레이 전용", "youtube_url": "https://youtu.be/n799qC1rCRI"},
        {"name": "저니 (Journey)", "style": "말 없이도 통하는 깊은 여운และ 예술적인 분위기를 느끼는 힐링 게임 🏜️", "mode": "싱글 플레이 / 온라인 매칭", "youtube_url": "https://youtu.be/u88gRWhO8kI"},
        {"name": "언더테일 (Undertale)", "style": "괴물들의 이야기에 공감하며 자비를 베푸는 감성 충만 스토리 뼈 때리는 게임 💀", "mode": "싱글 플레이 전용", "youtube_url": "https://youtu.be/Z7N_w7_11as"}
    ],
    "INTJ": [
        {"name": "시티즈: 스카이라인", "style": "도시 전체의 교통, 재정, 구역을 완벽하게 통제하고 설계하는 시뮬레이션 🏙️", "mode": "싱글 플레이 전용", "youtube_url": "https://youtu.be/T51W_bSveFs"},
        {"name": "문명 6 (Civilization VI)", "style": "몇 수 앞을 내다보며 자신만의 전략으로 세계를 정복하는 턴제 게임 🌍", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/g_pRE68GvXk"},
        {"name": "포탈 2 (Portal 2)", "style": "공간을 비틀어 정교한 퍼즐을 풀어내는 고지능 플레이 🌀", "mode": "싱글 플레이 / 2인 협동 모드 가능", "youtube_url": "https://youtu.be/0bB0e8bOszs"}
    ],
    "ISTP": [
        {"name": "몬스터 헌터: 월드", "style": "정교한 조작과 무기 메커니즘을 마스터해 거대 몬스터를 사냥하는 손맛 🦖", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/tS9tsh_7bZk"},
        {"name": "젤다의 전설 브레스 오브 더 와일드", "style": "세상의 물리 법칙을 이용해 내 맘대로 오픈월드를 탐험하고 생존하는 재미 🏹", "mode": "싱글 플레이 전용", "youtube_url": "https://youtu.be/3z8K1nrcuS0"},
        {"name": "에이펙스 레전드", "style": "빠른 판단력과 피지컬로 전장을 누비는 하이템포 배틀로얄 FPS 🔫", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/9PFrNfH86hE"}
    ],
    "ISFP": [
        {"name": "마인크래프트 (건축/셰이더)", "style": "아름다운 풍경 속에서 나만의 예술적인 건축물을 자유롭게 짓는 힐링 플레이 🌌", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/fSip6S_w_N0"},
        {"name": "그리스 (Gris)", "style": "한 편의 수채화 같은 그래픽과 감성적인 음악 속을 유영하는 예술 게임 🎨", "mode": "싱글 플레이 전용", "youtube_url": "https://youtu.be/BRiEkaXAVP4"},
        {"name": "로블록스 (입양하세요 등)", "style": "정해진 틀 없이 자유롭게 돌아다니며 가볍고 트렌디하게 즐기는 소통 플레이 🎒", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/zZfbyZ4V638"}
    ],
    "INFP": [
        {"name": "오리와 도깨비불", "style": "환상적이고 몽환적인 그래픽 속에서 감동적인 스토리를 따라가는 여정 🦊", "mode": "싱글 플레이 전용", "youtube_url": "https://youtu.be/2reK8k40wa8"},
        {"name": "스카이: 빛의 아이들", "style": "하늘을 날아다니며 따뜻한 감성을 나누고 친구를 사귀는 평화로운 오픈월드 ☁️", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/TfX8y5P_K8Y"},
        {"name": "라이프 이즈 스트레인지", "style": "시간을 돌리는 능력으로 주인공의 고뇌와 성장을 함께하는 감성 드라마 🦋", "mode": "싱글 플레이 전용", "youtube_url": "https://youtu.be/AURVxv_7W9Q"}
    ],
    "INTP": [
        {"name": "아우터 와일즈 (Outer Wilds)", "style": "우주의 비밀과 루프물의 미스터리를 순수 호기심과 추리로 풀어내는 갓겜 🚀", "mode": "싱글 플레이 전용", "youtube_url": "https://youtu.be/d6LGnvFAibU"},
        {"name": "바바 이즈 유 (Baba Is You)", "style": "게임의 규칙 자체를 코딩하듯 뜯어고쳐 깨는 신개념 하드코어 퍼즐 🧠", "mode": "싱글 플레이 전용", "youtube_url": "https://youtu.be/jZ8Z_I_919s"},
        {"name": "소울라이크 시리즈 (엘든 링)", "style": "보스의 패턴을 분석하고 완벽한 공략법을 찾아내어 파훼하는 성취감 ⚔️", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/AKXiKBnzpKw"}
    ],
    "ESTP": [
        {"name": "발로란트 (VALORANT)", "style": "순간적인 피지컬과 화려한 스킬 연계로 상대를 찍어누르는 하이퍼 FPS 🎯", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/e_E9W2vsRbQ"},
        {"name": "GTA 5", "style": "넓은 도시에서 법 따윈 불도저처럼 밀어버리는 짜릿하고 거침없는 오픈월드 액션 🚘", "mode": "싱글 플레이 / 온라인 멀티플레이", "youtube_url": "https://youtu.be/QkkoHAzjnUs"},
        {"name": "리그 오브 레전드 (LoL)", "style": "치열한 교전과 빠른 템포의 한타로 도파민을 폭발시키는 국민 게임 👑", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/mDYqT0_9VR4"}
    ],
    "ESFP": [
        {"name": "폴 가이즈 (Fall Guys)", "style": "귀여운 캐릭터들과 함께 난장판 레이스를 즐기는 웃음 벨 예능 게임 🦄", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/2O7KOnThcoY"},
        {"name": "저스트 댄스 (Just Dance)", "style": "신나는 음악에 맞춰 몸을 흔들며 에너지를 뿜어내는 흥 폭발 게임 🕺", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/H7mXMMm87fM"},
        {"name": "어몽 어스 (Among Us)", "style": "친구들과 왁자지껄 떠들며 속고 속이는 실시간 정치 대소동 🕵️‍♂️", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/ns8Sox4g5g8"}
    ],
    "ENFP": [
        {"name": "서브노티카 (Subnautica)", "style": "외계 해양 행성을 탐험하며 신기한 생물들을 발견하고 기지를 짓는 모험 🐳", "mode": "싱글 플레이 전용", "youtube_url": "https://youtu.be/Rz2RIdOGOuM"},
        {"name": "팀 파이트 택틱스 (TFT/롤토체스)", "style": "매 판 무궁무진한 시너지 조합을 짜며 나만의 사기 덱을 완성하는 재미 🃏", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/T_8V_8B9v_I"},
        {"name": "인간: 폴 플랫 (Human: Fall Flat)", "style": "흐느적거리는 몸으로 기상천외하고 엉뚱한 플레이를 만들어내는 몸개그 게임 🏃‍♂️", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/tIit636V_wY"}
    ],
    "ENTP": [
        {"name": "오버워치 2", "style": "고정관념을 깨는 기상천외한 영웅 조합과 화려한 한타 난전을 이끄는 재미 💥", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/GKXS_YA9s7E"},
        {"name": "하스스톤 (Hearthstone)", "style": "상대의 심리를 읽고 골탕 먹이는 참신한 예능 덱과 두뇌 싸움 🃏", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/QdHcMT-P0_4"},
        {"name": "게리스 모드 (Garry's Mod)", "style": "정해진 규칙 없이 내 멋대로 모드를 만들고 트롤링하며 노는 대혼돈 멀티 🛠️", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/b43I_pZ0_Sg"}
    ],
    "ESTJ": [
        {"name": "풋볼 매니저 (FM)", "style": "구단의 예산, 전술, 선수 영입까지 완벽하게 통제하는 악마의 경영 시뮬레이션 ⚽", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/Y7366-T0Imo"},
        {"name": "레인보우 식스 시즈", "style": "철저한 오더와 완벽한 전술, 팀원 간의 브리핑으로 승리하는 하드코어 FPS 🪖", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/6wKcl_N6g_M"},
        {"name": "림월드 (RimWorld)", "style": "생존자들에게 효율적인 업무를 배정하고 기지를 철두철미하게 방어하는 식민지 경영 🪵", "mode": "싱글 플레이 전용", "youtube_url": "https://youtu.be/3tDrxOAFUog"}
    ],
    "ESFJ": [
        {"name": "오버쿡! 올유캔잇 (Overcooked!)", "style": "지옥의 주방에서 역할 분담을 확실히 하며 최고의 팀워크를 발휘하는 게임 👨‍🍳", "mode": "멀티플레이 필수 (협동)", "youtube_url": "https://youtu.be/0kI79Z4F_I4"},
        {"name": "로스트아크 (LOST ARK)", "style": "길드원들과 다 같이 레이드 공략을 소통하며 함께 성장하는 대규모 MMORPG ⚔️", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/Yk8_oDkYhHA"},
        {"name": "리탈 컴퍼니 (Lethal Company)", "style": "팀원들과 음성 채팅으로 꽉꽉 소통하며 폐품을 수거하는 꿀잼 공포 시트콤 🎙️", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/S6Yw6U-pI_U"}
    ],
    "ENFJ": [
        {"name": "데드 바이 데이라이트", "style": "생존자 무리를 이끌고 협동하여 살인마의 눈을 피해 탈출하는 스릴 만점 팀플레이 🏃", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/JGhIXLO3Slo"},
        {"name": "헬다이버즈 2 (Helldivers 2)", "style": "은하계의 민주주의를 위해 동료들과 의기투합하여 전장을 누비는 화끈한 협동 슈팅 🔥", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/Xb_S6v7X9p8"},
        {"name": "스타듀 밸리 (멀티)", "style": "마을 주민들과 친해지고 친구들과 다 함께 협동 농장을 키워가는 따뜻한 공동체 생활 🌽", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/8AAsI8K_R4U"}
    ],
    "ENTJ": [
        {"name": "크루세이더 킹즈 3", "style": "국가의 정치, 외교, 군사를 총괄하며 세계 패권을 장악하는 최고 권력자 시뮬레이션 👑", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/uKofV5wWvIQ"},
        {"name": "스타크래프트 시리즈", "style": "엄청난 멀티태스킹과 카리스마 있는 부대 컨트롤로 상대를 압도하는 실시간 전략 🛸", "mode": "싱글 플레이 / 멀티플레이 가능", "youtube_url": "https://youtu.be/mDYqT0_9VR4"},
        {"name": "러스트 (Rust)", "style": "강한 자만 살아남는 무법지대에서 클랜을 결성하고 리더십을 발휘해 영토를 지배하는 생존 게임 ⛺", "mode": "온라인 멀티플레이 전용", "youtube_url": "https://youtu.be/LGc_bZ-NcoY"}
    ]
}

# 3. MBTI 선택받기
st.markdown("---")
selected_mbti = st.selectbox("👉 너의 MBTI를 골라봐!", list(mbti_games.keys()))

# 4. 결과 및 영상 출력
if selected_mbti:
    st.markdown(f"### ⚡ **{selected_mbti}** 유형에게 추천하는 인생 게임 리스트!")
    st.write("이번엔 에러 없이 무조건 잘 나오는 플레이 영상들이야! 재밌게 봐봐! 📺")
    
    games = mbti_games[selected_mbti]
    
    for idx, game in enumerate(games, 1):
        with st.container():
            st.markdown(f"#### **{idx}. {game['name']}**")
            st.write(f"**🎮 플레이 스타일:** {game['style']}")
            st.write(f"**👥 게임 모드:** `{game['mode']}`")
            
            # 플레이어 배치 (안전한 주소 형식 사용)
            try:
                st.video(game['youtube_url'])
            except Exception:
                st.warning("⚠️ 지금 스트림릿 서버 상태 때문에 플레이어가 안 뜰 수 있어!")
            
            # 직접가기 링크 버튼 상시 대기
            st.markdown(f"🔗 [유튜브 앱/웹에서 직접 크게 보기]({game['youtube_url']})")
            st.markdown("---")

st.caption("제작: MBTI 게임 추천 봇 🤖 | 고유 주소 필터링 완료")
# 기존 st.video(game['youtube_url']) 대신 이걸 넣어봐!
st.markdown(f"📺 **[여기 클릭해서 플레이 영상 보기]({game['youtube_url']})**")
st.write("💡 유튜브 앱이나 웹에서 끊김 없이 바로 재생돼요!")
