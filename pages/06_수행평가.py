import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="Gamer MBTI Game Recommender", page_icon="🎮", layout="centered")

st.title("🚀 MBTI 멀티버스 게임 매칭 플랫폼 🚀")
st.write("나의 성향을 예측할 수 없는 30문항 무작위 테스트! 내 진짜 인생 게임을 찾아보세요! ✨")

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

# 게임 데이터
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
    "ENTP": [{"name": "어mong 어스", "style": "화려한 말빨과 심리전의 마피아 게임", "mode": "멀티 전용"}, {"name": "문명 6", "style": "기발한 변수로 전 세계를 정복하는 전략", "mode": "솔로 (멀티 가능)"}, {"name": "플레이트 업", "style": "요리하고 동선을 개조하는 식당 로그라이크", "mode": "멀티 권장"}],
    "ESTJ": [{"name": "림월드", "style": "정착민들에게 효율적 업무를 배정 및 기지 관리", "mode": "솔로 전용"}, {"name": "트로피코 6", "style": "독재자가 되어 경제 구조를 꽉 잡는 경영", "mode": "솔로 (멀티 가능)"}, {"name": "플래닛 주", "style": "완벽한 통제로 맞추는 5성급 동물원 경영", "mode": "솔로 전용"}],
    "ESFJ": [{"name": "잇 테이크 투", "style": "서로 협력하지 않으면 못 깨는 레전드 협동", "mode": "멀티 전용 (2인)"}, {"name": "오버쿡", "style": "완벽한 역할 분담의 대환장 주방 대소동", "mode": "멀티 전용"}, {"name": "래프트 (Raft)", "style": "자원을 모아 뗏목을 키우는 해상 생존", "mode": "멀티 권장"}],
    "ENFJ": [{"name": "더 심즈 4", "style": "캐릭터들의 관계를 조율하는 시뮬레이션", "mode": "솔로 전용"}, {"name": "발더스 게이트 3", "style": "동료들의 마음을 이끌어 세상을 구하는 RPG", "mode": "솔로 (멀티 가능)"}, {"name": "테라리아", "style": "모험과 건설로 나만의 NPC 마을 채우기", "mode": "솔로 & 멀티 지원"}],
    "ENTJ": [{"name": "리그 오브 레전드", "style": "완벽한 오더와 전략적 판단으로 전장 지배", "mode": "멀티 전용"}, {"name": "프로스트펑크", "style": "단호한 결단력으로 인류 생존지를 이끄는 지도자", "mode": "솔로 전용"}, {"name": "스텔라리스", "style": "우주 제국의 지휘관이 되는 대형 스케일 전략", "mode": "솔로 (멀티 가능)"}]
}

