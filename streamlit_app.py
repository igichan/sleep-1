import streamlit as st
import pandas as pd

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
    elif O2 > 85:
        o2_등급 = "🟧 위험 수준"
    else:
        o2_등급 = "🟥 산소 저하"

    return rdi_등급, o2_등급

def draw_bar(value, ranges, colors, bar_length=40):
    bar_html = ""
    marker_pos = 0
    total = 0
    for i, (start, end) in enumerate(ranges):
        seg_len = int((end-start)/(ranges[-1][1]-ranges[0][0]) * bar_length)
        color = colors[i]
        if value >= start and value < end:
            marker_pos = total + int(seg_len * (value-start)/(end-start))
        bar_html += f"<span style='background:{color};'>{'&nbsp;'*seg_len}</span>"
        total += seg_len
    # 마커 찍기 (●)
    bar_html = bar_html[:marker_pos*6] + "<b>●</b>" + bar_html[marker_pos*6+6:]
    return bar_html

def highlight_row(row, value, start, end):
    color = 'background-color: #ffd700' if value >= start and value < end else ''
    return [color]*len(row)

st.title("🩺 수면무호흡 진단기")

rdi = st.number_input("RDI (수면무호흡지수)", min_value=0.0, max_value=100.0, step=0.1)
o2 = st.number_input("평균 혈중산소농도 (%)", min_value=50.0, max_value=100.0, step=0.1)

if st.button("결과 보기"):
    rdi_result, o2_result = 진단_등급_텍스트(rdi, o2)

    st.subheader("🔍 진단 결과")
    st.write(f"➡️ 내 RDI: {rdi} → {rdi_result}")
    st.write(f"➡️ 내 평균 혈중산소농도: {o2}% → {o2_result}")

    st.markdown("---")

    # 1. 색상 Bar + 마커
    st.markdown("#### RDI 구간 (시각 막대)")
    rdi_ranges = [(0,5),(5,15),(15,30),(30,100)]
    rdi_colors = ['#43a047','#fbc02d','#fb8c00','#e53935']
    st.markdown(draw_bar(rdi, rdi_ranges, rdi_colors), unsafe_allow_html=True)

    st.markdown("#### O2 구간 (시각 막대)")
    o2_ranges = [(0,85),(85,90),(90,95),(95,100)]
    o2_colors = ['#e53935','#fb8c00','#fbc02d','#43a047']
    st.markdown(draw_bar(o2, o2_ranges, o2_colors), unsafe_allow_html=True)

    # 2. 구간별 표
    rdi_table = pd.DataFrame({
        '구간': ['0~5', '5~15', '15~30', '30 이상'],
        '등급': ['정상', '경도', '중등도', '중증'],
        '설명': ['수면무호흡 없음', '경도 수면무호흡증', '중등도 수면무호흡증', '중증 수면무호흡증']
    })
    st.markdown("#### RDI 구간표")
    rdi_bounds = [(0,5),(5,15),(15,30),(30,100)]
    st.dataframe(rdi_table.style.apply(lambda x: highlight_row(x, rdi, *rdi_bounds[x.name]), axis=1))

    o2_table = pd.DataFrame({
        '구간': ['0~85', '85~90', '90~95', '95~100'],
        '등급': ['산소 저하', '위험 수준', '경계선', '정상'],
        '설명': ['저산소 위험', '경계선', '주의 필요', '정상']
    })
    st.markdown("#### O2 구간표")
    o2_bounds = [(0,85),(85,90),(90,95),(95,100)]
    st.dataframe(o2_table.style.apply(lambda x: highlight_row(x, o2, *o2_bounds[x.name]), axis=1))

    # 3. 구간별 슬라이더
    st.markdown("#### RDI 슬라이더")
    st.slider("RDI 위치", min_value=0.0, max_value=100.0, value=rdi, disabled=True)

    st.markdown("#### O2 슬라이더")
    st.slider("O2 위치", min_value=0.0, max_value=100.0, value=o2, disabled=True)
