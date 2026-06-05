import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="Masterpiece MBTI Game Recommender", page_icon="🎮", layout="centered")

st.title("🚀 MBTI 멀티버스 게임 매칭 플랫폼 🚀")
st.write("간이 테스트부터 친구 궁합, 나만의 위시리스트까지 수행평가 끝판왕 앱에 오신 것을 환영합니다! ✨")

# 데이터 정의 (성향 요약)
mbti_descriptions = {
    "ISTJ": "철저하고 신중하며 규칙을 좋아하는 '청렴결백한 공무원'형", "ISFJ": "성실하고 따뜻하게 주변을 보살피는 '용감한 수호자'형",
    "INFJ": "깊은 통찰력으로 몽환적인 서사를 좋아하는 '선의의 옹호자'형", "INTJ": "철저한 전략과 계산을 즐기는 '용의주도한 전략가'형",
    "ISTP": "도구와 물리 엔진을 잘 다루는 '만능 재주꾼'형", "ISFP": "예술적 감수성이 풍부한 '호기심 많은 예술가'형",
    "INFP": "낭만적이며 독창적인 스토리에 과몰입하는 '열정적인 중재자'형", "INTP": "복잡한 퍼즐을 풀 때 희열을 느끼는 '논리적인 사색가'형",
    "ESTP": "빠른 피지컬로 전장을 휩쓰는 '수완 좋은 활동가'형", "ESFP": "신나는 리듬과 파티를 즐기는 '자유로운 영혼의 연예인'형",
    "ENFP": "재기발랄하게 우당탕탕 모험을 떠나는 '활동가'형", "ENTP": "지능적인 심리전으로 판을 뒤흔드는 '뜨거운 변론가'형",
    "ESTJ": "효율적인 시스템을 구축하고 통제하는 '엄격한 관리자'형", "ESFJ": "소통과 역할 분담을 잘하는 '사교적인 외교관'형",
    "ENFJ": "정의로운 리더십으로 평화를 이끄는 '정의로운 지도자'형", "ENTJ": "대담한 통솔력과 큰 스케일로 정복하는 '대담한 통솔자'형"
}

