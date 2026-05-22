import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# --- 1. 안전한 한글 폰트 설정 ---
@st.cache_data
def set_korean_font():
    available_fonts = [f.name for f in fm.fontManager.ttflist]
    font_family = "DejaVu Sans"
    for f in ["NanumGothic", "NanumBarunGothic", "Liberation Sans", "DejaVu Sans"]:
        if f in available_fonts:
            font_family = f
            break
    plt.rc('font', family=font_family)
    plt.rcParams['axes.unicode_minus'] = False

set_korean_font()


# --- 2. 데이터 로드 및 전처리 ---
@st.cache_data
def load_data():
    encodings = ['utf-8', 'cp949', 'euc-kr', 'utf-8-sig']
    df = None
    
    for encoding in encodings:
        try:
            df = pd.read_csv("population.csv", encoding=encoding)
            break
        except UnicodeDecodeError:
            continue
            
    if df is None:
        raise ValueError("파일을 읽을 수 없습니다. 인코딩 형식을 확인해 주세요.")
    
    # 행정구역 명칭 전처리
    def clean_region_name(name):
        name = str(name).replace("서울특별시 ", "")
        if "(" in name:
            name = name.split("(")[0].strip()
        return name
    
    df['표시행정구역'] = df['행정구역'].apply(clean_region_name)
    df = df.rename(columns=lambda x: x.lstrip('_'))
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("📂 'population.csv' 파일을 찾을 수 없습니다.")
    st.stop()
except ValueError as e:
    st.error(f"❌ {e}")
    st.stop()


# --- 3. 스트림릿 UI 구성 ---
st.title("🏙️ 서울시 강북구 인구 통계 대시보드")
st.write("공공데이터를 활용한 행정동별 연령대 인구수 시각화 웹 앱입니다.")

region_list = df['표시행정구역'].tolist()
selected_region = st.selectbox("분석할 행정동을 선택하세요:", region_list)


# --- 4. 데이터 필터링 및 그래프 시각화 ---
selected_data = df[df['표시행정구역'] == selected_region].iloc[0]
age_columns = [col for col in df.columns if col not in ['행정구역', '표시행정구역']]
population_values = []

for col in age_columns:
    val = str(selected_data[col]).replace(',', '')
    population_values.append(int(val))

# 그래프 생성 (배경색 및 선 색상 조건 반영)
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#F3E5F5')  # 연한 보라색 배경
ax.set_facecolor('#F3E5F5')

# 꺾은선 그래프 그리기 (빨간색)
ax.plot(age_columns, population_values, color='red', marker='o', linewidth=2, markersize=6)

# 제목 및 레이블 설정
ax.set_title("서울시의 인구통계", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("연령대", fontsize=12, labelpad=10)
ax.set_ylabel("인구수 (명)", fontsize=12, labelpad=10)

ax.grid(True, linestyle='--', alpha=0.5, color='#999999')
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)


# --- 5. 데이터 테이블 상세 보기 ---
with st.expander("📊 선택한 지역 원본 데이터 보기"):
    raw_display = pd.DataFrame([population_values], columns=age_columns, index=[selected_region])
    st.dataframe(raw_display)
