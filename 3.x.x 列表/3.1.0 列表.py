#定义列表animal
animal = ['cat','dog','fish','pig']

#打印列表
print(animal)

#遍历列表
for i in range (0,3):
    print(animal[i])

#修改指定列表元素
animal[0] = 'human'
print('\n',animal)

#通过 del 删除元素
del animal[0]
print('\n',animal)

#可使用 append 将指定元素添加到列表末尾
animal.append('cat')
print('\n',animal)

#通过 insert 添加到指定位置，例如第三向位置，及2
animal.insert(2,'human')
print('\n',animal)

#使用 pop 删除指定元素，并指出
del_pop = animal.pop(2)   #与 del 不同之处
print('\n',animal)
print(f"删除的元素是：{del_pop}")

#不知道元素序号是多少？试试使用 remove('name') 删除
a = input("'dog', 'fish', 'pig', 'cat'选择一个删除")
#加入判定，输入检索不到时，返回ERROR
if a == 'cat':
    animal.remove(a)
    print(f"\n已删除{a},\n当前列表：{animal}")
elif a == 'dog':
    animal.remove(a)
    print(f"\n已删除{a},\n当前列表：{animal}")
elif a == 'pig':
    animal.remove(a)
    print(f"\n已删除{a},\n当前列表：{animal}")
elif a == 'fish':
    animal.remove(a)
    print(f"\n已删除{a},\n当前列表：{animal}")
else:
    print("ERROR")

