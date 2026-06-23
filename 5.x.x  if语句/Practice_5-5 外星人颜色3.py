#版本1，触发 if
#定义外星人颜色
alien_color = 'green'

if alien_color == 'green':
    print("加五分")     #判定为绿色加五分
elif alien_color == 'yellow':
    print("加十分")     #判定为黄色加十分
else:
    print("加十五分")   #判定为红色加十分


#版本2，触发 elif
#定义外星人颜色
alien_color = 'yellow'

if alien_color == 'green':
    print("加五分")     #判定为绿色加五分
elif alien_color == 'yellow':
    print("加十分")     #判定为黄色加十分
else:
    print("加十五分")   #判定为红色加十分


#版本3，触发 else
#定义外星人颜色
alien_color = 'red'

if alien_color == 'green':
    print("加五分")     #判定为绿色加五分
elif alien_color == 'yellow':
    print("加十分")     #判定为黄色加十分
else:
    print("加十五分")   #判定为红色加十分


'''类似的，我们可以将下列代码修改
else:
    print("加十五分")   #判定为红色加十分

修改为
elif alien_color == 'red':
    print("加十五分")   #判定为红色加十分

运行结果同上
结论，可以用 elif 代替 else
'''

print("\n本次程序运行结束，返回值0")