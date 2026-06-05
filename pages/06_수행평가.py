import streamlit as set_page_config
import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="Gamer MBTI Game Recommender", page_icon="🎮", layout="centered")

st.title("🚀 MBTI 멀티버스 게임 매칭 플랫폼 🚀")
st.write("질문부터 결과까지 100% 게임 친화형! 30문항 블라인드 테스트로 내 진짜 인생 게임을 찾아보세요! ✨")

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
    "ENTP": [{"name": "어몽 어스", "style": "화려한 말빨과 심리전의 마피아 게임", "mode": "멀티 전용"}, {"name": "문명 6", "style": "기발한 변수로 전 세계를 정복하는 전략", "mode": "솔로 (멀티 가능)"}, {"name": "플레이트 업", "style": "요리하고 동선을 개조하는 식당 로그라이크", "mode": "멀티 권장"}],
    "ESTJ": [{"name": "림월드", "style": "정착민들에게 효율적 업무를 배정 및 기지 관리", "mode": "솔로 전용"}, {"name": "트로피코 6", "style": "독재자가 되어 경제 구조를 꽉 잡는 경영", "mode": "솔로 (멀티 가능)"}, {"name": "플래닛 주", "style": "완벽한 통제로 맞추는 5성급 동물원 경영", "mode": "솔로 전용"}],
    "ESFJ": [{"name": "잇 테이크 투", "style": "서로 협력하지 않으면 못 깨는 레전드 협동", "mode": "멀티 전용 (2인)"}, {"name": "오버쿡", "style": "완벽한 역할 분담의 대환장 주방 대소동", "mode": "멀티 전용"}, {"name": "래프트 (Raft)", "style": "자원을 모아 뗏목을 키우는 해상 생존", "mode": "멀티 권장"}],
    "ENFJ": [{"name": "더 심즈 4", "style": "캐릭터들의 관계를 조율하는 시뮬레이션", "mode": "솔로 전용"}, {"name": "발더스 게이트 3", "style": "동료들의 마음을 이끌어 세상을 구하는 RPG", "mode": "솔로 (멀티 가능)"}, {"name": "테라리아", "style": "모험과 건설로 나만의 NPC 마을 채우기", "mode": "솔로 & 멀티 지원"}],
    "ENTJ": [{"name": "리그 오브 레전드", "style": "완벽한 오더와 전략적 판단으로 전장 지배", "mode": "멀티 전용"}, {"name": "프로스트펑크", "style": "단호한 결단력으로 인류 생존지를 이끄는 지도자", "mode": "솔로 전용"}, {"name": "스텔라리스", "style": "우주 제국의 지휘관이 되는 대형 스케일 전략", "mode": "솔로 (멀티 가능)"}]
}

