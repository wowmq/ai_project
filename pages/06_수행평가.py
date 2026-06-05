import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="Masterpiece MBTI Game Recommender", page_icon="🎮", layout="centered")

st.title("🚀 MBTI 멀티버스 게임 매칭 플랫폼 🚀")
st.write("30문항 정밀 성향 테스트부터 친구 궁합, 나만의 위시리스트까지 포함된 수행평가 끝판왕 앱입니다! ✨")

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

# 30문제 정밀 테스트 질문 데이터 정의
questions = {
    "EI": [
        {"q": "게임할 때 디스코드 마이크를 켜고 왁자지껄 떠드는 게 좋다.", "a1": "그렇다 (E)", "a2": "아니다, 조용히 채팅이나 듣기만 하는 게 편하다 (I)"},
        {"q": "새로 오픈한 멀티서버에 가면 먼저 모르는 사람에게 말을 건다.", "a1": "쉽게 다가가 말을 건다 (E)", "a2": "누가 말을 걸기 전까지는 혼자 사냥한다 (I)"},
        {"q": "스마트폰 배터리가 5% 남았을 때 나는?", "a1": "친구들과 카톡을 하거나 전화를 하느라 다 쓴다 (E)", "a2": "조용히 이어폰을 끼고 혼자 유튜브를 본다 (I)"},
        {"q": "학교 쉬는 시간에 나는 보통 어디에 있나?", "a1": "다른 반 친구들을 만나러 가거나 복도에서 떠든다 (E)", "a2": "내 자리에 앉아서 폰을 보거나 엎드려 쉰다 (I)"},
        {"q": "주말에 집에만 있으면 어떤 기분이 드나?", "a1": "몸이 근질근질하고 답답해서 탈출하고 싶다 (E)", "a2": "세상 편안하고 충전되는 기분이다 (I)"},
        {"q": "처음 본 사람들과 보드게임을 할 때 나는?", "a1": "게임을 주도하며 분위기를 띄우려고 노력한다 (E)", "a2": "리액션을 잘해주며 묵묵히 내 순서를 기다린다 (I)"},
        {"q": "친구가 '오늘 슬픈 일 있어서 코인 노래방 갈래?' 하면 내 반응은?", "a1": "당장 옷 입고 나갈 준비를 한다 (E)", "a2": "위로는 해주고 싶지만 솔직히 나가기 귀찮다 (I)"},
        {"q": "과제를 할 때 소그룹 팀 과제와 개인 과제 중 선호하는 것은?", "a1": "다 같이 의견을 모으는 팀 과제 (E)", "a2": "나 혼자 알아서 끝내는 개인 과제 (I)"}
    ],
    "SN": [
        {"q": "마인크래프트를 할 때 내가 더 흥미를 느끼는 부분은?", "a1": "광질, 건축, 자동화 팩토리 등 정해진 시스템 구현 (S)", "a2": "새로운 모드 탐험, 세계관 상상, 숨겨진 이스터에그 찾기 (N)"},
        {"q": "게임 튜토리얼(설명서)이 나오면 어떻게 행동하나?", "a1": "정독하면서 기본 조작법을 정확하게 익힌다 (S)", "a2": "대충 넘기고 직접 부딪히면서 감으로 알아낸다 (N)"},
        {"q": "친구가 여행 다녀온 이야기를 할 때 내가 더 궁금한 것은?", "a1": "얼마 들었는지, 어디서 잤는지, 뭘 먹었는지 구체적인 사실 (S)", "a2": "어떤 느낌이었는지, 가서 무슨 생각을 했는지 분위기와 감상 (N)"},
        {"q": "노래를 들을 때 나에게 더 중요한 요소는?", "a1": "귀에 꽂히는 멜로디와 리듬 (S)", "a2": "가사에 담긴 심오한 의미나 스토리텔링 (N)"},
        {"q": "선생님이 '자유 주제로 프로그램을 만들어라'라고 하면 드는 생각은?", "a1": "범위가 너무 넓어서 막막하니 예시를 줬으면 좋겠다 (S)", "a2": "머릿속에 기발하고 특이한 아이디어가 마구 샘솟는다 (N)"},
        {"q": "사과라는 단어를 들으면 머릿속에 가장 먼저 떠오르는 것은?", "a1": "빨갛고 맛있는 과일 사과 (S)", "a2": "애플 스마트폰, 뉴턴의 사유, 스티브 잡스 등 연상 생각 (N)"},
        {"q": "영화나 드라마를 볼 때 나는 보통 어떤 스타일인가?", "a1": "화면 속 장면에 집중하며 스토리를 그대로 따라간다 (S)", "a2": "‘저기서 저 사람이 배신하겠네’라며 앞으로의 결말을 상상한다 (N)"}
    ],
    "TF": [
        {"q": "팀원이 내 게임 실수를 지적했을 때 내 마음은?", "a1": "내 실수가 맞는지 분석하고 피드백을 수용한다 (T)", "a2": "나를 무시하는 것 같아 말투나 감정에 서운함을 느낀다 (F)"},
        {"q": "친구가 '나 시험에서 떨어졌어...'라고 했을 때 나의 첫 마디는?", "a1": "몇 점 차이로? 무슨 과목이 어려웠어? (이유 분석) (T)", "a2": "아 진짜 속상하겠다.. 고생 많았는데 어떡해ㅠㅠ (공감) (F)"},
        {"q": "웹캠이나 마이크가 고장 났을 때 내가 먼저 하는 행동은?", "a1": "설정창을 열어 장치 드라이버나 하드웨어 선을 체크한다 (T)", "a2": "디코방 친구들에게 고장 났다고 찡찡거리며 하소연한다 (F)"},
        {"q": "영화가 엄청 슬프게 끝났을 때 내 반응은?", "a1": "스토리가 좀 억지스럽네라며 연출을 비평한다 (T)", "a2": "감정에 완전히 이입해서 눈물을 흘리거나 여운이 길게 남는다 (F)"},
        {"q": "친구가 머리를 이상하게 자르고 와서 '나 어때?'라고 물어본다면?", "a1": "솔직하게 앞머리가 너무 짧다고 말해준다 (T)", "a2": "상처받을까 봐 귀엽다며 어울린다고 거짓말해 준다 (F)"},
        {"q": "나에게 더 기분 좋은 칭찬은 어떤 쪽인가?", "a1": "너 진짜 똑똑하다, 코딩 기가 막히게 짜네! (능력 칭찬) (T)", "a2": "너랑 있으면 항상 마음이 편해, 진짜 착하다! (인성/감정 칭찬) (F)"},
        {"q": "조별 과제 중 한 명이 개인 사정으로 늦는다고 할 때 내 생각은?", "a1": "늦는 건 늦는 거고, 그 사람 점수를 깎아야 공평하다고 생각한다 (T)", "a2": "무슨 피치 못할 사정이 있겠지 하며 최대한 편의를 봐준다 (F)"}
    ],
    "JP": [
        {"q": "마인크래프트 야생을 시작하기 전 나의 행동은?", "a1": "좌표를 확인하고 기지 구역과 상자 정리 규칙을 먼저 정한다 (J)", "a2": "일단 도구만 만들고 발길이 닿는 대로 돌아다닌다 (P)"},
        {"q": "수행평가 마감일이 일주일 남았을 때 나는?", "a1": "하루에 얼만큼 할지 미리 계획을 세우고 미리 끝내둔다 (J)", "a2": "미루고 미루다가 마감 전날 밤새서 벼락치기로 끝낸다 (P)"},
        {"q": "내 컴퓨터 바탕화면의 상태는 어떤가?", "a1": "폴더별로 보기 좋고 깔끔하게 정리되어 있다 (J)", "a2": "아이콘과 다운로드 파일들이 무작위로 어지럽게 널려있다 (P)"},
        {"q": "친구와 약속을 잡을 때 선호하는 방식은?", "a1": "몇 시에 어디서 만나서 뭘 할지 명확히 정하는 것 (J)", "a2": "‘일단 주말에 홍대 쪽에서 보자!’ 하고 만나서 정하는 것 (P)"},
        {"q": "계획이 갑자기 틀어졌을 때(예: 가려던 식당이 문을 닫음) 나의 반응은?", "a1": "스트레스를 받고 멘탈이 살짝 흔들린다 (J)", "a2": "그럼 옆집 가지 뭐! 하고 아무렇지 않게 대안을 찾는다 (P)"},
        {"q": "여행을 갈 때 나는 짐을 어떻게 싸는가?", "a1": "필요한 물품 리스트를 적어서 며칠 전부터 꼼꼼히 챙긴다 (J)", "a2": "출발하기 직전이나 전날 밤에 눈에 보이는 대로 때려 넣는다 (P)"},
        {"q": "하루 일과가 정해진 루틴대로 흘러갈 때 나는 어떤가?", "a1": "안정감이 들고 통제하고 있다는 느낌에 뿌듯하다 (J)", "a2": "지루하고 답답해서 일탈을 하고 싶어진다 (P)"}
    ]
}

