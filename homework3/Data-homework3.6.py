a=int(input("请输入考试成绩"))
if a>=0 and a<60:
    print("不合格")
elif a>60 and a<=74:
    print("合格")
elif a>74 and a<90:
    print("良好")
elif a>=90 and a<=100:
    print("优秀")
