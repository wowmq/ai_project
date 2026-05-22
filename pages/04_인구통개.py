import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import urllib.request
import os

# --- 1. 스트림릿 클라우드 한글 깨짐 방지 폰트 설정 ---
@st.cache_data
def load_korean_font():
    """스트림릿 클라우드 환경에서 한글 폰트를 다운로드하고 설정하는 함수"""
    font_url = "https://github.com/google/fonts/raw/main/ofl/nanumgothic/NanumGothic-Regular.ttf"
    font_path = "NanumGothic-Regular.ttf"
    
    # 폰트 파일이 없으면 다운로드
    if not os.path.exists(font_path):
        urllib.request.urlretrieve(font_url, font_path)
    
    # Matplotlib에 폰트 등록
    fm.font_manager.addfont(font_path)
    font_prop = fm.FontProperties(fname=font_path)
    plt.rc('font', family=font_prop.get_name())
    plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

# 폰트 로드 실행
load_korean_font()


# --- 2. 데이터 로드 및 전처리 ---
@st.cache_data
def load_data():
    # 데이터 불러오기 (업로드된 population.csv 파일이 같은 경로에 있어야 합니다)
    df = pd.read_csv("population.csv")
    
    # 행정구역 이름 깔끔하게 정리 (예: "서울특별시 강북구 삼양동(11305...)" -> "강북구 삼양동")
    def clean_region_name(name):
        name = name.replace("서울특별시 ", "")
        if "(" in name:
            name = name.split("(")[0].strip()
        return name
    
    df['표시행정구역'] = df['행정구역'].apply(clean_region_name)
    
    # 연령대 컬럼 앞의 언더바(_) 제거하여 깔끔하게 통일
    df = df.rename(columns=lambda x: x.lstrip('_'))
    
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("📂 'population.csv' 파일을 찾을 수 없습니다. GitHub 저장소에 데이터 파일을 함께 업로드해 주세요!")
    st.stop()


# --- 3. 스트림릿 UI 구성 ---
st.title("🏙️ 서울시 강북구 인구 통계 대시보드")
st.markdown("공공데이터를 활용한 행정동별 연령대 인구수 시각화 웹 앱입니다.")

# 행정동 선택 셀렉트박스
region_list = df['표시행정구역'].tolist()
selected_region = st.selectbox("분석할 행정동을 선택하세요:", region_list)


# --- 4. 데이터 필터링 및 그래프 그리기 ---
# 선택한 행정동의 데이터 추출
selected_data = df[df['표시행정구역'] == selected_region].iloc[0]

# 연령대 컬럼들만 선택 (행정구역 관련 컬럼 제외)
age_columns = [col for col in df.columns if col not in ['행정구역', '표시행정구역']]
population_values = []

# 천 단위 콤마(,)가 포함된 문자열을 숫자로 변환
for col in age_columns:
    val = str(selected_data[col]).replace(',', '')
    population_values.append(int(val))

# 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 6))

# 조건 4: 그래프 바탕색 설정 (연한 보라색 #E8DFF5 또는 #F3E5F5)
fig.patch.set_facecolor('#F3E5F5') # 전체 피규어 배경색
ax.set_facecolor('#F3E5F5')        # 그래프 안쪽 배경색

# 조건 2 & 4: 가로축 연령대, 세로축 인구수 꺾은선 그래프 (빨간색)
ax.plot(age_columns, population_values, color='red', marker='o', linewidth=2, markersize=6)

# 조건 3: 그래프 제목 및 레이블 설정 (한글 깨짐 없음)
ax.set_title(f"서울시의 인구통계 ({selected_region})", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("연령대", fontsize=12, labelpad=10)
ax.set_ylabel("인구수 (명)", fontsize=12, labelpad=10)

# 그래프 그리드 격자 및 디테일 설정
ax.grid(True, linestyle='--', alpha=0.5, color='#999999')
plt.xticks(rotation=45)
plt.tight_layout()

# 스트림릿에 그래프 출력
st.pyplot(fig)


# --- 5. 상세 데이터 테이블 보기 ---
with st.expander("📊 선택한 지역 원본 데이터 보기"):
    raw_display = pd.DataFrame([population_values], columns=age_columns, index=[selected_region])
    st.dataframe(raw_display)
