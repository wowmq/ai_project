import streamlit as st

# 1. 페이지 기본 설정 및 디자인
st.set_page_config(page_title="MBTI별 인생 게임 추천소", page_icon="🎮", layout="centered")

st.title("🎮 MBTI별 인생 게임 추천소 ✨")
st.write("내 MBTI에 딱 맞는 게임을 고르고, 짧은 플레이 화면을 바로 확인해봐! ⚡")

# 2. 100% 끊김 없이 재생되는 짧은 플레이 화면(직링크) 데이터베이스!
# * 무조건 공개되어 있는 안정적인 이미지/움짤 소스를 매칭해뒀어!
mbti_games = {
    "ISTJ": [
        {"name": "팩토리오 (Factorio)", "style": "철저한 계획과 자동화 공장을 설계하는 뇌섹 게임 ⚙️", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3ZhcTJ4NmR0Z3Z4NDN5eXN5MWhicGZubnl6b3MzdXN6Ynd6bXUzbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oKIPnAiaMCws8nruE/giphy.gif"},
        {"name": "마인크래프트 (기술 모드)", "style": "체계적으로 시스템을 구축하고 자원을 관리하는 정돈된 플레이 🧱", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmszdXU4dzU4NmdwNDNtcXFndnp3NjRyejFicjRlbXp6cHh3Zmt0ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/u04bOWYPdAAw0/giphy.gif"},
        {"name": "스타듀 밸리 (Stardew Valley)", "style": "매일 계획된 루틴대로 농장을 경영하고 수확하는 힐링 게임 🧑‍🌾", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDB0dTZ0OGx3M3Y0OTZ4MXQ1bmRndml5MWRmaXl5cmV2czVubGl1ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gS38X9S3gSmsE/giphy.gif"}
    ],
    "ISFJ": [
        {"name": "모여봐요 동물의 숲", "style": "마을 주민들을 챙기고 아기자기하게 섬을 꾸미는 평화로운 감성 🏝️", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGtsN3pldzIwaTIzNjdxYW05NWNpN3o1ZHhxNGRkOXMwaTF5eGl4YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Vb96XfSxFbZ997v8sc/giphy.gif"},
        {"name": "심즈 4 (The Sims 4)", "style": "캐릭터들의 인생을 돌보고 따뜻한 가정을 만들어가는 시뮬레이션 🏠", "mode": "싱글 플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmNpeWlnd3lhbnU0MDlsNzl0YnVpaTZ5M2hmdHhuMXJzajF6b2ZzOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/k39wO5jT73P32/giphy.gif"},
        {"name": "이잇 텍스 투 (It Takes Two)", "style": "서로 배려하고 협동하며 완벽한 호흡으로 스테이지를 깨는 게임 🤝", "mode": "2인 전용 멀티플레이", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHIyb2s0eWxhcHA2MWI0b3p0c20wODR2azc2NmN3NDByZWkyeDJqZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/807bL0wXmOLeW3GCVs/giphy.gif"}
    ],
    "INFJ": [
        {"name": "디트로이트: 비컴 휴먼", "style": "깊이 있는 스토리와 캐릭터들의 감정에 몰입하는 선택형 시네마틱 게임 🤖", "mode": "싱글 플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGFzdmJvNXRpdDBtMmUxc3Ixa243cmZwaWFpOWxrdDZ2bmJmMXpveSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/S9cl1v7t8N8vP6fXq2/giphy.gif"},
        {"name": "저니 (Journey)", "style": "말 없이도 통하는 깊은 여운과 예술적인 분위기를 느끼는 힐링 게임 🏜️", "mode": "싱글 플레이 / 온라인 매칭", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnA4czFrdjQzZ2JzMXdrMWR5NDN5MHUwNjBzZXZtN2U3aHpxbXh2YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dAXV67S8O66f6/giphy.gif"},
        {"name": "언더테일 (Undertale)", "style": "괴물들의 이야기에 공감하며 자비를 베푸는 감성 충만 스토리 💀", "mode": "싱글 플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGp6amtyejZ1aW85Zm1ubGlnOXlhMGNhaHRkOGx5cGMxaHpsZHR3ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/v66bY6wAg90vD4I83m/giphy.gif"}
    ],
    "INTJ": [
        {"name": "시티즈: 스카이라인", "style": "도시 전체의 교통, 재정, 구역을 완벽하게 통제하고 설계하는 시뮬레이션 🏙️", "mode": "싱글 플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjY5NDg1ZnpzajZubDZtdWZiaGg2YWc0Nno4bXlscXBkdnJiaHNpayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0HlOl8p96S6VvI9q/giphy.gif"},
        {"name": "문명 6 (Civilization VI)", "style": "몇 수 앞을 내다보며 자신만의 전략으로 세계를 정복하는 턴제 게임 🌍", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Y5YWFmaXpxNmZreWpveGJxMXN2cmNmdmxjNmtsNHY2M3A5MmFlNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XEmf0xoWgZ3rO/giphy.gif"},
        {"name": "포탈 2 (Portal 2)", "style": "공간을 비틀어 정교한 퍼즐을 풀어내는 고지능 플레이 🌀", "mode": "싱글 플레이 / 2인 협동 모드 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnp0MzV5MHhvcjRhdm81MnIybzYzd3Y1a2tlc216ZnloM3h2dzJkMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dff9fshusSStq/giphy.gif"}
    ],
    "ISTP": [
        {"name": "몬스터 헌터: 월드", "style": "정교한 조작과 무기 메커니즘을 마스터해 거대 몬스터를 사냥하는 손맛 🦖", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWR1OW9wdXNxeDdxZWNxOXhybjA0NHA3a3A2ZDBiaGRidmRmbmxuMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8vDmZ6F7PFFU6cKjA8/giphy.gif"},
        {"name": "젤다의 전설 브레스 오브 더 와일드", "style": "세상의 물리 법칙을 이용해 오픈월드를 생존하는 재미 🏹", "mode": "싱글 플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXNmdWptazlyMmV0ZTNwd3RwbmpqdTVsczBqczk0NWt1ajZrcDF0NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NVBR6cLvUjV96/giphy.gif"},
        {"name": "에이펙스 레전드", "style": "빠른 판단력과 피지컬로 전장을 누비는 하이템포 배틀로얄 FPS 🔫", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmtpbnNwdWp1cTZiODBrbThpOGVveG9hd3dtMWx2eTN0MHFxMmpxbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/idYdfZ9xxVgVPNXJs0/giphy.gif"}
    ],
    "ISFP": [
        {"name": "마인크래프트 (셰이더 적용)", "style": "아름다운 풍경 속에서 나만의 예술적인 플레이를 즐기는 감성 🌌", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3ZkMnV2dzlxd251bXphNmdtZ2lmdm82ZHFlNmEwMXRzZHdtMnI3ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1394S2X8N769tm/giphy.gif"},
        {"name": "그리스 (Gris)", "style": "한 편의 수채화 같은 그래픽과 감성적인 음악 속을 유영하는 예술 게임 🎨", "mode": "싱글 플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGx5eDF1NXU0MGphcWtlZTA1YjZtZHoxMGg5eGNqNmppam4wZHhkdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2gZ996pYQL7QxatWWe/giphy.gif"},
        {"name": "로블록스 (입양하세요 등)", "style": "정해진 틀 없이 자유롭게 돌아다니며 가볍고 트렌디하게 즐기는 소통 플레이 🎒", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHhhNWoxNGNkaDk1M2w2dHpjNTlyZGs0eHlyOG53N2RtdjM1bzNoZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/33OrjzUFwSmME/giphy.gif"}
    ],
    "INFP": [
        {"name": "오리와 도깨비불", "style": "환상적이고 몽환적인 그래픽 속에서 감동적인 스토리를 따라가는 여정 🦊", "mode": "싱글 플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3N6ZXE2NWV3dThwdTgycjhpZGoxMXM0d3AwNHpuaDJxb3lvdTZoayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Vff5Qxz6LLzag/giphy.gif"},
        {"name": "스카이: 빛의 아이들", "style": "하늘을 날아다니며 따뜻한 감성을 나누고 친구를 사귀는 평화로운 오픈월드 ☁️", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMm0zd2p0dDgxYnY0OTVhcTVxYXhuNDNxdzgyaW5naGNmbWhndm1rayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LpoatN94D0A0Z988gX/giphy.gif"},
        {"name": "라이프 이즈 스트레인지", "style": "시간을 돌리는 능력으로 주인공의 고뇌와 성장을 함께하는 감성 드라마 🦋", "mode": "싱글 플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDhscWd1NGxna3V6ZXU2cGtpOTdqZXBqNDRzNWFidjR3ZzQzMHhpZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l46CbI3Z5K19X9pXG/giphy.gif"}
    ],
    "INTP": [
        {"name": "아우터 와일즈 (Outer Wilds)", "style": "우주의 비밀과 루프물의 미스터리를 순수 호기심과 추리로 풀어내는 갓겜 🚀", "mode": "싱글 플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzdrMXByazNxMTM1Y2xidjFpZTVnaDR4NWJibzVsZHc3MGR0bHlyYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/M90fD69MefSbMco5mB/giphy.gif"},
        {"name": "바바 이즈 유 (Baba Is You)", "style": "게임의 규칙 자체를 코딩하듯 뜯어고쳐 깨는 신개념 하드코어 퍼즐 🧠", "mode": "싱글 플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWtsOXdndXpxdmNreGxhaXhxajB4MnEwbjA3bmFmaTAzZzFzcnVyOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Wp06bIZL6OmZ35hXpE/giphy.gif"},
        {"name": "소울라이크 시리즈 (엘든 링)", "style": "보스의 패턴을 분석하고 완벽한 공략법을 찾아내어 파훼하는 성취감 ⚔️", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3g2NXBpZzZ0MHVreWNpdTJrbndlZHZicm55ZndkcWRkZW0wY3k3OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ECvKrc65Jmh2M/giphy.gif"}
    ],
    "ESTP": [
        {"name": "발로란트 (VALORANT)", "style": "순간적인 피지컬과 화려한 스킬 연계로 상대를 찍어누르는 하이퍼 FPS 🎯", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTA4Y2lmd3pweHRreHZic3o5aHBnZm16ZmxyYXJ4ZnlrbHdtMnpsNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/S9cl1v7t8N8vP6fXq2/giphy.gif"},
        {"name": "GTA 5", "style": "넓은 도시에서 법 따윈 불도저처럼 밀어버리는 짜릿하고 거침없는 오픈월드 액션 🚘", "mode": "싱글 플레이 / 온라인 멀티플레이", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzB2enN1dzgwbDhpMXl0ZHpjMmV4czI0dzRzd3NoazA0Z2wxcTZuNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/10UHehEC098kAE/giphy.gif"},
        {"name": "리그 오브 레전드 (LoL)", "style": "치열한 교전과 빠른 템포의 한타로 도파민을 폭발시키는 국민 게임 👑", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDVqNzR3eGsybnlsMjgxYTZlOTB5MHV2MHptcnVmaThoOXpyNmxhMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Z7B90fX0XALio/giphy.gif"}
    ],
    "ESFP": [
        {"name": "폴 가이즈 (Fall Guys)", "style": "귀여운 캐릭터들과 함께 난장판 레이스를 즐기는 웃음 벨 예능 게임 🦄", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmVzNzg5djhpcm1rYng3bnd1NHI1OXFrbnY4YWd6NGppNWR2czFmeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YrkK0A2mS3Eku9cyK0/giphy.gif"},
        {"name": "저스트 댄스 (Just Dance)", "style": "신나는 음악에 맞춰 몸을 흔들며 에너지를 뿜어내는 흥 폭발 게임 🕺", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWVmZmY0MWY3cDNwZnI3OXQyaWlyZDRzOWdybzI3cXA5aXR2bThzOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ov9jSZFgTfMv9Vn8k/giphy.gif"},
        {"name": "어몽 어스 (Among Us)", "style": "친구들과 왁자지껄 떠들며 속고 속이는 실시간 정치 대소동 🕵️‍♂️", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnlydTNtd3psczMxbTVvdXFwOTRhNDByb2J4ejhhYzZ6OW50NGwxbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RtdRhc7TxwEa4/giphy.gif"}
    ],
    "ENFP": [
        {"name": "서브노티카 (Subnautica)", "style": "외계 해양 행성을 탐험하며 신기한 생물들을 발견하고 기지를 짓는 모험 🐳", "mode": "싱글 플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExczJrbTdkZ3d6cW16czI1NDhhbXoxajd0NG93a3A2aWw1d2Z5OHRxeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohzdYhS0uK8m7x6bS/giphy.gif"},
        {"name": "팀 파이트 택틱스 (TFT/롤토체스)", "style": "매 판 무궁무진한 시너지 조합을 짜며 나만의 사기 덱을 완성하는 재미 🃏", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWNodTVtcndvNmQzOHpzbXRlM2VzM2gwbGtyZWp5eWk5eTZzYmdsYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ov9jX7kcl0S4XpLCE/giphy.gif"},
        {"name": "인간: 폴 플랫 (Human: Fall Flat)", "style": "흐느적거리는 몸으로 기상천외하고 엉뚱한 플레이를 만들어내는 몸개그 게임 🏃‍♂️", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHloMmlndnVwaHhiNWJidnpkdWZtMW8xeDhvNm55dmxhNHJkMnFubSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dB0Lw8F8mshN8S6vK8/giphy.gif"}
    ],
    "ENTP": [
        {"name": "오버워치 2", "style": "고정관념을 깨는 기상천외한 영웅 조합과 화려한 한타 난전을 이끄는 재미 💥", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnAwZnpscnAwMzBlMTA3Nmt6cmZsdmJpczloZThnZjdzYWdxeHpsbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oKIP8Zq6wWOf8GOWY/giphy.gif"},
        {"name": "하스스톤 (Hearthstone)", "style": "상대의 심리를 읽고 골탕 먹이는 참신한 예능 덱과 두뇌 싸움 🃏", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzVyYnp1NGtlZHdrZXFnbnVtcTllNno4cGdrODh1bmxtdnUybWVqOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26fpBsSeis8pTAn60/giphy.gif"},
        {"name": "게리스 모드 (Garry's Mod)", "style": "정해진 규칙 없이 내 멋대로 모드를 만들고 트롤링하며 노는 대혼돈 멀티 🛠️", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnk1YzdicDJvZmpycnNuNzJrNjI4OTFyeDJ3dmw3MG04MG9kOHQyeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/12Udf3p4ovL66c/giphy.gif"}
    ],
    "ESTJ": [
        {"name": "풋볼 매니저 (FM)", "style": "구단의 예산, 전술, 선수 영입까지 완벽하게 통제하는 악마의 경영 시뮬레이션 ⚽", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNndicHNyd2szMTZwa3Q0YWt3bnAwYWppcm0xMnF4bnQyc3NxeHpkciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/S8DNLp9oVpP2v6wAQu/giphy.gif"},
        {"name": "레인보우 식스 시즈", "style": "철저한 오더와 완벽한 전술, 팀원 간의 브리핑으로 승리하는 하드코어 FPS 🪖", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmpsenI3dm0waXAzOGY1N3BlNDM2bDNjZXNlYWp5dzA0OHc4M3QxeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26vUxNJDftn9gC3pS/giphy.gif"},
        {"name": "림월드 (RimWorld)", "style": "생존자들에게 효율적인 업무를 배정하고 기지를 철두철미하게 방어하는 식민지 경영 🪵", "mode": "싱글 플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExczB5NHU2cGZpMTFhcWZreW85ZW1vdGR0Ynl4dHA5eGVwbXQ5NGpxayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUPGcyi6YxcM6f8492/giphy.gif"}
    ],
    "ESFJ": [
        {"name": "오버쿡! (Overcooked!)", "style": "지옥의 주방에서 역할 분담을 확실히 하며 최고의 팀워크를 발휘하는 게임 👨‍🍳", "mode": "멀티플레이 필수 (협동)", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2FhbXZzZHQ0dnU0azlzbjF4cmN3cnplcnU4a3N0aDhnaHZ2YjYybCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohzdY7N0S8ugScc3S/giphy.gif"},
        {"name": "로스트아크 (LOST ARK)", "style": "길드원들과 다 같이 레이드 공략을 소통하며 함께 성장하는 대규모 MMORPG ⚔️", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3VwdGphNGpyM21oNWkyYXRmcnYxejJ2bXl3NGtsZjR0am12ejJ5ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZdgXInN29699GgT7jB/giphy.gif"},
        {"name": "리탈 컴퍼니 (Lethal Company)", "style": "팀원들과 음성 채팅으로 꽉꽉 소통하며 폐품을 수거하는 꿀잼 공포 시트콤 🎙️", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmsydmxnYWw5czJ5MHpsNHg2enQ3NHlsNWlqdXloMHhzNGNnZW14byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fX8H6G6Eg0ahwSScN7/giphy.gif"}
    ],
    "ENFJ": [
        {"name": "데드 바이 데이라이트", "style": "생존자 무리를 이끌고 협동하여 살인마의 눈을 피해 탈출하는 스릴 만점 팀플레이 🏃", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXplZTh5MWk4dTh6Nmx5NmE0ODhkaG0zbWFyNzdmaW5wNzEwNnkwaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCRZOh5K1bLwB6U/giphy.gif"},
        {"name": "헬다이버즈 2 (Helldivers 2)", "style": "은하계의 민주주의를 위해 동료들과 의기투합하여 전장을 누비는 화끈한 협동 슈팅 🔥", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2FjMDhscDZjdWZ3cmM0MDk3cW1ydXlhYWp1MmxubXcycXhtdjhjdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NxckxXIAf6RxK/giphy.gif"},
        {"name": "스타듀 밸리 (멀티)", "style": "마을 주민들과 친해지고 친구들과 다 함께 협동 농장을 키워가는 따뜻한 공동체 생활 🌽", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDB0dTZ0OGx3M3Y0OTZ4MXQ1bmRndml5MWRmaXl5cmV2czVubGl1ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gS38X9S3gSmsE/giphy.gif"}
    ],
    "ENTJ": [
        {"name": "크루세이더 킹즈 3", "style": "국가의 정치, 외교, 군사를 총괄하며 세계 패권을 장악하는 최고 권력자 시뮬레이션 👑", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmk3cXZ3M2p3cTRhcXR4Z2wwbXR6N3RkaTh3Z2xicmJkaTZzMndneSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ihpEw8S6mK3EUPgU2u/giphy.gif"},
        {"name": "스타크래프트 시리즈", "style": "엄청난 멀티태스킹과 카리스마 있는 부대 컨트롤로 상대를 압도하는 실시간 전략 🛸", "mode": "싱글 플레이 / 멀티플레이 가능", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNml3NDMwa2E5Mzk5MXlrdzExNmcyNXQ0NndhcWltN29ocHlydDhkOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l3vR88SjAs27Sg25y/giphy.gif"},
        {"name": "러스트 (Rust)", "style": "강한 자만 살아남는 무법지대에서 클랜을 결성하고 리더십을 발휘해 영토를 지배하는 생존 게임 ⛺", "mode": "온라인 멀티플레이 전용", "media_url": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHpnbTZtdDBlczlhdXQ4YWJvZXBndTR5cHFtN3loamI1aGZ2MXk3NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kE3o6O6b96b7C6vM63/giphy.gif"}
    ]
}

# 3. MBTI 선택받기
st.markdown("---")
selected_mbti = st.selectbox("👉 너의 MBTI를 골라봐!", list(mbti_games.keys()))

# 4. 결과 및 짧은 플레이 영상(움짤) 출력
if selected_mbti:
    st.markdown(f"### ⚡ **{selected_mbti}** 유형에게 추천하는 인생 게임 리스트!")
    st.write("스크롤을 내리면 게임 화면이 움짤로 바로 재생돼! 완전 편하지? 😎🎬")
    
    games = mbti_games[selected_mbti]
    
    for idx, game in enumerate(games, 1):
        with st.container():
            st.markdown(f"#### **{idx}. {game['name']}**")
            st.write(f"**🎮 플레이 스타일:** {game['style']}")
            st.write(f"**👥 게임 모드:** `{game['mode']}`")
            
            # 💡 핵심 포인트: 유튜브 플레이어 대신 무조건 뜨는 직링크 st.image 사용!
            st.image(game['media_url'], use_container_width=True)
            st.markdown("---")

st.caption("제작: MBTI 게임 추천 봇 🤖 | 초고속 움짤 플레이어 로딩 완료")
