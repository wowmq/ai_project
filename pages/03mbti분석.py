import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="글로벌 MBTI 비율 분석기", layout="centered")
st.title("🌍 국가별 MBTI 비율 시각화")
st.write("국가를 선택하면 해당 국가의 MBTI 16가지 유형 비율을 인터렉티브한 그래프로 보여줍니다.")

# 2. 데이터 불러오기 함수 (캐싱 처리로 속도 향상)
@st.cache_data
def load_data():
    # Streamlit Cloud에 csv 파일이 동일 디렉토리에 있다고 가정합니다.
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

try:
    df = load_data()

    # 3. 사이드바 또는 메인 화면에서 국가 선택
    country_list = df['Country'].unique()
    selected_country = st.selectbox("분석할 국가를 선택하세요:", country_list)

    # 4. 선택된 국가의 데이터 추출 및 정렬
    country_data = df[df['Country'] == selected_country].iloc[0]
    
    # 'Country' 열을 제외한 MBTI 유형과 비율만 추출하여 데이터프레임 생성
    mbti_probs = country_data.drop('Country').astype(float)
    mbti_df = pd.DataFrame({'MBTI': mbti_probs.index, 'Percentage': mbti_probs.values * 100})
    
    # 비율이 높은 순서대로 정렬
    mbti_df = mbti_df.sort_values(by='Percentage', ascending=False).reset_index(drop=True)

    # 5. 조건별 색상 지정 (1등은 빨간색, 나머지는 파란색 그라데이션)
    # 정렬된 상태이므로 index 0이 1등입니다.
    colors = []
    num_items = len(mbti_df)
    
    for i in range(num_items):
        if i == 0:
            colors.append('rgb(230, 57, 70)')  # 1등: 진한 빨간색
        else:
            # 순위가 낮아질수록(i가 커질수록) 파란색이 점점 연해지도록 그라데이션 계산
            # rgb(최소값~최대값) 범위를 활용해 부드러운 그라데이션 구현
            blue_intensity = int(50 + (i * (180 / num_items)))
            green_intensity = int(100 + (i * (110 / num_items)))
            colors.append(f'rgb({blue_intensity}, {green_intensity}, 240)')

    # 6. Plotly를 이용한 인터렉티브 막대 그래프 생성
    fig = go.Figure(data=[go.Bar(
        x=mbti_df['MBTI'],
        y=mbti_df['Percentage'],
        marker_color=colors,
        text=mbti_df['Percentage'].round(2).astype(str) + '%', # 막대 위에 마우스를 대지 않아도 수치 표시
        textposition='auto',
        hovertemplate='<b>%{x}</b><br>비율: %{y:.2f}%<extra></extra>'
    )])

    # 그래프 레이아웃 설정 (깔끔하고 세련된 테마)
    fig.update_layout(
        title=f"📊 {selected_country}의 MBTI 유형별 비율 (높은 순)",
        xaxis_title="MBTI 유형",
        yaxis_title="비율 (%)",
        template="plotly_white",
        yaxis=dict(ticksuffix="%"),
        bargap=0.2
    )

    # 7. 스트림릿 화면에 그래프 그리기
    st.plotly_chart(fig, use_container_width=True)

    # 추가 정보 (미니 인사이트 카드)
    st.subheader(f"💡 {selected_country} 특징 요약")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="가장 많은 MBTI 유형 (1등)", value=mbti_df.iloc[0]['MBTI'], delta=f"{mbti_df.iloc[0]['Percentage']:.2f}%")
    with col2:
        st.metric(label="가장 적은 MBTI 유형 (16등)", value=mbti_df.iloc[-1]['MBTI'], delta=f"{mbti_df.iloc[-1]['Percentage']:.2f}%", delta_color="inverse")

except Exception as e:
    st.error(f"데이터를 불러오거나 처리하는 중 오류가 발생했습니다: {e}")
