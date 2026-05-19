<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>한국 관광지 안내 지도</title>
    <style>
        body {
            font-family: 'Malgun Gothic', dotum, sans-serif;
            margin: 20px;
            background-color: #f9f9f9;
        }
        h2 {
            color: #333;
        }
        /* 1. 지도 크기를 60%로 조절 (너비 기준) */
        #map-container {
            width: 60%; 
            height: 450px;
            margin-bottom: 20px;
            border: 2px solid #ccc;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        #map {
            width: 100%;
            height: 100%;
        }
        /* 2. 관광지 선택 리스트 스타일 */
        .attraction-list {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
        }
        .attraction-btn {
            padding: 10px 15px;
            background-color: #fff;
            border: 1px solid #007bff;
            color: #007bff;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
        }
        .attraction-btn:hover, .attraction-btn.active {
            background-color: #007bff;
            color: #fff;
        }
        /* 설명창 스타일 (3~4줄 구체적 설명) */
        #description-box {
            width: 60%;
            padding: 15px;
            background-color: #e9f5ff;
            border-left: 5px solid #007bff;
            border-radius: 4px;
            min-height: 80px;
            line-height: 1.6;
            color: #444;
        }
        .info-title {
            font-size: 1.1em;
            font-weight: bold;
            color: #0056b3;
            margin-bottom: 5px;
        }
    </style>