# 세션 상태 데이터 초기화
if "reviews" not in st.session_state:
    st.session_state.reviews = ["[ENFP] 폴가이즈 친구들이랑 하면 우정 파괴 꿀잼ㅋㅋㅋ", "[ISTJ] 스타듀밸리 계획대로 농사지으니 마음이 편안해집니다."]
if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

mbti_list = sorted(list(mbti_games.keys()))

# 탭 구성
tab1, tab2, tab3, tab4 = st.tabs(["🎮 게임 추천 및 찜하기", "📝 30문항 정밀 테스트", "👥 친구 게임 궁합", "💬 유저 게시판 & 위시리스트"])

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
            g_col1, g_col2 = st.columns([5, 1])
            with g_col1:
                st.markdown(f"**{idx+1}. {game['name']}** ({game['mode']})")
                st.caption(f"↳ {game['style']}")
            with g_col2:
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
    st.subheader("📝 30문항 정밀 MBTI 성향 테스트")
    st.write("총 30개의 질문에 솔직하게 답하면 가장 정확한 게임 성향 MBTI를 계산해 줍니다!")
    st.caption("※ 화면이 너무 길어지지 않게 단계별로 나누어 놓았으니 접힌 부분을 열어 풀어보세요.")
    
    # 정답을 누적할 딕셔너리 변수 생성
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    
    # 1과목: E vs I (8문항)
    with st.expander("🔵 1단계: 외향형(E) vs 내향형(I) 테스트 (8문항)", expanded=True):
        for idx, q_data in enumerate(questions["EI"]):
            choice = st.radio(f"Q{idx+1}. {q_data['q']}", [q_data['a1'], q_data['a2']], key=f"q_ei_{idx}")
            if "(E)" in choice: scores["E"] += 1
            else: scores["I"] += 1

    # 2과목: S vs N (7문항)
    with st.expander("🟢 2단계: 감각형(S) vs 직관형(N) 테스트 (7문항)"):
        for idx, q_data in enumerate(questions["SN"]):
            choice = st.radio(f"Q{idx+9}. {q_data['q']}", [q_data['a1'], q_data['a2']], key=f"q_sn_{idx}")
            if "(S)" in choice: scores["S"] += 1
            else: scores["N"] += 1

    # 3과목: T vs F (7문항)
    with st.expander("🟡 3단계: 사고형(T) vs 감정형(F) 테스트 (7문항)"):
        for idx, q_data in enumerate(questions["TF"]):
            choice = st.radio(f"Q{idx+16}. {q_data['q']}", [q_data['a1'], q_data['a2']], key=f"q_tf_{idx}")
            if "(T)" in choice: scores["T"] += 1
            else: scores["F"] += 1

    # 4과목: J vs P (7문항)
    with st.expander("🔴 4단계: 판단형(J) vs 인식형(P) 테스트 (7문항)"):
        for idx, q_data in enumerate(questions["JP"]):
            choice = st.radio(f"Q{idx+24}. {q_data['q']}", [q_data['a1'], q_data['a2']], key=f"q_jp_{idx}")
            if "(J)" in choice: scores["J"] += 1
            else: scores["P"] += 1

    st.write("---")
    # 결과 연산 버튼
    if st.button("📊 30문항 결과 정밀 분석하기"):
        # 다수결 알고리즘 연산
        res_ei = "E" if scores["E"] >= scores["I"] else "I"
        res_sn = "S" if scores["S"] >= scores["N"] else "N"
        res_tf = "T" if scores["T"] >= scores["F"] else "F"
        res_jp = "J" if scores["J"] >= scores["P"] else "P"
        
        final_result = res_ei + res_sn + res_tf + res_jp
        
        st.balloons()
        st.success(f"🎉 정밀 분석 완료! 당신의 성향 MBTI는 **[{final_result}]** 입니다!")
        st.markdown(f"👉 **[{final_result}] 유형 특징:** *{mbti_descriptions[final_result]}*")
        
        st.markdown(f"<h4>🎮 [{final_result}] 추천 대표 인생 게임 리스트</h4>", unsafe_allow_html=True)
        for g in mbti_games[final_result]:
            st.info(f"**{g['name']}** ({g['mode']})\n\n↳ {g['style']}")
            
        st.caption("💡 팁: 마음에 드는 게임은 첫 번째 탭에서 해당 MBTI를 선택 후 '⭐ 찜' 버튼을 눌러 위시리스트에 보관할 수 있습니다.")

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
