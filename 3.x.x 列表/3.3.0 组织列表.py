#定义列表animal
animal = ['cat','fish','dog','pig']

#使用 .sort 永久排序
animal.sort()
print(animal)                             #打印列表

#类似的可以用 .sort(reverse=True) 反向排序
animal.sort(reverse=True)
print('\n',animal)     #打印列表


#######################
#有永久排序，就有临时排序
#比如 sortde()
#同上不在此演示


#######################
#可以使用 len() 数
num = len(animal)                         #令 num 为 元素数量
print(f"列表 animal 的项目数量为 {num}")     #打印数量在屏幕上
