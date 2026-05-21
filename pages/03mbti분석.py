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
            st.metric(label="가장 적은 MBTI 유형 (16등)", value=mbti_df.iloc[-1]['MBTI'], delta=f"{mbti_df.iloc[-1]['Percentage']:.2f}%", delta_color="inverse")

    # ------------------------------------------------------------------
    # TAB 2: 신규 기능 (MBTI 선택 ➔ 비율 높은 상위 10개국)
    # ------------------------------------------------------------------
    with tab2:
        st.subheader("🏅 MBTI별 국가 순위 TOP 10")
        selected_mbti = st.selectbox("궁금한 MBTI 유형을 선택하세요:", mbti_types, key="tab2_mbti")

        # 데이터 가공: 선택한 MBTI 열과 Country 열만 추출하여 비율 기준 정렬
        rank_df = df[['Country', selected_mbti]].copy()
        rank_df[selected_mbti] = rank_df[selected_mbti].astype(float) * 100  # 퍼센트 변환
        
        # 가장 높은 나라부터 상위 10개국 추출
        top10_df = rank_df.sort_values(by=selected_mbti, ascending=False).head(10).reset_index(drop=True)

        # 1등은 빨간색, 나머지는 파란색 그라데이션 색상 계산 (총 10개 데이터)
        colors_tab2 = []
        num_items_tab2 = len(top10_df)
        for i in range(num_items_tab2):
            if i == 0:
                colors_tab2.append('rgb(230, 57, 70)')  # 1등 국가: 진한 빨간색
            else:
                blue_intensity = int(50 + (i * (180 / num_items_tab2)))
                green_intensity = int(100 + (i * (110 / num_items_tab2)))
                colors_tab2.append(f'rgb({blue_intensity}, {green_intensity}, 240)')

        # Plotly 그래프 생성
        fig_tab2 = go.Figure(data=[go.Bar(
            x=top10_df['Country'],
            y=top10_df[selected_mbti],
            marker_color=colors_tab2,
            text=top10_df[selected_mbti].round(2).astype(str) + '%',
            textposition='auto',
            hovertemplate='<b>%{x}</b><br>비율: %{y:.2f}%<extra></extra>'
        )])

        fig_tab2.update_layout(
            title=f"🥇 전 세계에서 {selected_mbti} 비율이 가장 높은 국가 TOP 10",
            xaxis_title="국가",
            yaxis_title=f"{selected_mbti} 비율 (%)",
            template="plotly_white",
            yaxis=dict(ticksuffix="%"),
            bargap=0.2
        )
        st.plotly_chart(fig_tab2, use_container_width=True)
        
        # 1등 국가 강조 메시지
        st.info(f"💡 전 세계에서 **{selected_mbti}** 성향이 가장 밀집된 국가는 **{top10_df.iloc[0]['Country']}** ({top10_df.iloc[0][selected_mbti]:.2f}%) 입니다.")

except Exception as e:
    st.error(f"데이터를 불러오거나 처리하는 중 오류가 발생했습니다: {e}")
