import streamlit as st

def diagnose(RDI, O2):
    결과 = ""

    if RDI < 5:
        결과 += "RDI: 정상 (수면무호흡 없음)\n"
    elif RDI < 15:
        결과 += "RDI: 경도 수면무호흡증\n"
    elif RDI < 30:
        결과 += "RDI: 중등도 수면무호흡증\n"
    else:
        결과 += "RDI: 중증 수면무호흡증\n"

    결과 += "\n"

    if O2 >= 95:
        결과 += "평균 혈중 산소농도: 정상"
    elif O2 >= 90:
        결과 += "평균 혈중 산소농도: 다소 낮음 (주의 필요)"
    elif O2 >= 85:
        결과 += "평균 혈중 산소농도: 낮음 (위험)"
    else:
        결과 += "평균 혈중 산소농도: 매우 낮음 (중증 산소저하 가능성)"

    return 결과

# Streamlit 인터페이스
st.title("수면무호흡증 판별 모의 프로그램")

rdi = st.number_input("RDI (수면무호흡지수)", min_value=0.0, max_value=100.0, step=0.1, format="%.1f")
o2 = st.number_input("평균 혈중 산소농도 (%)", min_value=50.0, max_value=100.0, step=0.1, format="%.1f")

if st.button("결과 보기"):
    진단결과 = diagnose(rdi, o2)
    st.subheader("🔍 진단 결과")
    st.text(진단결과)
