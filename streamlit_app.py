# 한글 폰트 설정 (Colab)
!apt-get -qq install fonts-nanum > /dev/null
import matplotlib.pyplot as plt

plt.rc('font', family='NanumGothic')
plt.rcParams['axes.unicode_minus'] = False

def diagnose_and_plot(RDI, O2):
    # 1. 진단 결과 출력
    result = ""

    if RDI < 5:
        result += "🟢 RDI: 정상 (수면무호흡 없음)\n"
    elif RDI < 15:
        result += "🟡 RDI: 경도 수면무호흡증\n"
    elif RDI < 30:
        result += "🟠 RDI: 중등도 수면무호흡증\n"
    else:
        result += "🔴 RDI: 중증 수면무호흡증\n"

    if O2 >= 95:
        result += "🟢 평균 혈중 산소농도: 정상"
    elif O2 >= 90:
        result += "🟡 평균 혈중 산소농도: 다소 낮음 (주의 필요)"
    elif O2 >= 85:
        result += "🟠 평균 혈중 산소농도: 낮음 (위험)"
    else:
        result += "🔴 평균 혈중 산소농도: 매우 낮음 (중증 산소저하 가능성)"

    print("📋 [진단 결과]")
    print(result)

    # 2. RDI 그래프
    plt.figure(figsize=(8, 2))
    plt.title("RDI 수면무호흡지수 구간")

    plt.axvspan(0, 5, color="green", alpha=0.3, label="정상")
    plt.axvspan(5, 15, color="yellow", alpha=0.3, label="경도")
    plt.axvspan(15, 30, color="orange", alpha=0.3, label="중등도")
    plt.axvspan(30, 40, color="red", alpha=0.3, label="중증")

    plt.axvline(RDI, color="black", linewidth=2, label=f"내 RDI: {RDI}")
    plt.xlim(0, 40)
    plt.yticks([])
    plt.legend(loc="upper left")
    plt.xlabel("RDI 수치")
    plt.grid(axis='x')
    plt.show()

    # 3. 산소농도 그래프
    plt.figure(figsize=(8, 2))
    plt.title("산소농도 구간 (%)")

    plt.axvspan(0, 85, color="red", alpha=0.3, label="매우 낮음")
    plt.axvspan(85, 90, color="orange", alpha=0.3, label="낮음")
    plt.axvspan(90, 95, color="yellow", alpha=0.3, label="다소 낮음")
    plt.axvspan(95, 100, color="green", alpha=0.3, label="정상")

    plt.axvline(O2, color="black", linewidth=2, label=f"내 산소농도: {O2}%")
    plt.xlim(80, 100)
    plt.yticks([])
    plt.legend(loc="upper left")
    plt.xlabel("평균 산소농도 (%)")
    plt.grid(axis='x')
    plt.show()


# 사용자 입력 받기
try:
    RDI = float(input("RDI (수면무호흡지수)를 입력하세요: ").replace(",", "."))
    O2 = float(input("평균 산소농도 (%)를 입력하세요: ").replace(",", "."))
    diagnose_and_plot(RDI, O2)
except ValueError:
    print("❌ 숫자만 입력하세요. 예: 17.2 / 91.5")
