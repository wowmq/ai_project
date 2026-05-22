import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# --- 1. 스트림릿 클라우드 안전한 한글 설정 (외부 다운로드 없음) ---
@st.cache_data
def set_korean_font():
    """리눅스/스트림릿 클라우드 환경에서 깨지지 않는 기본 한글/고딕 폰트 설정"""
    available_fonts = [f.name for f in fm.fontManager.ttflist]
    
    # 순서대로 지원하는 폰트 찾기 (DejaVu Sans는 스트림릿 클라우드 리눅스 기본 내장이며 한글 지원함)
    font_family = "DejaVu Sans"
    for f in ["NanumGothic", "NanumBarunGothic", "Liberation Sans", "DejaVu Sans"]:
        if f in available_fonts:
            font_family = f
            break
            
    plt.rc('font', family=font_family)
    plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

set_korean_font()


# --- 2. 데이터 로드 및 전처리 (UnicodeDecodeError 해결 버전) ---
@st.cache_data
def load_data():
    # 파일 인코딩 에러를 방지하기 위해 여러 인코딩 방식을 순서대로 시도합니다.
    encodings = ['utf-8', 'cp949', 'euc-kr', 'utf-8-sig']
    df = None
    
    for encoding in encodings:
        try:
            df = pd.read_csv("population.csv", encoding=encoding)
            break  # 성공적으로 읽으면 반복문 탈출
        except UnicodeDecodeError:
            continue
            
    if df is None:
        raise ValueError("파일을 읽을 수 없습니다. 인코딩 형식을 확인해 주세요.")
    
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
except ValueError as e:
    st.error(f"❌ {e}")
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

# 그래프 생성
fig, ax = plt.subplots(figsize=(10, 6))

# 조건 4: 그래프 바탕색 설정 (연한 보라색)
fig.patch.set_facecolor('#F3E5F5') # 전체 배경색
ax.set_facecolor('#F3E5F5')        # 그래프 내부 배경색

# 조건 2 & 4: 가로축 연령대, 세로축 인구수 꺾은선 그래프 (빨간색)
ax.plot(age
