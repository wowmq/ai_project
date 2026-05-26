import streamlit as st
import pandas as pd
import plotly.graph_objects as object

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="서울 기온 분석 앱", layout="centered")
st.title("🌡️ 서울 역대 날짜별 기온 분석")
st.write("1907년부터의 서울 기온 데이터를 바탕으로, 특정 날짜의 연도별 최고/최저 기온 변화 추이를 확인합니다.")

# 2. 데이터 로드 함수 (캐싱 적용으로 속도 향상)
@st.cache_data
def load_data():
    # 데이터 불러오기
    df = pd.read_csv("seoul.csv")
    
    # 컬럼명 공백 제거 및 확인
    df.columns = df.columns.str.strip()
    
    # '날짜' 컬럼의 문자열 공백 및 탭(\t) 기호 완벽 제거
    df['날짜'] = df['날짜'].astype(str).str.replace(r'[\t\s]', '', regex=True)
    
    # 날짜 데이터 타입을 datetime으로 변환 (에러는 누락 처리)
    df['날짜'] = pd.to_datetime(df['날짜'], errors='coerce')
    
    # 날짜 파싱 실패 데이터 및 기온 데이터 결측치(NaN) 제거
    df = df.dropna(subset=['날짜', '최고기온(℃)', '최저기온(℃)'])
    
    # 분석에 필요한 연, 월, 일 컬럼 추가
    df['연도'] = df['날짜'].dt.year
    df['월'] = df['날짜'].dt.month
    df['일'] = df['날짜'].dt.day
    
    return df

try:
    df = load_data()

    # 3. 사용자 입력 UI (사이드바 또는 메인 화면)
    st.sidebar.header("📅 분석하고 싶은 날짜 선택")
    selected_month = st.sidebar.selectbox("월을 선택하세요", list(range(1, 13)), index=4)  # 기본값 5월
    
    # 선택한 월에 맞는 일 수 계산 (안전한 처리를 위해 1~31일까지 제공 후 필터링)
    selected_day = st.sidebar.selectbox("일을 선택하세요", list(range(1, 32)), index=25)   # 기본값 26일

    # 4. 데이터 필터링
    filtered_df = df[(df['월'] == selected_month) & (df['일'] == selected_day)]
    # 연도 순으로 정렬
    filtered_df = filtered_df.sort_values(by='연도')

    if filtered_df.empty:
        st.warning(f"선택하신 {selected_month}월 {selected_day}일에 해당하는 데이터가 없습니다. 다른 날짜를 선택해 주세요.")
    else:
        st.subheader(f"📊 매년 {selected_month}월 {selected_day}일의 기온 변화")
        
        # 5. Plotly를 활용한 꺾은선 그래프 생성
        fig = object.Figure()
        
        # 최고기온 선 추가 (핫핑크색)
        fig.add_trace(object.Scatter(
            x=filtered_df['연도'],
            y=filtered_df['최고기온(℃)'],
            mode='lines+markers',
            name='최고기온',
            line=dict(color='deeppink', width=2),
            marker=dict(size=4)
        ))
        
        # 최저기온 선 추가 (연한 파란색 / 스카이블루)
        fig.add_trace(object.Scatter(
            x=filtered_df['연도'],
            y=filtered_df['최저기온(℃)'],
            mode='lines+markers',
            name='최저기온',
            line=dict(color='lightskyblue', width=2),
            marker=dict(size=4)
        ))
        
        # 레이아웃 정의 (요청하신 조건 충족)
        fig.update_layout(
            title={
                'text': "날짜별 기온분석",
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': dict(size=20, weight='bold')
            },
            xaxis_title="연도",
            yaxis_title="온도 (℃)",
            showlegend=True,  # 범례 표시
            legend=dict(x=0.01, y=0.99, bgcolor="rgba(255, 255, 255, 0.5)"),
            hovermode="x unified",
            plot_bgcolor="white"
        )
        
        # 격자선 스타일 조정
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')

        # 스트림릿 화면에 그래프 그리기
        st.plotly_chart(fig, use_container_width=True)
        
        # 6. 추가 통계 정보 표시 (선택 항목)
        st.markdown("#### 💡 이 날짜의 기록적인 순간들")
        max_row = filtered_df.loc[filtered_df['최고기온(℃)'].idxmax()]
        min_row = filtered_df.loc[filtered_df['최저기온(℃)'].idxmin()]
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label=f"역대 가장 더웠던 {selected_month}/{selected_day}", 
                      value=f"{max_row['최고기온(℃)']} ℃", 
                      delta=f"{int(max_row['연도'])}년")
        with col2:
            st.metric(label=f"역대 가장 추웠던 {selected_month}/{selected_day}", 
                      value=f"{min_row['최저기온(℃)']} ℃", 
                      delta=f"{int(min_row['연도'])}년")

except FileNotFoundError:
    st.error("📂 `seoul.csv` 파일을 찾을 수 없습니다. 대시보드 스크립트(`app.py`)와 동일한 폴더(루트 경로)에 데이터를 업로드해 주세요.")
