import streamlit as st

def 진단_등급_텍스트(RDI, O2):
    rdi_등급 = ""
    o2_등급 = ""

    if RDI < 5:
        rdi_등급 = "🟩 정상 (수면무호흡 없음)"
    elif RDI < 15:
        rdi_등급 = "🟨 경도 수면무호흡증"
    elif RDI < 30:
        rdi_등급 = "🟧 중등도 수면무호흡증"
    else:
        rdi_등급 = "🟥 중증 수면무호흡증"

    if O2 >= 95:
        o2_등급 = "🟩 정상"
    elif O2 > 90:
        o2_등급 = "🟨 다소 낮음 (주의)"
    elif O2 > 85:
        o2_등급 = "🟧 낮음 (위험)"
    else:
        o2_등급 = "🟥 매우 낮음 (산소저하)"

    return rdi_등급, o2_등급

st.title("🩺 수면무호흡 진단기")

rdi = st.number_input("RDI (수면무호흡지수)", min_value=0.0, max_value=100.0, step=0.1)
o2 = st.number_input("평균 산소농도 (%)", min_value=50.0, max_value=100.0, step=0.1)

if st.button("결과 보기"):
    rdi_result, o2_result = 진단_등급_텍스트(rdi, o2)

    st.subheader("🔍 진단 결과")
    st.write(f"➡️ 내 RDI: {rdi} → {rdi_result}")
    st.write(f"➡️ 내 산소농도: {o2}% → {o2_result}")

    st.markdown("---")
    st.markdown("### 🗂️ 기준 구간")
    st.markdown("**RDI 구간**")
    st.text("🟩 0~5: 정상\n🟨 5~15: 경도\n🟧 15~30: 중등도\n🟥 30 이상: 중증")
    st.markdown("**산소농도 구간**")
    st.text("🟥 0~85: 매우 낮음\n🟧 85~90: 낮음\n🟨 90~95: 다소 낮음\n🟩 95~100: 정상")
