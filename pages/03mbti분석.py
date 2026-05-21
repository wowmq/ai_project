import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="글로벌 MBTI 분석 대시보드", layout="centered")
st.title("🌍 글로벌 MBTI 데이터 시각화")
st.write("국가별 MBTI 비율을 확인하거나, 특정 MBTI 유형이 가장 많은 국가 순위를 탐색해 보세요.")

# 2. 데이터 불러오기 함수 (캐싱 처리)
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

try:
    df = load_data()
    
    # MBTI 16가지 유형 목록 정의 (첫 번째 'Country' 열 제외)
    mbti_types = [col for col in df.columns if col != 'Country']

    # 3. 탭(Tab) 구성으로 기존 기능과 신규 기능 분리
    tab1, tab2 = st.tabs(["📊 국가별 MBTI 비율 (기존)", "🏆 MBTI별 상위 10개국 (신규)"])

    # ------------------------------------------------------------------
    # TAB 1: 기존 기능 (국가 선택 ➔ 해당 국가의 MBTI 비율)
    # ------------------------------------------------------------------
    with tab1:
        st.subheader("📍 국가별 MBTI 분석")
        country_list = df['Country'].unique()
        selected_country = st.selectbox("분석할 국가를 선택하세요:", country_list, key="tab1_country")

        # 데이터 추출 및 정렬
        country_data = df[df['Country'] == selected_country].iloc[0]
        mbti_probs = country_data.drop('Country').astype(float)
        mbti_df = pd.DataFrame({'MBTI': mbti_probs.index, 'Percentage': mbti_probs.values * 100})
        mbti_df = mbti_df.sort_values(by='Percentage', ascending=False).reset_index(drop=True)

        # 1등은 빨간색, 나머지는 파란색 그라데이션 색상 계산
        colors_tab1 = []
        num_items_tab1 = len(mbti_df)
        for i in range(num_items_tab1):
            if i == 0:
                colors_tab1.append('rgb(230, 57, 70)')  # 1등: 진한 빨간색
            else:
                blue_intensity = int(50 + (i * (180 / num_items_tab1)))
                green_intensity = int(100 + (i * (110 / num_items_tab1)))
                colors_tab1.append(f'rgb({blue_intensity}, {green_intensity}, 240)')

        # Plotly 그래프 생성
        fig_tab1 = go.Figure(data=[go.Bar(
            x=mbti_df['MBTI'],
            y=mbti_df['Percentage'],
            marker_color=colors_tab1,
            text=mbti_df['Percentage'].round(2).astype(str) + '%',
            textposition='auto',
            hovertemplate='<b>%{x}</b><br>비율: %{y:.2f}%<extra></extra>'
        )])

        fig_tab1.update_layout(
            title=f"📊 {selected_country}의 MBTI 유형별 비율 (높은 순)",
            xaxis_title="MBTI 유형",
            yaxis_title="비율 (%)",
            template="plotly_white",
            yaxis=dict(ticksuffix="%"),
            bargap=0.2
        )
        st.plotly_chart(fig_tab1, use_container_width=True)

        # 미니 인사이트 카드
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="가장 많은 MBTI 유형 (1등)", value=mbti_df.iloc[0]['MBTI'], delta=f"{mbti_df.iloc[0]['Percentage']:.2f}%")
        with col2:
            st.metric(label="가장 적은 MBTI 유형 (16
