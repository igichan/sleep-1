git add .
git commit -m "initial commit"
git push origin main

import streamlit as st
import matplotlib.pyplot as plt

def diagnose_and_plot(RDI, O2):
    result = ""

    if RDI < 5:
        result += "RDI: 정상 (수면무호흡 없음)\n"
    elif RDI < 15:
        result += "RDI: 경도 수면무호흡증\n"
    elif RDI < 30:
        result += "RDI: 중등도 수면무호흡증\n"
    else:
        result += "RDI: 중증 수면무호흡증\n"

    if O2 >= 95:
        result += "평균 혈중 산소농도: 정상"
    elif O2 >= 90:
        result += "평균 혈중 산소농도: 다소 낮음 (주의 필요)"
    elif O2 >= 85:
        result += "평균 혈중 산소농도: 낮음 (위험)"
    else:
        result += "평균 혈중 산소농도: 매우 낮음 (중증 산소저하 가능성)"

    st.subheader("🩺 진단 결과")
    st.text(result)

    # RDI 시각화
    fig1, ax1 = plt.subplots(figsize=(8, 2))
    ax1.set_title("RDI 수면무호흡지수 구간")
    ax1.axvspan(0, 5, color="green", alpha=0.3, label="정상")
    ax1.axvspan(5, 15, color="yellow", alpha=0.3, label="경도")
    ax1.axvspan(15, 30, color="orange", alpha=0.3, label="중등도")
    ax1.axvspan(30, 40, color="red", alpha=0.3, label="중증")
    ax1.axvline(RDI, color="black", linewidth=2, label=f"내 RDI: {RDI}")
    ax1.set_xlim(0, 40)
    ax1.set_yticks([])
    ax1.set_xlabel("RDI")
    ax1.grid(axis='x')
    ax1.legend(loc="upper left")
    st.pyplot(fig1)

    # 산소농도 시각화
    fig2, ax2 = plt.subplots(figsize=(8, 2))
    ax2.set_title("산소농도 구간 (%)")
    ax2.axvspan(0, 85, color="red", alpha=0.3, label="매우 낮음")
    ax2.axvspan(85, 90, color="orange", alpha=0.3, label="낮음")
    ax2.axvspan(90, 95, color="yellow", alpha=0.3, label="다소 낮음")
    ax2.axvspan(95, 100, color="green", alpha=0.3, label="정상")
    ax2.axvline(O2, color="black", linewidth=2, label=f"내 산소농도: {O2}%")
    ax2.set_xlim(80, 100)
    ax2.set_yticks([])
    ax2.set_xlabel("평균 산소농도 (%)")
    ax2.grid(axis='x')
    ax2.legend(loc="upper left")
    st.pyplot(fig2)

# Streamlit UI
st.title("수면무호흡 진단 시뮬레이터")

rdi_val = st.number_input("RDI (수면무호흡지수)", min_value=0.0, max_value=100.0, step=0.1)
o2_val = st.number_input("평균 산소농도 (%)", min_value=50.0, max_value=100.0, step=0.1)

if st.button("진단하기"):
    diagnose_and_plot(rdi_val, o2_val)
