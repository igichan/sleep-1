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

def highlight_row(row, value, start, end):
    color = 'background-color: #ffd700' if value >= start and value < end else ''
    return [color]*len(row)

def gradient_bar(min_val, max_val, value, ranges, colors, labels):
    bar_width = 400
    bar_height = 28
    marker_pos = int(bar_width * (value-min_val)/(max_val-min_val))
    gradient = ','.join(colors)
    stops = ""
    for i, (start, end) in enumerate(ranges):
        left = int(bar_width * (start-min_val)/(max_val-min_val))
        right = int(bar_width * (end-min_val)/(max_val-min_val))
        mid = (left + right) // 2
        stops += f"<span style='position:absolute;left:{mid-15}px;top:{bar_height+2}px;color:{colors[i]};font-weight:bold;'>{start}~{end}<br>{labels[i]}</span>"
    html = f"""
    <div style='position:relative;width:{bar_width}px;height:{bar_height+32}px;'>
      <div style='width:{bar_width}px;height:{bar_height}px;border-radius:8px;background:linear-gradient(to right, {gradient});'></div>
      <div style='position:absolute;left:{marker_pos-8}px;top:0;'><span style='font-size:24px;'>▲</span></div>
      {stops}
    </div>
    """
    return html

st.title("🩺 수면무호흡증 모의 분석")

rdi = st.number_input("RDI (수면무호흡지수)", min_value=0.0, max_value=100.0, step=0.1)
o2 = st.number_input("평균 혈중산소농도 (%)", min_value=50.0, max_value=100.0, step=0.1)

if st.button("결과 보기"):
    rdi_result, o2_result = 진단_등급_텍스트(rdi, o2)

    st.markdown("---")

    # 1. 구간별 표
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

    # 2. 위험도 그라데이션 바

    def gradient_bar(min_value, max_value, value, ranges, colors, labels):
    bar_width = 600  # 기존보다 크게 (예: 300 → 600)
    # 아래 HTML/CSS에서 width:600px; 처럼 반영
    html = f'''
    <div style="width:{bar_width}px; height:30px; ...">
      <!-- 그라데이션 영역 -->
    </div>
    '''
    # 이하 기타 코드...
    return html

    
    st.markdown("##### RDI 위험도 그라데이션")
    rdi_ranges = [(0,5),(5,15),(15,30),(30,100)]
    rdi_colors = ['#43a047','#fbc02d','#fb8c00','#e53935']
    st.markdown(gradient_bar(0, 100, rdi, rdi_ranges, rdi_colors, ['정상','경도','중등도','중증']), unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
                
    st.markdown("##### 혈중산소농도 위험도 그라데이션")
    o2_ranges = [(0,85),(85,90),(90,95),(95,100)]
    o2_colors = ['#e53935','#fb8c00','#fbc02d','#43a047']
    st.markdown(gradient_bar(0, 100, o2, o2_ranges, o2_colors, ['저하','위험','경계','정상']), unsafe_allow_html=True)
