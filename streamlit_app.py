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
    elif O2 >= 90:
        o2_등급 = "🟨 경계선 (주의)"
    elif O2 > 90:
        o2_등급 = "🟧 위험 수준"
    else:
        o2_등급 = "🟥 산소 저하"

    return rdi_등급, o2_등급

st.title("🩺 수면무호흡 진단기")

rdi = st.number_input("RDI (수면무호흡지수)", min_value=0.0, max_value=100.0, step=0.1)
o2 = st.number_input("평균 혈중산소농도 (%)", min_value=50.0, max_value=100.0, step=0.1)

# 기존 코드...

if st.button("결과 보기"):
    rdi_result, o2_result = 진단_등급_텍스트(rdi, o2)

    st.subheader("🔍 진단 결과")
    st.write(f"➡️ 내 RDI: {rdi} → {rdi_result}")
    st.write(f"➡️ 내 평균 혈중산소농도: {o2}% → {o2_result}")

    st.markdown("---")
    st.markdown("### 🗂️ 기준 구간")
    st.markdown("**RDI 구간**")
    st.text("🟩 0~5: 정상\n🟨 5~15: 경도\n🟧 15~30: 중등도\n🟥 30 이상: 중증")
    st.markdown("**평균 혈중산소농도 구간**")
    st.text("🟥 0~85: 산소 저하\n🟧 85~90: 위험 수준\n🟨 90~95: 경계선 (주의)\n🟩 95~100: 정상")

    # 1. st.progress 막대
    st.markdown("#### RDI Progress")
    st.progress(int(rdi if rdi <= 100 else 100))
    st.markdown("#### O2 Progress")
    st.progress(int(o2 if o2 <= 100 else 100))

    # 3. HTML 막대 표시
    def color_bar(value, min_val, max_val, colors):
        pct = (value - min_val) / (max_val - min_val)
        idx = int(pct * (len(colors)-1))
        color = colors[idx]
        bar = f"<div style='width:100%;height:25px;background:linear-gradient(to right, {' ,'.join(colors)});'><div style='width:{pct*100}%;height:25px;background:{color};'></div></div>"
        return bar

    rdi_colors = ['#43a047','#fbc02d','#fb8c00','#e53935']
    st.markdown("#### RDI Color Bar")
    st.markdown(color_bar(rdi, 0, 100, rdi_colors), unsafe_allow_html=True)