</head>
<body>

    <h2>한국의 주요 관광지 (60% 축소 지도)</h2>
    
    <!-- 지도 영역 -->
    <div id="map-container">
        <div id="map"></div>
    </div>

    <!-- 2. 지도 밑 관광지 10개 선택 버튼 -->
    <div class="attraction-list">
        <button class="attraction-btn" onclick="selectAttraction(0)">경복궁</button>
        <button class="attraction-btn" onclick="selectAttraction(1)">N서울타워</button>
        <button class="attraction-btn" onclick="selectAttraction(2)">해운대해수욕장</button>
        <button class="attraction-btn" onclick="selectAttraction(3)">제주 성산일출봉</button>
        <button class="attraction-btn" onclick="selectAttraction(4)">불국사</button>
        <button class="attraction-btn" onclick="selectAttraction(5)">전주 한옥마을</button>
        <button class="attraction-btn" onclick="selectAttraction(6)">남이섬</button>
        <button class="attraction-btn" onclick="selectAttraction(7)">여수 낭만포차</button>
        <button class="attraction-btn" onclick="selectAttraction(8)">수원 화성</button>
        <button class="attraction-btn" onclick="selectAttraction(9)">부산 감천문화마을</button>
    </div>

    <!-- 2. 전철역 및 놀거리 구체적 설명창 -->
    <div id="description-box">
        <div class="info-title">관광지를 선택해 주세요.</div>
        지정된 관광지를 클릭하시면 가장 가까운 전철역 정보와 주변의 구체적인 즐길 거리가 이곳에 3~4줄로 상세하게 표시됩니다.
    </div>

    <!-- 1. 구글 지도 API 로드 (language=ko 설정을 통해 한국말로 나오게 처리) -->
    <!-- 'YOUR_API_KEY' 부분을 본인의 실제 구글 맵 API 키로 변경하셔야 지도가 정상 작동합니다. -->
    <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&language=ko&callback=initMap" async defer></script>

    <script>
        let map;
        let activeMarker = null;

        // 관광지 10개 데이터 (좌표, 이름, 전철역 및 3~4줄 놀거리 상세 설명)
        const attractions = [
            {
                name: "경복궁",
                lat: 37.5796, lng: 126.9770,
                desc: "<b>가장 가까운 역:</b> 3호선 경복궁역 5번 출구와 바로 연결됩니다.<br>궁궐 내부를 거닐며 근정전과 경회루의 아름다운 조선 건축미를 감상할 수 있습니다. 주변 한복 대여점에서 한복을 입고 입장하면 무료 관람이 가능해 특별한 사진을 남기기 좋습니다. 관람 후에는 인근 삼청동 카페거리나 서촌마을에서 아기자기한 소품숍을 구경하고 맛집 탐방을 즐길 수 있습니다."
            },
            {
                name: "N서울타워",
                lat: 37.5511, lng: 126.9882,
                desc: "<b>가장 가까운 역:</b> 4호선 명동역 3번 출구에서 도보 이동 후 케이블카 이용.<br>남산 정상에 위치하여 서울 시내 전체를 한눈에 내려다볼 수 있는 탁 트인 전망을 자랑합니다. 타워 타워 플라자 주변 펜스에 사랑의 자물쇠를 걸며 소중한 추억을 기록하는 연인들의 필수 코스입니다. 해가 진 후에는 화려하게 빛나는 서울의 야경을 감상하고 대중교통이나 도보 순환로를 통해 명동으로 내려와 야시장을 즐기기 좋습니다."
            },
            {
                name: "해운대해수욕장",
                lat: 35.1587, lng: 129.1603,
                desc: "<b>가장 가까운 역:</b> 부산 2호선 해운대역 3번, 5번 출구에서 도보 5분.<br>넓은 백사장과 푸른 바다가 펼쳐져 있으며 여름철 해수욕뿐만 아니라 사계절 내내 버스킹 공연이 열려 활기찬 분위기입니다. 주변의 '미포철길' 해변열차나 스카이캡슐을 타고 해안 절경을 감상하는 이색 체험이 인기를 끌고 있습니다. 저녁에는 해운대 전통시장에서 꼼장어와 떡볶이 등 로컬 음식을 맛보거나 더베이101에서 세련된 마천루 야경을 즐길 수 있습니다."
            },
            {
                name: "제주 성산일출봉",
                lat: 33.4585, lng: 126.9424,
                desc: "<b>가장 가까운 역:</b> 전철 없음 (제주국제공항에서 급행버스 111, 112번 이용).<br>푸른 바다 위로 우뚝 솟은 거대한 사발 모양의 분화구가 장관을 이루는 유네스코 세계자연유산입니다. 정상까지 잘 정비된 계단을 따라 약 20분간 오르면 가슴이 뻥 뚫리는 제주 동쪽 바다의 파노라마 뷰를 감상할 수 있습니다. 하산 길에는 성산보트 양어장에서 해녀들의 물질 시연을 관람하거나 주변 유채꽃밭(봄철)에서 인생 사진을 남기기 좋습니다."
            },
            {
                name: "불국사",
                lat: 35.7901, lng: 129.3320,
                desc: "<b>가장 가까운 역:</b> KTX 신경주역 또는 경주역에서 700번, 10, 11번 버스 이용.<br>신라 시대 불교 문화의 정수를 보여주는 사찰로 국보인 다보탑과 석가탑, 청운교와 백운교를 직접 마주할 수 있습니다. 고즈넉한 숲길을 따라 산책하며 역사 속 장인들의 숨결과 정교한 석조 건축의 미학을 체험하게 됩니다. 봄에는 겹벚꽃, 가을에는 붉은 단풍이 아름다우며, 자차나 셔틀버스로 석굴암까지 함께 둘러보는 코스를 추천합니다."
            },
            {
                name: "전주 한옥마을",
                lat: 35.8147, lng: 127.1526,
                desc: "<b>가장 가까운 역:</b> 전라선 전주역에서 버스(119, 535번 등)로 약 20분 이동.<br>700여 채의 전통 한옥이 도심 속에 보존되어 있어 고풍스러운 기와지붕 아래 전통차를 마시며 여유를 즐기기 좋습니다. 경기전에서 태조 이성계의 어진을 관람하고 전동성당의 아름다운 서양식 건축물을 배경으로 인증샷을 남길 수 있습니다. 특히 전주비빔밥, 한옥마을 길거리의 전주 초코파이, 육전, 맥주 골목(가맥) 등 풍성한 먹거리 투어가 가장 큰 즐거움입니다."
            },
            {
                name: "남이섬",
                lat: 37.7913, lng: 127.5255,
                desc: "<b>가장 가까운 역:</b> 경춘선 가평역에서 도보 20분 또는 택시로 5분 이동 후 선착장 이용.<br>메타세쿼이아 길과 은행나무 길 등 사계절마다 색다른 옷을 입는 아름다운 가로수길이 펼쳐져 있어 자전거를 대여해 섬 전체를 돌기 좋습니다. 섬 내부의 미니 기차인 나눔열차를 타거나 타조, 토끼 등 방목된 동물들과 교감하는 자연 친화적인 힐링을 선사합니다. 모험을 좋아한다면 배 대신 스릴 넘치는 짚와이어를 타고 북한강을 가로질러 섬으로 입장하는 방법을 추천합니다."
            },
            {
                name: "여수 낭만포차거리",
                lat: 34.7394, lng: 127.7420,
                desc: "<b>가장 가까운 역:</b> 전라선 여수엑스포역에서 버스나 택시로 약 7~10분 거리.<br>거북선대교 아래 하멜등대 주변에 위치하여 여수 밤바다의 화려한 야경과 잔잔한 파도 소리를 들으며 낭만적인 밤을 보낼 수 있습니다. 여수의 대표 별미인 '돌문어삼합'과 지역 소주를 맛보며 버스킹 가수들의 감성적인 라이브 공연을 감상하는 재미가 쏠 수 합니다. 주변 여수 해상케이블카를 타고 바다 위를 지나며 도심 불빛을 감상하면 완벽한 야간 여행 코스가 완성됩니다."
            },
            {
                name: "수원 화성",
                lat: 37.2891, lng: 127.0118,
                desc: "<b>가장 가까운 역:</b> 1호선/수인분당선 수원역에서 버스로 10분 (행궁동 하차).<br>정조대왕의 효심과 과학적 성곽 건축의 정수를 보여주는 성곽길로, 장안문에서 창룡문까지 이어지는 산책로가 웅장합니다. 화성행궁 내부를 관람하며 조선 시대 행궁 문화체험을 즐기고, 주변 '행리단길'의 감성 카페와 공방에서 트렌디한 문화를 즐길 수 있습니다. 특히 밤이 되면 성벽을 따라 은은한 조명이 켜져 성곽 야간 산책이나 국궁 활쏘기 체험, 화성어차 탑승이 인기입니다."
            },
            {
                name: "부산 감천문화마을",
                lat: 35.0974, lng: 129.0095,
                desc: "<b>가장 가까운 역:</b> 부산 1호선 토성역 6번 출구에서 마을버스(서구2, 사하1-1) 환승.<br>산자락을 따라 계단식으로 들어선 알록달록한 파스텔톤 집들이 마치 한 폭의 그림 같아 '한국의 마추픽추'라고 불립니다. 마을 골목길 구석구석 설치된 아기자기한 예술 조형물과 벽화를 찾아다니는 스탬프 투어 미션을 즐길 수 있습니다. 특히 줄을 서서 찍는 '어린왕자와 사막여우' 포토존에서 마을 전체와 부산항 바다를 배경으로 멋진 인생 사진을 건질 수 있습니다."
            }
        ];

        // 지도 초기화 함수
        function initMap() {
            // 초기 중심지는 대한민국 중심 부근 (대전/충청 인근)
            const defaultCenter = { lat: 36.3504, lng: 127.3845 };
            
            map = new google.maps.Map(document.getElementById('map'), {
                zoom: 7,
                center: defaultCenter,
                mapTypeControl: false
            });
        }

        // 관광지 선택 시 실행되는 함수
        function selectAttraction(index) {
            const data = attractions[index];
            const position = { lat: data.lat, lng: data.lng };

            // 1. 기존 마커가 있다면 제거
            if (activeMarker) {
                activeMarker.setMap(null);
            }

            // 3. 지도에 마커 표시를 파란색으로 선명하게 설정
            // 구글 표준 마커 핀의 색상을 선명한 파란색(#0055ff)으로 커스텀 빌드합니다.
            activeMarker = new google.maps.Marker({
                position: position,
                map: map,
                title: data.name,
                icon: {
                    path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
                    scale: 6,
                    fillColor: "#0055ff", // 선명한 파란색 채우기
                    fillOpacity: 1.0,     // 흐려지지 않게 불투명도 100%
                    strokeColor: "#ffffff",// 테두리는 흰색으로 선명도 강조
                    strokeWeight: 2
                }
            });

            // 선택한 관광지 위치로 지도 이동 및 줌인
            map.setCenter(position);
            map.setZoom(15);

            // 2. 하단 설명창에 역 정보 및 구체적인 놀거리 3~4줄 매칭하여 갱신
            const descBox = document.getElementById('description-box');
            descBox.innerHTML = `
                <div class="info-title">📍 ${data.name}</div>
                <div>${data.desc}</div>
            `;

            // 버튼 활성화 스타일 전환
            const buttons = document.querySelectorAll('.attraction-btn');
            buttons.forEach((btn, idx) => {
                if(idx === index) btn.classList.add('active');
                else btn.classList.remove('active');
            });
        }
    </script>
</body>
</html>