# 원래 문장에서 학교/일상 단어만 게임 관련 상황으로 매끄럽게 수정
raw_questions = [
    # EI 관련 질문
    {"q": "게임할 때 디스코드 마이크를 켜고 왁자지껄 떠드는 게 좋다.", "a1": "그렇다", "a2": "아니다, 조용히 채팅이나 듣기만 하는 게 편하다", "val1": "E", "val2": "I"},
    {"q": "새로 오픈한 멀티서버에 가면 먼저 모르는 사람에게 말을 건다.", "a1": "쉽게 다가가 말을 건다", "a2": "누가 말을 걸기 전까지는 혼자 사냥한다", "val1": "E", "val2": "I"},
    {"q": "인게임 스마트폰이나 무전기 배터리가 5% 남았을 때 나는?", "a1": "팀원들과 브리핑을 하거나 수다를 떨며 다 쓴다", "a2": "조용히 볼륨을 낮추고 혼자 인게임 풍경을 보거나 쉰다", "val1": "E", "val2": "I"},
    {"q": "멀티서버 정비 시간(쉬는 시간)에 나는 보통 어디에 있나?", "a1": "다른 구역 유저들을 만나러 가거나 마을 광장에서 떠든다", "a2": "내 아지트에 앉아서 템창을 보거나 잠수(AFK)를 타며 쉰다", "val1": "E", "val2": "I"},
    {"q": "주말에 싱글룸(솔로 게임)에만 있으면 어떤 기분이 드나?", "a1": "몸이 근질근질하고 답답해서 대규모 멀티방으로 탈출하고 싶다", "a2": "세상 편안하고 영혼이 충전되는 기분이다", "val1": "E", "val2": "I"},
    {"q": "처음 본 유저들과 보드게임이나 미니게임을 할 때 나는?", "a1": "게임을 주도하며 채팅으로 분위기를 띄우려고 노력한다", "a2": "리액션을 잘해주며 묵묵히 내 플레이 순서를 기다린다", "val1": "E", "val2": "I"},
    {"q": "게임 친구가 '오늘 연패해서 슬픈데 코인 던전이나 한 판 돌래?' 하면 내 반응은?", "a1": "당장 캐릭터 접속해서 접속 대기를 한다", "a2": "위로는 해주고 싶지만 솔직히 다시 게임 켜기 귀찮다", "val1": "E", "val2": "I"},
    {"q": "인게임 퀘스트를 할 때 소그룹 팀 퀘스트와 개인 일일 퀘스트 중 선호하는 것은?", "a1": "다 같이 역할을 분담하는 팀 퀘스트", "a2": "나 혼자 알아서 끝내는 개인 퀘스트", "val1": "E", "val2": "I"},
    
    # SN 관련 질문
    {"q": "마인크래프트를 할 때 내가 더 흥미를 느끼는 부분은?", "a1": "광질, 건축, 자동화 팩토리 등 정해진 시스템 구현", "a2": "새로운 모드 탐험, 세계관 상상, 숨겨진 이스터에그 찾기", "val1": "S", "val2": "N"},
    {"q": "게임 튜토리얼(설명서)이 나오면 어떻게 행동하나?", "a1": "정독하면서 기본 조작법과 콤보를 정확하게 익힌다", "a2": "대충 넘기고 직접 보스랑 부딪히면서 감으로 알아낸다", "val1": "S", "val2": "N"},
    {"q": "친구가 새로 나온 신작 게임을 플레이한 이야기를 할 때 내가 더 궁금한 것은?", "a1": "정가가 얼마인지, 플탐이 몇 시간인지, 사양은 어떤지 구체적인 사실", "a2": "어떤 감성이었는지, 스토리가 어떤 메시지를 주는지 분위기와 감상", "val1": "S", "val2": "N"},
    {"q": "게임 배경음악(BGM)을 들을 때 나에게 더 중요한 요소는?", "a1": "귀에 꽂히는 신나는 멜로디와 타격감 있는 리듬", "a2": "음악에 담긴 심오한 게임의 서사나 스토리텔링", "val1": "S", "val2": "N"},
    {"q": "길드 마스터가 '자유 주제로 길드 이벤트를 기획해라'라고 하면 드는 생각은?", "a1": "범위가 너무 넓어서 막막하니 이전 이벤트 예시를 줬으면 좋겠다", "a2": "머릿속에 기발하고 특이한 미니게임 아이디어가 마구 샘솟는다", "val1": "S", "val2": "N"},
    {"q": "게임 속 '독사과'라는 아이템 단어를 들으면 머릿속에 가장 먼저 떠오르는 것은?", "a1": "체력을 깎거나 중독 상태이상을 일으키는 소모성 포션 아이템", "a2": "백설공주 스토리, 흑막 NPC의 음모, 히든 퀘스트 복선 등 연상 생각", "val1": "S", "val2": "N"},
    {"q": "스토리 중심의 갓겜 영화나 드라마(컷신)를 볼 때 나는 보통 어떤 스타일인가?", "a1": "화면 속 연출 장면에 집중하며 연출된 스토리를 그대로 따라간다", "a2": "‘저기서 저 NPC가 통수 치겠네’라며 앞으로의 히든 결말을 상상한다", "val1": "S", "val2": "N"},
    
    # TF 관련 질문
    {"q": "팀원이 내 인게임 실수를 지적했을 때 내 마음은?", "a1": "내 실수가 맞는지 로그를 분석하고 피드백을 수용한다", "a2": "나를 무시하는 것 같아 말투나 타이핑 감정에 서운함을 느낀다", "val1": "T", "val2": "F"},
    {"q": "친구가 '나 이번 승급전에서 떨어졌어...'라고 했을 때 나의 첫 마디는?", "a1": "몇 대 몇으로 졌어? 상대 조합이 뭐였는데?", "a2": "아 진짜 속상하겠다.. 고생 많았는데 어떡해ㅠㅠ", "val1": "T", "val2": "F"},
    {"q": "게임방 헤드셋이나 마이크가 고장 났을 때 내가 먼저 하는 행동은?", "a1": "오디오 설정창을 열어 제어판 장치나 하드웨어 연결 선을 체크한다", "a2": "인게임 채팅창에 고장 났다고 찡찡거리며 팀원들에게 하소연한다", "val1": "T", "val2": "F"},
    {"q": "게임 스토리가 엄청 슬픈 새드 엔딩으로 끝났을 때 내 반응은?", "a1": "스토리 개연성이 좀 억지스럽네라며 패치 밸런스를 비평한다", "a2": "캐릭터에 완전히 이입해서 눈물을 흘리거나 여운이 길게 남는다", "val1": "T", "val2": "F"},
    {"q": "친구가 룩덕 게임에서 캐릭터 룩을 이상하게 맞추고 와서 '나 어때?'라고 물어본다면?", "a1": "솔직하게 색 조합이 너무 언밸런스하다고 말해준다", "a2": "상처받을까 봐 유니크하고 어울린다고 칭찬해 준다", "val1": "T", "val2": "F"},
    {"q": "나에게 더 기분 좋은 인게임 칭찬은 어떤 쪽인가?", "a1": "너 진짜 대박이다, 플레이 피지컬 기가 막히게 짜네!", "a2": "너랑 게임하면 항상 마음이 편해, 진짜 매너 좋다!", "val1": "T", "val2": "F"},
    {"q": "길드 레이드 중 한 명이 개인 사정으로 트롤링이나 지각을 했을 때 내 생각은?", "a1": "실수는 실수고, 그 유저의 보상 분배를 깎아야 공평하다고 생각한다", "a2": "무슨 피치 못할 사정이 있겠지 하며 최대한 편의를 봐준다", "val1": "T", "val2": "F"},
    
    # JP 관련 질문
    {"q": "마인크래프트 야생을 시작하기 전 나의 행동은?", "a1": "좌표를 확인하고 기지 구역과 상자 정리 규칙을 먼저 정한다", "a2": "일단 도구만 만들고 발길이 닿는 대로 돌아다닌다", "val1": "J", "val2": "P"},
    {"q": "주간 한정 시즌 미션 마감일이 일주일 남았을 때 나는?", "a1": "하루에 얼만큼 채울지 계획을 세우고 프리미엄 보상을 미리 받아둔다", "a2": "미루고 미루다가 마감 전날 밤새서 벼락치기로 클리어한다", "val1": "J", "val2": "P"},
    {"q": "내 게임 내부 인벤토리나 창고 보관함의 상태는 어떤가?", "a1": "아이템 카테고리별로 보기 좋고 깔끔하게 정렬되어 있다", "a2": "아이콘과 장비, 잡템들이 무작위로 어지럽게 널려있다", "val1": "J", "val2": "P"},
    {"q": "팀원과 레이드 약속(공대 시간)을 잡을 때 선호하는 방식은?", "a1": "몇 시에 어느 채널에서 만나서 몇 판 돌지 명확히 정하는 것", "a2": "‘일단 주말 오후쯤에 접속하자!’ 하고 눈 맞으면 출발하는 것", "val1": "J", "val2": "P"},
    {"q": "오더나 빌드가 갑자기 틀어졌을 때(예: 가려던 사냥터에 보스가 이미 잡힘) 나의 반응은?", "a1": "스트레스를 받고 동선 계획이 깨져서 멘탈이 살짝 흔들린다", "a2": "그럼 옆 동네 던전 가지 뭐! 하고 아무렇지 않게 대안을 찾는다", "val1": "J", "val2": "P"},
    {"q": "보스 레이드를 갈 때 나는 소모품(포션 등) 짐을 어떻게 싸는가?", "a1": "필요한 버프 물품 리스트를 계산해서 출발 전에 꼼꼼히 챙긴다", "a2": "던전 입장하기 직전이나 매칭 잡힐 때 눈에 보이는 대로 상점에서 대충 산다", "val1": "J", "val2": "P"},
    {"q": "하루 플레이가 정해진 일일 숙제(일퀘) 루틴대로 흘러갈 때 나는 어떤가?", "a1": "안정감이 들고 스펙업을 완벽하게 제어하고 있다는 느낌에 뿌듯하다", "a2": "지루하고 답답해서 계획에 없던 위험한 던전으로 일탈을 하고 싶어진다", "val1": "J", "val2": "P"},
    {"q": "게임을 하다가 방종이나 취침 시간 등 마감 시간이 다가오면?", "a1": "지금 하던 판이나 퀘스트만 깔끔하게 딱 끝내고 정해진 시간에 컴퓨터를 종료한다", "a2": "“아 진짜 딱 한 판만 더!”를 외치며 질질 끌다가 결국 정해진 시간을 훌쩍 넘긴다", "val1": "J", "val2": "P"}
]

