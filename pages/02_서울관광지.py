import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. 페이지 설정
st.set_page_config(
    page_title="Seoul Top 10 Attractions for Foreigners",
    page_icon="📌",
    layout="wide"
)

# 2. 타이틀 및 소개
st.title("🇰🇷 Top 10 Seoul Attractions for Tourists")
st.markdown("""
Welcome to Seoul! This interactive map shows the **Top 10 must-visit attractions** highly loved by international visitors. 
Click on the markers to see the names and descriptions of each place.
""")

# 3. 서울 주요 관광지 Top 10 데이터 (위도, 경도, 이름, 설명)
attractions = [
    {
        "name": "Gyeongbokgung Palace (경복궁)",
        "lat": 37.5796, "lon": 126.9770,
        "desc": "The main and largest royal palace of the Joseon Dynasty. Perfect for Hanbok (traditional clothing) experiences."
    },
    {
        "name": "N Seoul Tower (N서울타워)",
        "lat": 37.5512, "lon": 126.9882,
        "desc": "Located on Namsan Mountain, offering breathtaking panoramic views of the entire city, especially at night."
    },
    {
        "name": "Myeong-dong (명동)",
        "lat": 37.5635, "lon": 126.9846,
        "desc": "Seoul's ultimate shopping district, famous for cosmetics, fashion trends, and incredible street food."
    },
    {
        "name": "Bukchon Hanok Village (북촌한옥마을)",
        "lat": 37.5829, "lon": 126.9835,
        "desc": "A picturesque village filled with hundreds of traditional Korean houses (Hanoks) dating back to the Joseon Dynasty."
    },
    {
        "name": "Insadong (인사동)",
        "lat": 37.5744, "lon": 126.9875,
        "desc": "A vibrant cultural street where you can experience traditional Korean crafts, tea houses, and antique shops."
    },
    {
        "name": "Dongdaemun Design Plaza - DDP (동대문디자인플라자)",
        "lat": 37.5668, "lon": 127.0094,
        "desc": "An iconic futuristic landmark designed by Zaha Hadid, famous for fashion shows, exhibitions, and modern architecture."
    },
    {
        "name": "Hongdae (홍대거리)",
        "lat": 37.5555, "lon": 126.9240,
        "desc": "The center of youth culture, indie music, busking, and vibrant nightlife near Hongik University."
    },
    {
        "name": "Lotte World Tower & Mall (롯데월드타워)",
        "lat": 37.5126, "lon": 127.1025,
        "desc": "The tallest building in Korea (555m). Features the 'Seoul Sky' observation deck and a massive shopping complex."
    },
    {
        "name": "Gangnam COEX Mall & Starfield Library (코엑스 스타필드)",
        "lat": 37.5119, "lon": 127.0589,
        "desc": "A massive underground mall featuring the famous Instagrammable Starfield Library with giant bookshelves."
    },
    {
        "name": "Gwangjang Market (광장시장)",
        "lat": 37.5701, "lon": 127.0010,
        "desc": "One of Korea's oldest traditional markets, world-famous for street food like Binden-tteok (mung bean pancakes) and Mayak Gimbap."
    }
]

# 4. 사이드바 - 목록 보기
st.sidebar.header("📍 Attraction List")
for i, place in enumerate(attractions, 1):
    st.sidebar.markdown(f"**{i}. {place['name']}**")

# 5. 지도 생성 및 마커 추가
# 서울 중심부 좌표로 초기 지도 설정
m = folium.Map(location=[37.555, 126.985], zoom_start=12, tiles="OpenStreetMap")

# 관광지 마커 추가
for place in attractions:
    # 팝업에 들어갈 HTML 스타일링
    popup_html = f"""
    <div style="font-family: Arial, sans-serif; width: 200px;">
        <h4 style="margin: 0 0 5px 0; color: #1E3A8A;">{place['name']}</h4>
        <p style="margin: 0; font-size: 12px; color: #4B5563;">{place['desc']}</p>
    </div>
    """
    popup = folium.Popup(popup_html, max_width=250)
    
    folium.Marker(
        location=[place['lat'], place['lon']],
        popup=popup,
        tooltip=place['name'],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 6. 스트림릿 레이아웃에 지도 렌더링
st_folium(m, width=900, height=600, returned_objects=[])

# 7. 푸터
st.caption("Data source: Compiled based on popular Korea Tourism Organization (KTO) trends.")