# 게임 데이터 (사진 완벽 제거 깔끔 버전)
mbti_games = {
    "ISTJ": [{"name": "스타듀밸리", "style": "꼼꼼한 계획과 루틴으로 농장 경영", "mode": "솔로 (멀티 가능)"}, {"name": "팩토리오", "style": "최적의 효율을 찾는 공장 자동화 시뮬레이션", "mode": "솔로 (멀티 가능)"}, {"name": "풋볼매니저 (FM)", "style": "방대한 데이터 분석과 구단 관리", "mode": "솔로 전용"}],
    "ISFJ": [{"name": "모여봐요 동물의 숲", "style": "주변을 가꾸고 주민들을 챙기는 힐링", "mode": "솔로 (멀티 가능)"}, {"name": "언패킹", "style": "이삿짐을 정해진 자리에 정리하는 안정감", "mode": "솔로 전용"}, {"name": "하우스 플리퍼", "style": "더러운 집을 깨끗하게 인테리어 개조", "mode": "솔로 전용"}],
    "INFJ": [{"name": "언더테일", "style": "선택에 따라 결말이 바뀌는 깊은 서사", "mode": "솔로 전용"}, {"name": "오리와 도깨비불", "style": "아름다운 동화 속 서사 탐험", "mode": "솔로 전용"}, {"name": "디트로이트: 비컴 휴먼", "style": "인간성을 묻는 영화 같은 선택형 게임", "mode": "솔로 전용"}],
    "INTJ": [{"name": "시티즈: 스카이라인", "style": "완벽한 도시 교통망과 구역 설계", "mode": "솔로 전용"}, {"name": "슬레이 더 스파이어", "style": "철저한 계산으로 덱을 짜는 전략", "mode": "솔로 전용"}, {"name": "체스", "style": "오직 수싸움으로만 승부하는 지적 대결", "mode": "솔로 & 멀티 모두 지원"}],
    "ISTP": [{"name": "마인크래프트", "style": "세상을 내 마음대로 개조하는 최고 자유도", "mode": "솔로 & 멀티 지원"}, {"name": "몬스터 헌터 월드", "style": "무기 메커니즘을 마스터하는 피지컬 사냥", "mode": "솔로 (멀티 가능)"}, {"name": "젤다의 전설 야숨", "style": "물리 엔진을 활용한 오픈월드 공략", "mode": "솔로 전용"}],
    "ISFP": [{"name": "저니 (Journey)", "style": "영상미와 음악을 즐기는 예술적 힐링", "mode": "솔로 (랜덤 만남)"}, {"name": "데이브 더 다이버", "style": "낮에는 해양 탐험, 밤에는 초밥집 경영", "mode": "솔로 전용"}, {"name": "슬라임 랜처", "style": "귀여운 슬라임들을 수집하는 농장 경영", "mode": "솔로 전용"}],
    "INFP": [{"name": "스카이: 빛의 아이들", "style": "몽환적인 하늘을 날아다니는 감성 게임", "mode": "솔로 & 멀티 지원"}, {"name": "투 더 문", "style": "기억을 바꾸어 소원을 들어주는 감동 스토리", "mode": "솔로 전용"}, {"name": "라이프 이즈 스트레인지", "style": "시간을 되돌려 선택의 무게를 배우는 드라마", "mode": "솔로 전용"}],
    "INTP": [{"name": "포탈 시리즈", "style": "물리학 법칙을 이용한 공간 퍼즐 해결", "mode": "솔로 (2인 멀티 가능)"}, {"name": "바바 이즈 유", "style": "게임 규칙 자체를 코딩하듯 바꾸는 퍼즐", "mode": "솔로 전용"}, {"name": "아우터 와일즈", "style": "우주의 비밀을 푸는 본격 우주 탐사 추리", "mode": "솔로 전용"}],
    "ESTP": [{"name": "에이펙스 레전드", "style": "빠른 속도감과 화려한 스킬의 FPS", "mode": "멀티 전용"}, {"name": "GTA 5", "style": "지루할 틈 없는 도시 속 최고 자유도", "mode": "솔로 & 멀티 지원"}, {"name": "포르자 호라이즌", "style": "오픈월드를 슈퍼카로 질주하는 레이싱", "mode": "솔로 & 멀티 지원"}],
    "ESFP": [{"name": "저스트 댄스", "style": "신나게 몸을 흔들며 에너지를 발산하는 파티", "mode": "솔로 & 멀티 지원"}, {"name": "로블록스", "style": "친구들과 우당탕탕 노는 미니게임 놀이터", "mode": "멀티 전용"}, {"name": "폴가이즈", "style": "귀여운 인형들의 우당탕탕 서바이벌 런", "mode": "멀티 전용"}],
    "ENFP": [{"name": "레드 데드 리뎀션 2", "style": "광활한 서부 시대를 방랑하는 로망", "mode": "솔로 (멀티 가능)"}, {"name": "파티 애니멀즈", "style": "흐물거리는 동물들의 난장판 몸싸움", "mode": "멀티 전용"}, {"name": "갱비스트", "style": "친구들을 난간 밑으로 던지는 난투 파티", "mode": "멀티 전용"}],
    "ENTP": [{"name": "어몽 어스", "style": "화려한 말빨과 심리전의 마피아 게임", "mode": "멀티 전용"}, {"name": "문명 6", "style": "기발한 변수로 전 세계를 정복하는 전략", "mode": "솔로 (멀티 가능)"}, {"name": "플레이트 업", "style": "요리하고 동선을 개조하는 식당 로그라이크", "mode": "멀티 권장"}],
    "ESTJ": [{"name": "림월드", "style": "정착민들에게 효율적 업무를 배정 및 기지 관리", "mode": "솔로 전용"}, {"name": "트로피코 6", "style": "독재자가 되어 경제 구조를 꽉 잡는 경영", "mode": "솔로 (멀티 가능)"}, {"name": "플래닛 주", "style": "완벽한 통제로 맞추는 5성급 동물원 경영", "mode": "솔로 전용"}],
    "ESFJ": [{"name": "잇 테이크 투", "style": "서로 협력하지 않으면 못 깨는 레전드 협동", "mode": "멀티 전용 (2인)"}, {"name": "오버쿡", "style": "완벽한 역할 분담의 대환장 주방 대소동", "mode": "멀티 전용"}, {"name": "래프트 (Raft)", "style": "자원을 모아 뗏목을 키우는 해상 생존", "mode": "멀티 권장"}],
    "ENFJ": [{"name": "더 심즈 4", "style": "캐릭터들의 관계를 조율하는 시뮬레이션", "mode": "솔로 전용"}, {"name": "발더스 게이트 3", "style": "동료들의 마음을 이끌어 세상을 구하는 RPG", "mode": "솔로 (멀티 가능)"}, {"name": "테라리아", "style": "모험과 건설로 나만의 NPC 마을 채우기", "mode": "솔로 & 멀티 지원"}],
    "ENTJ": [{"name": "리그 오브 레전드", "style": "완벽한 오더와 전략적 판단으로 전장 지배", "mode": "멀티 전용"}, {"name": "프로스트펑크", "style": "단호한 결단력으로 인류 생존지를 이끄는 지도자", "mode": "솔로 전용"}, {"name": "스텔라리스", "style": "우주 제국의 지휘관이 되는 대형 스케일 전략", "mode": "솔로 (멀티 가능)"}]
}