# 30개 전체 질문 리스트 (100% 게임 기반 질문 구성)
raw_questions = [
    # EI 관련 게임 질문 (8개)
    {"q": "게임할 때 디스코드 음성 채널(마이크)을 켜고 시끌벅적하게 소통하는 편인가?", "a1": "그렇다. 마이크 켜고 브리핑하며 떠드는 게 재밌다.", "a2": "아니다. 듣기만 하거나 핑, 인게임 채팅으로만 소통하는 게 편하다.", "val1": "E", "val2": "I"},
    {"q": "새로 오픈한 대형 멀티 서버나 MMORPG에 처음 접속했을 때 나는?", "a1": "지나가는 유저들에게 말을 걸거나 빠르게 길드/클랜부터 가입한다.", "a2": "아무도 없는 한적한 사냥터를 찾아 혼자 조용히 레벨업을 시작한다.", "val1": "E", "val2": "I"},
    {"q": "게임 속 마을 광장에 유저들이 모여서 이벤트를 하거나 춤을 추고 있다면?", "a1": "나도 군중 속으로 들어가 같이 감정표현을 쓰며 축제를 즐긴다.", "a2": "‘다들 뭐하지?’ 생각하며 멀찍이 떨어져서 구경하거나 무시하고 갈 길 간다.", "val1": "E", "val2": "I"},
    {"q": "스쿼드(팀) 게임을 하려는데 같이 할 친구가 접속해 있지 않다면?", "a1": "공개 매칭(랜덤 큐)을 돌려서 모르는 사람들과도 바로 게임을 시작한다.", "a2": "솔로 모드로 바꾸거나, 혼자 할 수 있는 다른 싱글 게임을 켠다.", "val1": "E", "val2": "I"},
    {"q": "게임 속에서 정말 구하기 힘든 레어 아이템을 획득했을 때 나의 행동은?", "a1": "오픈채팅방, 커뮤니티, 혹은 친구들에게 단톡으로 바로 스샷을 보내 자랑한다.", "a2": "조용히 내 인벤토리를 열어보며 혼자 흐뭇해하고 만족한다.", "val1": "E", "val2": "I"},
    {"q": "주말에 약속 없이 하루 종일 집에서 모니터만 보며 게임을 달렸을 때 내 기분은?", "a1": "재밌긴 한데 몸이 좀 찌뿌둥하고 밖으로 나가서 바람을 쐬고 싶다.", "a2": "이보다 완벽한 주말은 없다! 영혼까지 완벽하게 충전된 기분이다.", "val1": "E", "val2": "I"},
    {"q": "친구들이 갑자기 '오늘 밤 10시 PC방 어택 가자!'라고 단톡방을 파면?", "a1": "무조건 콜! 당장 나갈 준비를 하고 설레는 마음으로 향한다.", "a2": "집에서 편하게 디코로 하자고 제안하거나, 나가지 않을 핑계를 고민한다.", "val1": "E", "val2": "I"},
    {"q": "게임 안에서 인맥을 쌓고 사람들과 소통하는 커뮤니티적 요소는 나에게?", "a1": "게임을 오래 지속하게 만드는 아주 중요한 원동력이다.", "a2": "가끔은 친목질이나 인간관계가 피곤하게 느껴져서 혼자가 편할 때가 많다.", "val1": "E", "val2": "I"},
    
    # SN 관련 게임 질문 (7개)
    {"q": "마인크래프트를 할 때 내가 더 진심으로 몰입하는 작업은?", "a1": "레드스톤 회로 설계, 자동화 공장 건설, 효율적인 광질 레이아웃 짜기", "a2": "모드팩 탐험, 숨겨진 이스터에그 발견, 나만의 독창적인 스토리나 세계관 상상하기", "val1": "S", "val2": "N"},
    {"q": "대작 오픈월드 게임을 새로 시작했는데 튜토리얼과 조작 가이드가 뜬다면?", "a1": "설명을 꼼꼼히 읽으며 기본 콤보나 시스템 메커니즘을 정확히 숙지한다.", "a2": "스킵(Skip)을 연타하거나 대충 넘기고, 직접 부딪히며 몸으로 체득한다.", "val1": "S", "val2": "N"},
    {"q": "새로운 게임 패치 노트가 공개되었을 때 내가 가장 주목하는 부분은?", "a1": "데미지 계수 버프/너프 수치, 버그 수정 내역 등 구체적이고 명확한 데이터", "a2": "새로운 에피소드 추가, 세계관 확장, 앞으로 전개될 떡밥과 연출 방향성", "val1": "S", "val2": "N"},
    {"q": "게임 그래픽이나 사운드를 감상할 때 내가 더 중요하게 생각하는 포인트는?", "a1": "렉이 없는 최적화 프레임, 사운드 플레이가 잘 되는 명확한 타격음", "a2": "게임의 몽환적인 픽셀 감성, 웅장하고 눈물 나는 배경음악(BGM)과 분위기", "val1": "S", "val2": "N"},
    {"q": "내가 만약 게임 개발자가 되어 나만의 자유 주제 게임을 기획한다면?", "a1": "기존에 검증된 장르(FPS, 타이쿤)의 시스템을 완벽하게 다듬은 웰메이드 게임", "a2": "지금껏 세상에 없던 독특한 규칙이나 심오한 철학적 메시지를 담은 예술적 게임", "val1": "S", "val2": "N"},
    {"q": "RPG 게임을 할 때 NPC들의 방대한 메인 스토리 대사나 스크립트를 마주하면?", "a1": "스토리는 핵심만 대충 보고, 내가 지금 깨야 하는 '퀘스트 목표와 보상'에 집중한다.", "a2": "소설책을 읽듯 세계관 대사를 정독하며, 이 인물의 숨겨진 과거 이야기를 상상한다.", "val1": "S", "val2": "N"},
    {"q": "미스터리나 추리 장르의 힌트를 얻었을 때 나는 어떤 방식으로 생각하나?", "a1": "화면에 제시된 단서와 오브젝트의 사실 관계를 있는 그대로 조합한다.", "a2": "‘혹시 이게 나중에 타임루프를 암시하는 복선 아닐까?’ 하며 거대한 음모론을 펼친다.", "val1": "S", "val2": "N"},
    
    # TF 관련 게임 질문 (7개)
    {"q": "팀 게임 중 아군 피드백 시간에 팀원이 내 치명적인 플레이 실수를 지적했다면?", "a1": "내 동선이나 스킬 분배가 잘못된 게 맞는지 팩트를 따져보고 수용한다.", "a2": "틀린 말은 아니지만, 많은 사람 앞에서 나를 탓하는 말투와 분위기에 서운함을 느낀다.", "val1": "T", "val2": "F"},
    {"q": "같이 게임하던 듀오 친구가 '아.. 요즘 슬럼프인가 게임 너무 안 되네' 하고 한숨을 쉬면?", "a1": "민감도 설정을 바꾸어 보라거나, 현재 메타 챔피언을 추천하며 솔루션을 준다.", "a2": "“에이 판수가 적어서 그래! 판수 박으면 올라감 화이팅!” 하며 텐션을 올려준다.", "val1": "T", "val2": "F"},
    {"q": "스토리 중심의 선택형 게임을 할 때, 비극적인 운명에 처한 동료를 살릴지 선택해야 한다면?", "a1": "동료를 살렸을 때와 버렸을 때의 보상 아이템 및 추후 스토리 효율을 계산한다.", "a2": "효율이 쓰레기여도 정든 동료를 배신할 수 없으니 무조건 감정에 이입해 살린다.", "val1": "T", "val2": "F"},
    {"q": "스토리 연출이 엄청 고조되어 게임 속 주인공이 눈물을 흘리며 엔딩을 맞이할 때 나의 반응은?", "a1": "“스토리 개연성이 좀 떨어지네”라며 연출력과 짜임새를 객관적으로 평가한다.", "a2": "내가 주인공이 된 것처럼 가슴이 먹먹해지고 여운이 남아 한동안 멍하니 있는다.", "val1": "T", "val2": "F"},
    {"q": "친구의 인게임 캐릭터 커스터마이징(룩덕질) 상태를 보았는데 내 기준에 너무 난해하고 이상하다면?", "a1": "“야 솔직히 색 조합 혼종이다ㅋㅋㅋ 리터칭 좀 해라” 하고 직구를 날린다.", "a2": "“오.. 되게 독특하다! 네 개성이 확실히 묻어나네!” 하고 상처받지 않게 돌려 말한다.", "val1": "T", "val2": "F"},
    {"q": "팀 매칭에서 만난 아군 유저에게 들었을 때 짜릿하고 더 기분 좋은 칭찬은?", "a1": "“와 님 피지컬 지리네요, 오더 지렸다 버스 달달합니다.” (플레이 능력 칭찬)", "a2": "“와 님 덕분에 멘탈 잡았어요, 진짜 친절하시네요 매너 유저 추!” (인성 및 매너 칭찬)", "val1": "T", "val2": "F"},
    {"q": "협동 경쟁 게임에서 조원이 개인 사정으로 약속된 대회가 가벼운 내전 시간에 지각했다면?", "a1": "사정이 어쨌든 다른 팀원들의 시간을 뺏은 것이니 벌칙이나 패널티를 줘야 한다고 생각한다.", "a2": "무슨 급한 일이 있었겠지 하고 걱정하며, 팀 분위기가 나빠지지 않게 다독인다.", "val1": "T", "val2": "F"},
    
    # JP 관련 게임 질문 (8개)
    {"q": "오픈월드 생존 야생 게임(생존 게임) 서버를 파서 본격적으로 시작하기 전 나의 행동은?", "a1": "자원 저장용 상자 배치 규칙, 기지 좌표 설정, 각자 맡을 역할 분담부터 짠다.", "a2": "일단 기본 도구만 대충 만들고 눈앞에 보이는 맵을 탐험하러 무작정 달려 나간다.", "val1": "J", "val2": "P"},
    {"q": "한 달 기간 한정 배틀패스나 이벤트 보상 미션이 새로 열렸을 때 나는?", "a1": "하루에 깨야 하는 미션 개수를 분배해서 마감일보다 여유 있게 미리 다 깨둔다.", "a2": "평소엔 신경 안 쓰고 막 하다가, 이벤트 종료 2~3일 전에 벼락치기로 밤새며 달린다.", "val1": "J", "val2": "P"},
    {"q": "내 인게임 인벤토리나 창고, 마이룸 보관함의 정리 상태는 어떠한가?", "a1": "소모품, 장비, 잡템이 종류별/등급별로 칼같이 정렬되어 칸이 맞춰져 있다.", "a2": "자동 정렬 버튼만 대충 누르거나, 빈 공간이 있는 창고에 일단 다 때려 박아 둔다.", "val1": "J", "val2": "P"},
    {"q": "친구와 주말에 같이 PC방에서 만나 게임을 하기로 약속을 잡을 때 선호하는 방식은?", "a1": "토요일 오후 2시 신촌 PC방에서 만나서 1부는 롤, 2부는 스팀 게임 하기로 정함.", "a2": "“주말 오후쯤에 대충 동네에서 접선하자! 만나서 뭐 할지 정하든가~”", "val1": "J", "val2": "P"},
    {"q": "경쟁 게임에서 내가 미리 시뮬레이션해 둔 밴픽이나 전략 큐가 상대 변수로 인해 완전히 꼬였다면?", "a1": "설계해 둔 판이 깨져서 순간적으로 멘탈이 흔들리고 극심한 스트레스를 받는다.", "a2": "“오히려 좋아, 임기응변 가보자!” 하고 즉흥적으로 다른 빌드를 올리며 즐긴다.", "val1": "J", "val2": "P"},
    {"q": "기대하던 신작 게임이 정식 출시된다는 소식을 들었을 때 나는?", "a1": "공식 홈페이지 가이드북이나 유튜브 트레일러를 보며 미리 직업 빌드를 공부해 둔다.", "a2": "아무 정보 없이 그냥 접속해서 커스터마이징부터 내 느낌대로 키우기 시작한다.", "val1": "J", "val2": "P"},
    {"q": "게임 플레이 타임(일과)이 정해진 스케줄이나 매일 도는 숙제(일일 퀘스트) 루틴대로 흘러갈 때?", "a1": "성장 가도가 안정적이고 알차게 채워지는 느낌이라 큰 보람을 느낀다.", "a2": "금방 지루해지고 기계적인 숙제처럼 느껴져서 금방 게임을 접고 싶어진다.", "val1": "J", "val2": "P"},
    {"q": "게임을 하다가 꺼야 하는 마감 시간(예: 취침 시간, 학원 갈 시간)이 다가오면?", "a1": "지금 하던 판이나 퀘스트만 깔끔하게 딱 끝내고 정해진 시간에 컴퓨터를 종료한다.", "a2": "“아 딱 한 판만 더!”를 외치며 질질 끌다가 결국 계획한 시간을 훌쩍 넘긴다.", "val1": "J", "val2": "P"}
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
    st.caption("※ 모든 문항은 순수한 게임 플레이 상황을 기반으로 제작되었습니다.")
    
    # 누적 스코어 딕셔너리
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    
    st.write("---")
    
    # 셔플된 게임 문항 순회 출력
    for display_idx, (original_idx, q_data) in enumerate(st.session_state.shuffled_questions):
        choice = st.radio(
            f"Q{display_idx+1}. {q_data['q']}", 
            [q_data['a1'], q_data['a2']], 
            key=f"gamer_q_{original_idx}"
        )
        if choice == q_data['a1']:
            scores[q_data['val1']] += 1
        else:
            scores[q_data['val2']] += 1
            
    st.write("---")
    
    # 결과 계산 및 히든 노출 버튼
    if st.button("📊 나의 게이머 MBTI 결과 확인하기"):
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
import streamlit as st
import random

# (앞부분 데이터 정의 및 tab1까지는 동일하므로 중복 생략, 바로 tab2 코드로 적용할 수 있게 구성)

with tab2:
    st.subheader("📝 게이머 전용 30문항 블라인드 테스트")
    st.write("문항 순서와 정답 성향이 무작위로 완전히 뒤섞여 지표 예측이 불가능합니다. 내 진짜 게이밍 성향은 과연 무엇일까요?")
    st.caption("※ 모든 문항은 순수한 게임 플레이 상황을 기반으로 제작되었습니다.")
    
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
            index=None,  # 🔥 [치트키] 최초에 아무것도 선택되지 않도록 설정!
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
        # 🔥 모든 문제를 풀었는지 검증하는 예외 처리 알고리즘
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
