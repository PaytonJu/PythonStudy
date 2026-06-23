#定义外星人颜色
alien_color = 'green'

#判定颜色，如果为 'green' ,加五分
if alien_color == 'green':
    print("加五分")


#修改外新人颜色使判定不通过
alien_color = 'yellow'   #修改颜色为 'yellow'

#同上，进行判定
if alien_color == 'green':
    print("加五分")
#若无输出，则为 Flase

print("\n本次程序运行结束，返回值0")