# 세션 상태(데이터 가존 유지) 초기화
if "reviews" not in st.session_state:
    st.session_state.reviews = ["[ENFP] 폴가이즈 친구들이랑 하면 우정 파괴 꿀잼ㅋㅋㅋ", "[ISTJ] 스타듀밸리 계획대로 농사지으니 마음이 편안합니다."]
if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

mbti_list = sorted(list(mbti_games.keys()))

# 탭 구성 (수행평가 채점 포인트 다변화)
tab1, tab2, tab3, tab4 = st.tabs(["🎮 게임 추천 및 찜하기", "📝 간이 MBTI 테스트", "👥 친구 게임 궁합", "💬 유저 게시판 & 위시리스트"])

with tab1:
    st.subheader("🎯 내 MBTI 맞춤 게임 찾기")
    user_mbti = st.selectbox("너의 MBTI를 선택해봐! 👇", mbti_list, key="main_mbti")
    
    if user_mbti:
        st.markdown(f"**💡 유형 특징:** *{mbti_descriptions[user_mbti]}*")
        st.write("")
        
        st.markdown("#### 🎮 추천 인생 게임 리스트")
        games = mbti_games[user_mbti]
        
        download_text = f"=== {user_mbti} 추천 게임 리스트 ===\n"
        
        for idx, game in enumerate(games):
            # 레이아웃 정렬을 위해 컬럼 분할 (게임 설명 / 찜하기 버튼)
            g_col1, g_col2 = st.columns([5, 1])
            with g_col1:
                st.markdown(f"**{idx+1}. {game['name']}** ({game['mode']})")
                st.caption(f"↳ {game['style']}")
            with g_col2:
                # [🔥 핵심 기능 1] 실시간 즐겨찾기(위시리스트) 추가 버튼
                if st.button("⭐ 찜", key=f"wish_{user_mbti}_{game['name']}"):
                    if game['name'] not in st.session_state.wishlist:
                        st.session_state.wishlist.append(game['name'])
                        st.toast(f"'{game['name']}'을(를) 위시리스트에 담았습니다!")
                    else:
                        st.toast("이미 담겨있는 게임입니다.")
            
            download_text += f"{idx+1}. {game['name']} [{game['mode']}]\n   - {game['style']}\n"
            
        st.write("")
        st.download_button(
            label="📋 내 추천 결과 메모장으로 다운로드",
            data=download_text,
            file_name=f"{user_mbti}_추천게임.txt",
            mime="text/plain"
        )

