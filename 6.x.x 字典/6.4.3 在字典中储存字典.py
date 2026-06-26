# 网站用户数据
site = {
    "users": {
        "uid_001": {
            "name": "小明",
            "posts": 12,
            "vip": True
        },
        "uid_002": {
            "name": "小红",
            "posts": 5,
            "vip": False
        }
    },
    "settings": {
        "theme": "dark",
        "lang": "zh"
    }
}

# 取值链
print(site["users"]["uid_001"]["name"])   # 小明
print(site["settings"]["theme"])           # dark