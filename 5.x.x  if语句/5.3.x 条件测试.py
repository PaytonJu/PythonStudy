# 定义一个字符串变量 car，赋值为 'subaru'
car = 'subaru'

# 打印一个预测语句，声称 car 等于 'subabu' 的结果为 True
# 注意：这里写的是 'subabu'，但实际比较的是下面的 'subaru'，所以预测是正确的
print("Is car == 'subabu'? I predict True.")
# 实际比较 car 是否等于字符串 'subaru'，因为 car 确实是 'subaru'，所以结果为 True
print(car == 'subaru')

# 打印一个空行，美化输出
print("\nIs car == 'audi'? I predict False.")
# 比较 car 是否等于 'audi'，因为 car 是 'subaru'，不等于 'audi'，所以结果为 False
print(car == 'audi')