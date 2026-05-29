import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as object
from sklearn.linear_model import LinearRegression

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="서울 기온 분석 및 예측 앱", layout="centered")
st.title("🌡️ 서울 역대 기온 분석 및 미래 예측")
st.write("1907년부터의 서울 기온 데이터를 바탕으로 과거 추이를 확인하고, 통계 모델을 통해 미래 기온을 예측합니다.")

# 2. 데이터 로드 함수 (캐싱 및 인코딩 예외 처리)
@st.cache_data
def load_data():
    encodings = ['utf-8', 'cp949', 'euc-kr', 'utf-8-sig']
    df = None
    
    for encoding in encodings:
        try:
            df = pd.read_csv("seoul.csv", encoding=encoding)
            break
        except (UnicodeDecodeError, LookupError):
            continue
            
    if df is None:
        raise ValueError("seoul.csv 파일을 읽을 수 있는 인코딩 형식을 찾지 못했습니다.")
    
    # 전처리: 컬럼명 공백 제거
    df.columns = df.columns.str.strip()
    
    # [문법 수정] 문자열 변환 후 탭 문자(\t)와 공백을 가장 안전한 내장 함수 방식으로 제거 (SyntaxError 방지)
    df['날짜'] = df['날짜'].astype(str)
    df['날짜'] = df['날짜'].str.replace('\t', '', regex=False)
    df['날짜'] = df['날짜'].str.replace(' ', '', regex=False)
    
    # 날짜 데이터 타입을 datetime으로 변환 (에러는 누락 처리)
    df['날짜'] = pd.to_datetime(df['날짜'], errors='coerce')
    
    # 필수 결측치 제거
    df = df.dropna(subset=['날짜', '최고기온(℃)', '최저기온(℃)'])
    
    # 연, 월, 일 컬럼 파생
    df['연도'] = df['날짜'].dt.year
    df['월'] = df['날짜'].dt.month
    df['일'] = df['날짜'].dt.day
    
    return df

