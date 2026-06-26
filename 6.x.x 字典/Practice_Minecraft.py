#新建字典
server_0 = {
    "name" : "PaytonServer",                                  #我的服务器名称
    "version" : "1.20.1",                                     #游戏版本
    "online" : True,                                          #在线情况
    "player" : {                                              #嵌套 玩家信息
        "Me": {                                               #名字 我
            "level": 999,                                     #等级
            "hp": 20,                                         #血量
            "items": ["钻石剑", "面包", "末影珍珠"],          #物品栏信息
            "coordinates": {"x": 0, "y": 0, "z": 0}           #坐标
        },
        "DXN": {                                              #同上，再次不一一赘述
            "level": 0,
            "hp": 20,
            "items": ["钻石剑", "面包", "床"],
            "coordinates": {"x": 1000, "y": 50, "z": -1000}
        }
    },
}

#查询 Me 的血量是多少
Me_HP = server_0["player"]["Me"]["hp"]                      #获取血量
print(f"我的血量是 {Me_HP}")                                  #打印

server_0["player"]["DXN"]["coordinates"]["y"] = 51.2        #修改 DXN 对应的 Y 轴坐标，使她跳起来

server_0["player"]["Me"]["items"].append("盾牌")             # 在我的物品栏里增加 盾牌

#打印字典
print(f"\n{server_0}")

print(f"\n")

#打印所有玩家的 名字 和 坐标
for players in server_0["player"]:
    c = server_0["player"][players]["coordinates"]
    print(f"玩家 {players} 的坐标是：X：{c['x']} Y：{c['y']} Z：{c['z']}")

'''
或者说，更加优雅的方式

for name, info in server_0["player"].items():
    c = info["coordinates"]
    print(f"玩家 {name} 的坐标：{c['x']}, {c['y']}, {c['z']}")

'''