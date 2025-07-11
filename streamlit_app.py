import tkinter as tk

def diagnose():
    try:
        RDI = float(entry_rdi.get().replace(",", "."))
        O2 = float(entry_o2.get().replace(",", "."))
    except ValueError:
        결과창.config(text="숫자만 입력하세요. (예: 17.2 / 91.5)")
        return

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

    결과창.config(text=결과)

root = tk.Tk()
root.title("수면무호흡증 판별 모의 프로그램")
root.geometry("360x240")

tk.Label(root, text="RDI (수면무호흡지수)").pack(pady=5)
entry_rdi = tk.Entry(root)
entry_rdi.pack()

tk.Label(root, text="평균 혈중 산소농도 (%)").pack(pady=5)
entry_o2 = tk.Entry(root)
entry_o2.pack()

tk.Button(root, text="결과 보기", command=diagnose).pack(pady=10)
결과창 = tk.Label(root, text="", justify="left")
결과창.pack()

root.mainloop()