try:
    df = load_data()
    max_data_year = int(df['연도'].max())

    # 3. 사용자 입력 UI (사이드바)
    st.sidebar.header("📅 분석 및 예측 설정")
    selected_month = st.sidebar.selectbox("월을 선택하세요", list(range(1, 13)), index=4)  # 기본값 5월
    selected_day = st.sidebar.selectbox("일을 선택하세요", list(range(1, 32)), index=25)   # 기본값 26일
    
    # 예측을 위한 미래 연도 선택
    predict_year = st.sidebar.slider(
        "예측할 미래 연도를 선택하세요", 
        min_value=max_data_year + 1, 
        max_value=2100, 
        value=max_data_year + 10
    )

    # 4. 데이터 필터링 및 과거 트렌드 정렬
    filtered_df = df[(df['월'] == selected_month) & (df['일'] == selected_day)]
    filtered_df = filtered_df.sort_values(by='연도')

    if filtered_df.empty:
        st.warning(f"선택하신 {selected_month}월 {selected_day}일에 해당하는 과거 데이터가 부족합니다. 다른 날짜를 선택해 주세요.")
    else:
        # 5. 머신러닝(Linear Regression) 기반 미래 기온 예측 코드
        X = filtered_df[['연도']].values
        y_max = filtered_df['최고기온(℃)'].values
        y_min = filtered_df['최저기온(℃)'].values
        
        # 최고기온 모델 학습 및 예측
        model_max = LinearRegression()
        model_max.fit(X, y_max)
        predicted_max = model_max.predict([[predict_year]])[0]
        
        # 최저기온 모델 학습 및 예측
        model_min = LinearRegression()
        model_min.fit(X, y_min)
        predicted_min = model_min.predict([[predict_year]])[0]

        # 6. 예측 결과 상단 배치
        st.subheader(f"🔮 {predict_year}년 {selected_month}월 {selected_day}일 기온 예측 결과")
        p_col1, p_col2 = st.columns(2)
        with p_col1:
            st.metric(label="예측 최고기온", value=f"{predicted_max:.1f} ℃", delta="통계적 선형 예측")
        with p_col2:
            st.metric(label="예측 최저기온", value=f"{predicted_min:.1f} ℃", delta="통계적 선형 예측")

        # 7. 시각화를 위한 과거 데이터와 예측 데이터 결합
        plot_df = filtered_df[['연도', '최고기온(℃)', '최저기온(℃)']].copy()
        
        # 추세선(Trendline) 데이터 계산
        full_years = np.array(list(range(int(plot_df['연도'].min()), predict_year + 1))).reshape(-1, 1)
        trend_max = model_max.predict(full_years)
        trend_min = model_min.predict(full_years)

        # 8. Plotly를 이용한 그래프 시각화
        st.subheader(f"📊 날짜별 기온분석 ({plot_df['연도'].min()}년 ~ {predict_year}년)")
        fig = object.Figure()
        
        # 과거 최고기온 (핫핑크)
        fig.add_trace(object.Scatter(
            x=plot_df['연도'], y=plot_df['최고기온(℃)'],
            mode='lines+markers', name='과거 최고기온',
            line=dict(color='deeppink', width=2),
            hovertemplate='<b>%{x}년 최고기온</b><br>온도: %{y:.1f}℃<extra></extra>'
        ))
        
        # 미래 예측 최고기온 단독 점 표시
        fig.add_trace(object.Scatter(
            x=[predict_year], y=[predicted_max],
            mode='markers', name='예측 최고기온',
            marker=dict(color='crimson', size=10, symbol='diamond'),
            hovertemplate='<b>🎯 %{x}년 예측 최고</b><br>온도: %{y:.1f}℃<extra></extra>'
        ))

        # 최고기온 장기 추세선
        fig.add_trace(object.Scatter(
            x=full_years.flatten(), y=trend_max,
            mode='lines', name='최고기온 상승추세',
            line=dict(color='deeppink', width=1, dash='dash'),
            hoverinfo='skip'
        ))
        
        # 과거 최저기온 (연한 파란색)
        fig.add_trace(object.Scatter(
            x=plot_df['연도'], y=plot_df['최저기온(℃)'],
            mode='lines+markers', name='과거 최저기온',
            line=dict(color='lightskyblue', width=2),
            hovertemplate='<b>%{x}년 최저기온</b><br>온도: %{y:.1f}℃<extra></extra>'
        ))
        
        # 미래 예측 최저기온 단독 점 표시
        fig.add_trace(object.Scatter(
            x=[predict_year], y=[predicted_min],
            mode='markers', name='예측 최저기온',
            marker=dict(color='darkblue', size=10, symbol='diamond'),
            hovertemplate='<b>🎯 %{x}년 예측 최저</b><br>온도: %{y:.1f}℃<extra></extra>'
        ))

        # 최저기온 장기 추세선
        fig.add_trace(object.Scatter(
            x=full_years.flatten(), y=trend_min,
            mode='lines', name='최저기온 상승추세',
            line=dict(color='lightskyblue', width=1, dash='dash'),
            hoverinfo='skip'
        ))
        
        # 레이아웃 정의
        fig.update_layout(
            title={
                'text': "날짜별 기온분석",
                'y': 0.95, 'x': 0.5,
                'xanchor': 'center', 'yanchor': 'top',
                'font': dict(size=20, weight='bold')
            },
            xaxis_title="연도",
            yaxis_title="온도 (℃)",
            showlegend=True,
            hovermode="x unified",
            plot_bgcolor="white"
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')

        st.plotly_chart(fig, use_container_width=True)

except FileNotFoundError:
    st.error("📂 `seoul.csv` 파일을 찾을 수 없습니다. 대시보드 스크립트와 동일한 루트 폴더에 데이터를 위치시켜 주세요.")
except ValueError as ve:
    st.error(f"❌ 데이터 로드 실패: {ve}")
