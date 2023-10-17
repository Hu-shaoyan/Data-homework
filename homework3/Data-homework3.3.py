import re
id=input("请输入身份证号码：")
pattern=r'^[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[1-2]\d|30|31)\d{3}[0-9Xx]$'
if re.match(pattern,id):
    print("合法")
else:
    print("不合法")
