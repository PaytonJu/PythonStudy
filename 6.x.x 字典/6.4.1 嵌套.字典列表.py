alienS = []     #创建一个空列表

#生成 30 个外星人👽
for i in range(30):
    alien = {
        'height': 180,
        'weight': 100,
        'color': 'green',
        'point': 5
    }
    alienS.append(alien)
    print(f"Finish {i + 1}")

print("\n")    #美化结构

#遍历以检查
for a in alienS[:5]:     #只检查前五个
    print(a)
print(f"\n外星人的个数是 {len(alienS)} .")


'''此时，我们创建了 30 个外星人，使用 for 修改前三个'''
for alien in alienS[:3]:
    if alien['color'] == 'green':
        alien['height'] = 190
        alien['weight'] = 110
        alien['color'] = 'yellow'
        alien['point'] = 1

for a in alienS[:5]:     #只检查前五个
    print(a)