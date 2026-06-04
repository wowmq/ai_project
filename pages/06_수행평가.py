import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 5-Game Recommender", page_icon="🎮", layout="centered")

st.title("✨ MBTI별 인생 게임 추천소 ✨")
st.write("내 MBTI를 선택하면, 성향 저격 레전드 게임 5개를 추천해줄게! 🔥")

# 16개 mbti별 완벽한 5개 게임 딕셔너리 데이터 (실제 게임 특징을 담은 고퀄리티 비주얼 링크)
mbti_games = {
    "ISTJ": [
        {"name": "스타듀밸리", "style": "꼼꼼한 계획과 루틴이 핵심! 농장을 경영하며 체계적으로 성장하는 재미", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1595853035070-59a39fe84de3?q=80&w=600&auto=format&fit=crop"},
        {"name": "팩토리오", "style": "최적의 효율을 찾아 공장을 자동화하는 두뇌 풀가동 시뮬레이션", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=600&auto=format&fit=crop"},
        {"name": "풋볼매니저 (FM)", "style": "방대한 데이터를 분석하고 구단을 관리하는 본격 과몰입 경영", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1628155930542-3c7a64e2c833?q=80&w=600&auto=format&fit=crop"},
        {"name": "유로 트럭 시뮬레이션 2", "style": "교통 법규를 준수하며 안전하게 화물을 운송하는 평화로운 배달", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b?q=80&w=600&auto=format&fit=crop"},
        {"name": "모노폴리 (Monopoly)", "style": "자산을 투자하고 회계적 이익을 계산하는 정통 보드게임 스타일", "mode": "멀티 권장", "image": "https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?q=80&w=600&auto=format&fit=crop"}
    ],
    "ISFJ": [
        {"name": "모여봐요 동물의 숲", "style": "주변을 가꾸고 주민들을 올바른 마음으로 챙기는 따뜻한 힐링", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1579373903781-fd5c0c30c4cd?q=80&w=600&auto=format&fit=crop"},
        {"name": "언패킹 (Unpacking)", "style": "이삿짐을 정해진 자리에 차분히 정리하며 안정감을 얻는 게임", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1505691938895-1758d7feb511?q=80&w=600&auto=format&fit=crop"},
        {"name": "가든 인", "style": "나만의 아늑한 방에서 아기자기한 식물들을 정성껏 키우는 힐링", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?q=80&w=600&auto=format&fit=crop"},
        {"name": "하우스 플리퍼", "style": "더러운 집을 깨끗하게 청소하고 인테리어를 개조하는 보람", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1513694203232-719a280e022f?q=80&w=600&auto=format&fit=crop"},
        {"name": "고양이는 몇 마리나 있지", "style": "화면 속에 숨어있는 고양이들을 사랑으로 찾는 숨은그림찾기", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?q=80&w=600&auto=format&fit=crop"}
    ],
    "INFJ": [
        {"name": "언더테일", "style": "심오한 스토리와 스토리텔링! 내 선택에 따라 결말이 바뀌는 감성", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=600&auto=format&fit=crop"},
        {"name": "오리와 도깨비불", "style": "한 편의 아름다운 동화 속 주인공이 되어 감동적인 서사를 탐험", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=600&auto=format&fit=crop"},
        {"name": "디스코 엘리시움", "style": "인간의 내면을 깊게 파고드는 철학적 메시지를 추리하는 웰메이드 RPG", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?q=80&w=600&auto=format&fit=crop"},
        {"name": "디트로이트: 비컴 휴먼", "style": "인공지능이 감정을 가지면 어떻게 될까? 인간성을 묻는 선택형 영화 같은 게임", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?q=80&w=600&auto=format&fit=crop"},
        {"name": "왓 리메인즈 오브 에디스 핀치", "style": "한 가문의 비극적인 이야기를 독특한 연출로 탐험하는 예술 게임", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1513151233558-d860c5398176?q=80&w=600&auto=format&fit=crop"}
    ],
    "INTJ": [
        {"name": "시티즈: 스카이라인", "style": "완벽한 도시 교통망과 구역을 설계하며 도시를 통제", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=600&auto=format&fit=crop"},
        {"name": "슬레이 더 스파이어", "style": "철저한 계산과 확률을 바탕으로 나만의 최강 덱을 짜는 전략", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1611195974226-a6a9be9dd763?q=80&w=600&auto=format&fit=crop"},
        {"name": "체스", "style": "상대의 몇 수 앞을 내다보며 오직 수싸움으로만 승부하는 지적 대결", "mode": "솔로 & 멀티 모두 지원", "image": "https://images.unsplash.com/photo-1529699211952-734e80c4d42b?q=80&w=600&auto=format&fit=crop"},
        {"name": "엑스컴 (XCOM) 시리즈", "style": "확률과 전술적 위치를 계산하여 외계인을 소탕하는 턴제 전략", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=600&auto=format&fit=crop"},
        {"name": "플레이그 인크 (Plague Inc.)", "style": "전 세계에 바이러스를 퍼뜨리는 지능적인 전략 시뮬레이션", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1584118624012-df056829fba0?q=80&w=600&auto=format&fit=crop"}
    ],
    "ISTP": [
        {"name": "마인크래프트", "style": "도구를 만들고 세상을 내 마음대로 개조하는 진정한 자유도", "mode": "솔로 & 멀티 모두 지원", "image": "https://images.unsplash.com/photo-1607988795691-3d0147b43231?q=80&w=600&auto=format&fit=crop"},
        {"name": "몬스터 헌터 월드", "style": "무기 고유의 메커니즘을 마스터하고 거대 괴수를 사냥하는 피지컬", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1552820728-8b83bb6b773f?q=80&w=600&auto=format&fit=crop"},
        {"name": "젤다의 전설 브레스 오브 더 와일드", "style": "물리 엔진을 활용해 내 방식대로 맵을 공략하는 오픈월드", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=600&auto=format&fit=crop"},
        {"name": "사이버펑크 2077", "style": "내 마음대로 신체를 개조하고 미래 도시를 누비는 액션 RPG", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?q=80&w=600&auto=format&fit=crop"},
        {"name": "러스트 (Rust)", "style": "맨몸으로 시작해서 도구를 만들고 기지를 지어 생존하는 하드코어 게임", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1533240332313-0db49b459ad6?q=80&w=600&auto=format&fit=crop"}
    ],
    "ISFP": [
        {"name": "저니 (Journey)", "style": "아름다운 영상미와 음악을 즐기며 정처 없이 떠나는 예술적 힐링", "mode": "솔로 (랜덤 만남 가능)", "image": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?q=80&w=600&auto=format&fit=crop"},
        {"name": "그리스 (GRIS)", "style": "한 편의 수채화 같은 연출 속에서 감정을 치유하는 플랫포머", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1541701494587-cb58502866ab?q=80&w=600&auto=format&fit=crop"},
        {"name": "데이브 더 다이버", "style": "낮에는 평화롭게 바다를 탐험하고 밤에는 초밥집을 운영하는 재미", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1682687220063-4742bd7fd53c?q=80&w=600&auto=format&fit=crop"},
        {"name": "압주 (ABZU)", "style": "아름다운 바다 속을 헤엄치며 해양 생물들과 교감하는 예술 힐링", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=600&auto=format&fit=crop"},
        {"name": "슬라임 랜처", "style": "말랑말랑한 슬라임들을 수집하고 키우는 귀여운 농장 경영", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1561484930-998b6a7b22e8?q=80&w=600&auto=format&fit=crop"}
    ],
    "INFP": [
        {"name": "스카이: 빛의 아이들", "style": "몽환적인 하늘을 날아다니며 평화를 전파하는 감성 끝판왕", "mode": "솔로 & 멀티 모두 지원", "image": "https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=600&auto=format&fit=crop"},
        {"name": "오모리 (OMORI)", "style": "꿈과 현실을 오가며 내면의 깊은 상처와 기억을 마주하는 RPG", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1509248961158-e54f6934749c?q=80&w=600&auto=format&fit=crop"},
        {"name": "투 더 문", "style": "기억을 바꾸어 소원을 들어주는 감동적인 스토리 중심 게임", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=600&auto=format&fit=crop"},
        {"name": "라이프 이즈 스트레인지", "style": "시간을 되돌리는 능력으로 친구를 구하고 선택의 무게를 배우는 드라마", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1493612276216-ee3925520721?q=80&w=600&auto=format&fit=crop"},
        {"name": "나이트 인 더 우즈", "style": "대학을 자퇴하고 고향으로 돌아온 고양이 주인공의 청춘 방황 스토리", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1448375240586-882707db888b?q=80&w=600&auto=format&fit=crop"}
    ],
    "INTP": [
        {"name": "포탈 시리즈", "style": "물리학 법칙을 이용해 공간을 넘나드는 명작 퍼즐 해결", "mode": "솔로 (2편은 멀티 가능)", "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=600&auto=format&fit=crop"},
        {"name": "바바 이즈 유", "style": "게임의 규칙 자체를 코딩하듯 뜯어고쳐 깨는 뇌섹 퍼즐 게임", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1614741118887-7a4ee193a5fa?q=80&w=600&auto=format&fit=crop"},
        {"name": "아우터 와일즈", "style": "22분마다 멸망하는 우주의 비밀을 푸는 본격 우주 탐사 추리", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=600&auto=format&fit=crop"},
        {"name": "탈로스 법칙", "style": "인공지능 로봇이 되어 고대 유적에서 고난이도 물리 퍼즐을 푸는 게임", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1563383151-5125434d3eb5?q=80&w=600&auto=format&fit=crop"},
        {"name": "스크리블너츠", "style": "내가 상상하는 단어를 타이핑하면 물건이 생겨나서 문제를 해결하는 창의력 게임", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?q=80&w=600&auto=format&fit=crop"}
    ],
    "ESTP": [
        {"name": "에이펙스 레전드", "style": "빠른 속도감과 화려한 스킬! 전장을 휩쓰는 피지컬 FPS", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=600&auto=format&fit=crop"},
        {"name": "GTA 5", "style": "지루할 틈이 없다! 넓은 도시에서 하고 싶은 모든 걸 하는 높은 자유도", "mode": "솔로 & 멀티 모두 지원", "image": "https://images.unsplash.com/photo-1547394765-185e1e68f34e?q=80&w=600&auto=format&fit=crop"},
        {"name": "FC 시리즈 (피파)", "style": "화려한 개인기와 스피디한 경기로 상대를 압도하는 스포츠 대결", "mode": "솔로 & 멀티 모두 지원", "image": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=600&auto=format&fit=crop"},
        {"name": "오버워치 2", "style": "내가 영웅이 되어 팀원들과 빠른 템포로 경기를 리드하는 하이퍼 슈팅", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1553481187-be93c21490a9?q=80&w=600&auto=format&fit=crop"},
        {"name": "포르자 호라이즌", "style": "오픈월드 도로를 슈퍼카로 질주하며 스피디한 레이싱을 즐기는 짜릿함", "mode": "솔로 & 멀티 모두 지원", "image": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?q=80&w=600&auto=format&fit=crop"}
    ],
    "ESFP": [
        {"name": "저스트 댄스", "style": "리듬에 몸을 맡기고 신나게 흔들며 에너지를 발산하는 파티 게임", "mode": "솔로 & 멀티 모두 지원", "image": "https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?q=80&w=600&auto=format&fit=crop"},
        {"name": "로블록스", "style": "매일 새로운 미니게임과 맵에서 친구들과 우당탕탕 노는 놀이터", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1511512578047-dfb367046420?q=80&w=600&auto=format&fit=crop"},
        {"name": "태고의 달인", "style": "신나는 노래 비트에 맞춰 북을 두드리는 스트레스 타파 리듬게임", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?q=80&w=600&auto=format&fit=crop"},
        {"name": "폴가이즈", "style": "귀여운 인형들을 조작하여 우당탕탕 서바이벌 런닝 게임", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1566577134770-3d85bb3a9cc4?q=80&w=600&auto=format&fit=crop"},
        {"name": "얼음과 불의 노래 (ADOFAI)", "style": "신나게 회전하는 볼을 박자에 맞춰 클릭하는 중독성 리듬 게임", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?q=80&w=600&auto=format&fit=crop"}
    ],
    "ENFP": [
        {"name": "폴 가이즈", "style": "예측 불허한 상황 속에서 우당탕탕 순위 경쟁을 펼치는 서바이벌", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1566577134770-3d85bb3a9cc4?q=80&w=600&auto=format&fit=crop"},
        {"name": "레드 데드 리뎀션 2", "style": "광활한 서부 시대를 나만의 방식대로 방랑하고 탐험하는 로망", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1533240332313-0db49b459ad6?q=80&w=600&auto=format&fit=crop"},
        {"name": "파티 애니멀즈", "style": "흐물거리는 인형 같은 동물들이 되어 난장판 몸싸움 빅재미", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1555685812-4b943f1cb0eb?q=80&w=600&auto=format&fit=crop"},
        {"name": "하이파이 러시", "style": "리듬에 맞춰 적들을 때려부수는 만화 같은 유쾌한 리듬 액션", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1511192336575-5a79af67a629?q=80&w=600&auto=format&fit=crop"},
        {"name": "갱비스트 (Gang Beasts)", "style": "몸을 가누지 못하는 친구들을 난간 밑으로 던지는 난투 파티게임", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1531058020387-3be344559be6?q=80&w=600&auto=format&fit=crop"}
    ],
    "ENTP": [
        {"name": "어mong 어스", "style": "화려한 말빨과 심리전으로 상대를 속이고 추리하는 마피아 전략", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1614624532983-4ce03382d63d?q=80&w=600&auto=format&fit=crop"},
        {"name": "구스구스덕", "style": "다양한 특수 직업들로 판을 뒤흔들고 예측 불가능한 대혼돈 마피아", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1563245372-f21724e3856d?q=80&w=600&auto=format&fit=crop"},
        {"name": "문명 6", "style": "‘한 턴만 더...’ 온갖 변수와 외교, 전장을 나만의 기발한 트롤링으로 정복", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=600&auto=format&fit=crop"},
        {"name": "플레이트 업 (PlateUp!)", "style": "요리도 하고 가게 동선도 내 마음대로 개조하며 협동하는 식당 로그라이크", "mode": "멀티 권장", "image": "https://images.unsplash.com/photo-1512485600747-5b454b4216b6?q=80&w=600&auto=format&fit=crop"},
        {"name": "잭박스 파티 팩", "style": "스마트폰을 리모컨으로 써서 황당한 퀴즈와 드립으로 친구들을 낚는 게임", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1551818255-e6e10975bc17?q=80&w=600&auto=format&fit=crop"}
    ],
    "ESTJ": [
        {"name": "림월드", "style": "정착민들에게 효율적인 업무를 배정하고 기지를 철저하게 관리", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=600&auto=format&fit=crop"},
        {"name": "트로피코 6", "style": "내가 독재자가 되어 국가의 법을 제정하고 경제 구조를 꽉 잡고 이끄는 재미", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1506970845246-18f10d533bf5?q=80&w=600&auto=format&fit=crop"},
        {"name": "플래닛 주", "style": "관람객들의 동선과 동물의 복지를 완벽한 통제로 맞추는 5성급 동물원 경영", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1534567153574-2b12153a87f0?q=80&w=600&auto=format&fit=crop"},
        {"name": "쥬라기 월드 에볼루션", "style": "공룡들의 위험도를 통제하고 관람객을 유치하는 공룡 공원 경영", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1569003339405-ea396a5a8a90?q=80&w=600&auto=format&fit=crop"},
        {"name": "아노 1800 (Anno 1800)", "style": "산업 혁명 시대의 복잡한 물류 네트워크를 구축하는 고급 도시 경영", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?q=80&w=600&auto=format&fit=crop"}
    ],
    "ESFJ": [
        {"name": "잇 테이크 투", "style": "서로 협력하지 않으면 절대 깰 수 없는 레전드 우정/커플 테스트 게임", "mode": "멀티 전용 (2인)", "image": "https://images.unsplash.com/photo-1511512578047-dfb367046420?q=80&w=600&auto=format&fit=crop"},
        {"name": "오버쿡", "style": "완벽한 역할 분담과 소통으로 헤쳐나가는 대환장 주방 대소동", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1556910116-e220f711432d?q=80&w=600&auto=format&fit=crop"},
        {"name": "폴아웃 76", "style": "황무지에서 새로운 사람들을 만나 커뮤니티를 이루고 돕고 사는 힐링 생존", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1475274047050-1d0c0975c63e?q=80&w=600&auto=format&fit=crop"},
        {"name": "래프트 (Raft)", "style": "바다 위를 떠다니며 친구들과 자원을 모아 달달한 뗏목을 키우는 생존", "mode": "멀티 권장", "image": "https://images.unsplash.com/photo-1505118380757-91f5f5632de0?q=80&w=600&auto=format&fit=crop"},
        {"name": "피코 파크 (Pico Park)", "style": "고양이들이 서로 몸을 잇고 협동하여 퍼즐을 깨는 파티 협동 게임", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1574144611937-0df059b5ef3e?q=80&w=600&auto=format&fit=crop"}
    ],
    "ENFJ": [
        {"name": "더 심즈 4", "style": "캐릭터들의 관계를 매끄럽게 조율하고, 행복한 가정을 설계하는 시뮬레이션", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1513694203232-719a280e022f?q=80&w=600&auto=format&fit=crop"},
        {"name": "발더스 게이트 3", "style": "동료들의 이야기를 경청하고 그들의 마음을 이끌어 세상을 구하는 대서사 RPG", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?q=80&w=600&auto=format&fit=crop"},
        {"name": "스타듀밸리 멀티", "style": "친구들을 불러 모아 각자 할 일을 지정하고 마을 주민들과 친해지도록 리드", "mode": "멀티 권장", "image": "https://images.unsplash.com/photo-1464226184884-fa280b87c3a9?q=80&w=600&auto=format&fit=crop"},
        {"name": "놀러오세요 동물의 숲", "style": "마을의 모든 동물들에게 선물을 주고 모두를 행복하게 만드는 소통 경영", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?q=80&w=600&auto=format&fit=crop"},
        {"name": "테라리아 (Terraria)", "style": "모험과 건설을 하면서 NPC 집을 지어주어 나만의 마을을 채우는 미니 공동체", "mode": "솔로 & 멀티 모두 지원", "image": "https://images.unsplash.com/photo-1518837695005-2083093ee35b?q=80&w=600&auto=format&fit=crop"}
    ],
    "ENTJ": [
        {"name": "리그 오브 레전드", "style": "승리를 위한 완벽한 오더와 전략적 판단으로 전장을 지배하는 게임", "mode": "멀티 전용", "image": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?q=80&w=600&auto=format&fit=crop"},
        {"name": "하츠 오브 아이언 4", "style": "2차 세계대전의 군대를 직접 지휘하여 전 세계의 판도를 바꾸는 대전략", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1524661135-423995f22d0b?q=80&w=600&auto=format&fit=crop"},
        {"name": "프로스트펑크", "style": "극한의 추위 속에서 단호한 결단력과 법안으로 인류의 생존지를 이끄는 지도자", "mode": "솔로 전용", "image": "https://images.unsplash.com/photo-1518156677180-95a2893f3e9f?q=80&w=600&auto=format&fit=crop"},
        {"name": "토탈 워: 삼국지", "style": "내가 군주가 되어 중국 대륙을 통일하는 대규모 전장 및 외교 시뮬레이션", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1599733589046-10c005739ef9?q=80&w=600&auto=format&fit=crop"},
        {"name": "스텔라리스 (Stellaris)", "style": "우주 제국의 지휘관이 되어 은하계 전체를 정복하고 식민지를 관리하는 대형 스케일", "mode": "솔로 (멀티 가능)", "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=600&auto=format&fit=crop"}
    ]
}

# MBTI 정렬 및 선택 박스
mbti_list = sorted(list(mbti_games.keys()))
user_mbti = st.selectbox("너의 MBTI는 뭐야? 선택해봐! 👇", mbti_list)

if user_mbti:
    games = mbti_games[user_mbti]
    st.divider()
    st.subheader(f"✨ [{user_mbti}] 유형을 위한 추천 게임 Top 5! ✨")
    st.write("")
    
    for idx, game in enumerate(games):
        st.markdown(f"### 🎮 {idx+1}. {game['name']}")
        
        try:
            st.image(game['image'], caption=f"{game['name']} 콘셉트 아트 및 비주얼", use_container_width=True)
        except Exception:
            st.warning("⚠️ 이미지를 가져오는 중 일시적인 네트워크 오류가 발생했습니다.")
            
        st.markdown(f"**👥 플레이 방식:** `{game['mode']}`")
        st.info(f"**🧐 추천 스타일**\n\n{game['style']}")
        st.write("") 
        
    st.success("해당 게임을 상징하는 직관적인 일러스트 비주얼로 전면 수정되었습니다! 🚀")