# [🔥 치트키 알고리즘] 최초 실행 시 한 번만 질문 순서를 완전히 섞어서 고정시킴
if "shuffled_questions" not in st.session_state:
    indexed_questions = list(enumerate(raw_questions))
    random.shuffle(indexed_questions)
    st.session_state.shuffled_questions = indexed_questions

# 세션 상태 변수 초기화
if "reviews" not in st.session_state:
    st.session_state.reviews = ["[ENFP] 친구들이랑 파티 애니멀즈 하다가 배 찢어지는 줄 알았음ㅋㅋㅋ", "[ISTJ] 팩토리오 자동화 라인 깔끔하게 정렬하니 마음이 편안합니다."]
if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

mbti_list = sorted(list(mbti_games.keys()))

# 탭 레이아웃
tab1, tab2, tab3, tab4 = st.tabs(["🎮 게임 추천 및 찜하기", "📝 게이머 성향 블라인드 테스트", "👥 친구 게임 궁합", "💬 유저 게시판 & 위시리스트"])

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
    st.subheader("📝 게이머 전용 30문항 블라인드 테스트")
    st.write("문항 순서와 정답 성향이 무작위로 완전히 뒤섞여 지표 예측이 불가능합니다. 내 진짜 게이밍 성향은 과연 무엇일까요?")
    st.caption("※ 모든 문항은 초기 미선택 상태로 나타납니다.")
    
    # 누적 스코어 딕셔너리
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    
    st.write("---")
    
    # 모든 문제를 다 풀었는지 체크하기 위한 리스트
    all_answered = True
    
    # 셔플된 게임 문항 순회 출력
    for display_idx, (original_idx, q_data) in enumerate(st.session_state.shuffled_questions):
        choice = st.radio(
            f"Q{display_idx+1}. {q_data['q']}", 
            [q_data['a1'], q_data['a2']], 
            index=None,  # 최초에 아무것도 선택되지 않도록 설정!
            key=f"gamer_q_{original_idx}"
        )
        
        # 유저가 선택했다면 스코어에 반영, 안 했다면 변수를 False로 변경
        if choice:
            if choice == q_data['a1']:
                scores[q_data['val1']] += 1
            else:
                scores[q_data['val2']] += 1
        else:
            all_answered = False  # 하나라도 누락되면 False가 됨
            
    st.write("---")
    
    # 결과 계산 및 히든 노출 버튼
    if st.button("📊 나의 게이머 MBTI 결과 확인하기"):
        if not all_answered:
            st.warning("⚠️ 아직 풀지 않은 문제가 있습니다! 30개의 모든 질문에 답한 뒤 결과를 확인해 주세요.")
        else:
            res_ei = "E" if scores["E"] >= scores["I"] else "I"
            res_sn = "S" if scores["S"] >= scores["N"] else "N"
            res_tf = "T" if scores["T"] >= scores["F"] else "F"
            res_jp = "J" if scores["J"] >= scores["P"] else "P"
            
            final_result = res_ei + res_sn + res_tf + res_jp
            
            st.balloons()
            st.success(f"🎉 분석 완료! 당신의 숨겨진 게이머 MBTI는 **[{final_result}]** 입니다!")
            st.markdown(f"👉 **[{final_result}] 유형 특징:** *{mbti_descriptions[final_result]}*")
            
            st.markdown(f"<h4>🎮 [{final_result}] 유형에게 최적화된 추천 인생 게임</h4>", unsafe_allow_html=True)
            for g in mbti_games[final_result]:
                st.info(f"**{g['name']}** ({g['mode']})\n\n↳ {g['style']}")
                
            st.caption("💡 팁: 결과가 마음에 든다면 '게임 추천 및 찜하기' 탭으로 이동해서 위시리스트에 담보세요.")

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
        new_review = st.text_input("한줄평 작성", placeholder="[INTJ] 슬레이 더 스파이어 뇌섹게임 강추합니다.")
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
with tab2:
    st.subheader("📝 게이머 전용 30문항 블라인드 테스트")
    st.write("문항 순서와 정답 성향이 무작위로 완전히 뒤섞여 지표 예측이 불가능합니다. 내 진짜 게이밍 성향은 과연 무엇일까요?")
    st.caption("※ 모든 문항은 실제 MBTI 설문지처럼 가로형으로 깔끔하게 정렬되며, 초기에는 아무것도 선택되지 않습니다.")
    
    # 누적 스코어 딕셔너리
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    
    st.write("---")
    
    # 모든 문제를 다 풀었는지 체크하기 위한 변수
    all_answered = True
    
    # 셔플된 게임 문항 순회 출력
    for display_idx, (original_idx, q_data) in enumerate(st.session_state.shuffled_questions):
        
        # 💡 깔끔한 설문지 느낌을 위해 질문 텍스트를 위쪽에 먼저 배치
        st.markdown(f"**Q{display_idx+1}. {q_data['q']}**")
        
        # 💡 보기 선택 컴포넌트 (horizontal=True를 추가하여 가로로 나란히 배치!)
        choice = st.radio(
            label=f"Q{display_idx+1}_label", # 화면에는 안 보이고 시스템 내부에서 식별할 레이블
            options=[q_data['a1'], q_data['a2']], 
            index=None,                      # 🔥 최초에 1번이 선택되어 있지 않고 깔끔하게 비어있도록 설정!
            horizontal=True,                 # 🔥 세로가 아닌 가로형 설문지 양식으로 보기 편하게 정렬!
            key=f"gamer_q_{original_idx}",
            label_visibility="collapsed"     # 중복 번호 표시 방지를 위해 라디오 내부 레이블은 숨김
        )
        st.write("") # 문항 사이 적당한 여백 추가
        
        # 유저가 선택했다면 스코어에 반영, 안 했다면 변수를 False로 변경
        if choice:
            if choice == q_data['a1']:
                scores[q_data['val1']] += 1
            else:
                scores[q_data['val2']] += 1
        else:
            all_answered = False  # 하나라도 누락되면 False가 됨
            
    st.write("---")
    
    # 결과 계산 및 히든 노출 버튼
    if st.button("📊 나의 게이머 MBTI 결과 확인하기"):
        if not all_answered:
            st.warning("⚠️ 아직 풀지 않은 문제가 있습니다! 30개의 모든 질문에 답한 뒤 결과를 확인해 주세요.")
        else:
            res_ei = "E" if scores["E"] >= scores["I"] else "I"
            res_sn = "S" if scores["S"] >= scores["N"] else "N"
            res_tf = "T" if scores["T"] >= scores["F"] else "F"
            res_jp = "J" if scores["J"] >= scores["P"] else "P"
            
            final_result = res_ei + res_sn + res_tf + res_jp
            
            st.balloons()
            st.success(f"🎉 분석 완료! 당신의 숨겨진 게이머 MBTI는 **[{final_result}]** 입니다!")
            st.markdown(f"👉 **[{final_result}] 유형 특징:** *{mbti_descriptions[final_result]}*")
            
            st.markdown(f"<h4>🎮 [{final_result}] 유형에게 최적화된 추천 인생 게임</h4>", unsafe_allow_html=True)
            for g in mbti_games[final_result]:
                st.info(f"**{g['name']}** ({g['mode']})\n\n↳ {g['style']}")
                
            st.caption("💡 팁: 결과가 마음에 든다면 '게임 추천 및 찜하기' 탭으로 이동해서 위시리스트에 담아보세요.")
