import time
start_time = time.time()

a = 0

for i in range(1,10000001):
    a = i + int(a)
    print(f"a的值为 {a}")

end_time = time.time()
elapsed_time = end_time - start_time


print(f"程序运行时间: {elapsed_time:.4f} 秒")
print(f"程序运行时间: {elapsed_time*1000:.2f} 毫秒")