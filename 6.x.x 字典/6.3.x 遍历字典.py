# 创建字典（而不是列表）
alien_0 = {
    'height': 180,
    'weight': 100,
    'color': 'green',
    'point': 5
}
print(alien_0)  # 打印整个字典

# 遍历字典的键值对
for key, info in alien_0.items():
    print(f"\nKey: {key}")
    print(f"Information: {info}")   # 这里也建议把值打印出来