with tab2:
    # [🔥 핵심 기능 2] 알고리즘 요소가 가득한 간이 MBTI 테스트
    st.subheader("📝 30초 간이 MBTI 성향 테스트")
    st.write("내 진짜 MBTI를 잘 모르겠다면? 아래 4가지 질문에 답해보세요!")
    
    q1 = st.radio("1. 주말을 보내는 나의 방식은?", ["친구들과 밖에서 신나게 놀기 (E)", "집에서 조용히 혼자 에너지를 충전하기 (I)"])
    q2 = st.radio("2. 게임 속 세상을 볼 때 나는?", ["눈앞에 보이는 퀘스트와 시스템에 집중한다 (S)", "이 세계의 숨겨진 세계관이나 상상을 펼친다 (N)"])
    q3 = st.radio("3. 팀원이 내 플레이 실수를 지적했을 때 내 반응은?", ["지적의 논리적 이유가 맞는지 따져본다 (T)", "말투나 서운한 감정에 먼저 서글퍼진다 (F)"])
    q4 = st.radio("4. 마인크래프트를 시작할 때 나의 행동은?", ["집 지을 구역과 재료 상자 등 계획을 완벽히 짠다 (J)", "일단 발길이 닿는 대로 모험하며 즉흥적으로 시작한다 (P)"])
    
    if st.button("내 결과 분석 및 게임 추천받기 🔮"):
        res_e = "E" if "E" in q1 else "I"
        res_s = "S" if "S" in q2 else "N"
        res_t = "T" if "T" in q3 else "F"
        res_j = "J" if "J" in q4 else "P"
        
        calculated_mbti = res_e + res_s + res_t + res_j
        st.balloons()
        st.success(f"🎉 당신의 임시 분석 MBTI는 **[{calculated_mbti}]** 입니다!")
        st.markdown(f"**[{calculated_mbti}] 추천 대표 게임:**")
        for g in mbti_games[calculated_mbti]:
            st.write(f"- 🎮 **{g['name']}**: {g['style']}")
        st.info("💡 위의 '게임 추천' 탭에서 해당 MBTI를 선택하면 직접 위시리스트에 찜할 수도 있습니다!")

with tab3:
    st.subheader("👥 우리 둘이 같이 게임하면 어떨까?")
    col1, col2 = st.columns(2)
    with col1:
        my_mbti = st.selectbox("내 MBTI", mbti_list, key="my_p")
    with col2:
        friend_mbti = st.selectbox("친구 MBTI", mbti_list, key="friend_p")
        
    if st.button("궁합 결과 분석하기 🔍"):
        match_score = (len(set(my_mbti) & set(friend_mbti)) * 25) + random.randint(10, 24)
        if match_score > 70:
            st.success(f"❤️ 궁합 지수: {match_score}% [환상의 멀티 듀오!]")
            st.write("서로 눈빛만 봐도 통하는 사이! '잇 테이크 투'나 '오버쿡' 같은 협동 멀티 게임을 당장 시작하세요.")
        elif match_score > 40:
            st.info(f"💛 궁합 지수: {match_score}% [평화로운 비즈니스 관계]")
            st.write("크게 싸우지는 않지만 각자 할 일 하는 '스타듀밸리 멀티' 같은 평화로운 경영 게임을 추천합니다.")
        else:
            st.error(f"☠️ 궁합 지수: {match_score}% [우정 파괴 경보 발령]")
            st.write("같이 피지컬 게임이나 마피아 게임을 하면 대판 싸울 수 있으니 평화로운 솔로 게임을 따로 하세요!")

with tab4:
    # 실시간 데이터 상태를 보여주는 종합 게시판 및 보관함 섹션
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("💬 실시간 유저 한줄평")
        new_review = st.text_input("한줄평 작성", placeholder="[INTJ] 체스 최고입니다... 입력 후 등록 클릭")
        if st.button("등록하기 🚀") and new_review:
            st.session_state.reviews.insert(0, new_review)
            st.rerun()
            
        st.write("---")
        for r in st.session_state.reviews[:5]:
            st.markdown(f"• {r}")
            
    with col_right:
        st.subheader("⭐ 내가 찜한 위시리스트")
        if st.session_state.wishlist:
            for w_game in st.session_state.wishlist:
                st.write(f"✅ {w_game}")
            if st.button("🗑️ 위시리스트 비우기"):
                st.session_state.wishlist = []
                st.rerun()
        else:
            st.caption("아직 찜한 게임이 없습니다. 1번 탭에서 게임을 찜해 보세요!")

# 사이드바 재미 요소
st.sidebar.subheader("🎲 오늘의 행운 픽")
if st.sidebar.button("랜덤 게임 뽑기"):
    all_g = [g['name'] for list_g in mbti_games.values() for g in list_g]
    st.sidebar.success(f"🎯 [{random.choice(all_g)}] 당첨!")
