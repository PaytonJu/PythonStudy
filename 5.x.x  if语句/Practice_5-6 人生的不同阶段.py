import  sys

#请求输入
your_age = input("你的年龄：")

#首先对输入 your_age 进行检验
try:
    age = int(your_age)          # 尝试转换
    # 转换成功，说明是整数，继续后续操作
    print(f"你输入的年龄是：{age}")
except ValueError:
    # 转换失败，说明不是整数
    print("\n输入错误，请输入整数！")
    sys.exit(1)

#若检验成功继续执行代码
#判定年龄阶段
if age < 2:
    print("你是婴儿")             #当输入年龄小于 2 时
elif age >= 2 and age < 4:
    print("你是幼儿")             #当输入年龄大于等于 2 小于 4 时
elif age >= 4 and age < 13:
    print("你是儿童")             #当输入年龄大于等于 4 小于 13 时
elif age >= 13 and age < 20:
    print("你是青少年")           #当输入年龄大于等于 13 小于 20 时
elif age >= 20 and age < 65:
    print("你是成年人")           #当输入年龄大于等于 20 小于65 时
else:
    print("你是老年人")             #当输入年龄大于等于 65 时

print("\n本次程序运行结束，返回值0")
