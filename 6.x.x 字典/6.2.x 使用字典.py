'''创建字典 空'''
#先新建一个空字典
alien = {}


#添加键值对
alien['color'] = 'green'
alien['point'] = 5

#检验效果
print(alien)


'''尝试修改'''
print(f"\n现在，外星人的颜色是 {alien['color']}")     #检查当前颜色

#开始修改
alien['color'] = 'yellow'

#检验当前颜色
print(f"\n现在，外星人的颜色是 {alien['color']}")
print("修改成功")


'''删除键值对'''
del alien['color']
print(alien)                                      #检验效果


#类似的，当字典较长时，可以如下
alien_0 = {
    'height' : 180,
    'weight' : 100,
    'color'  : 'green',
    'point'  : 5
}
print(alien_0)


'''当你不确定字典里是否存在某个键值对时，可使用 get() '''
#检验 alien 是否存在 height
print(alien.get("height","Dont't Find It."))
#发现不存在，返回 default


