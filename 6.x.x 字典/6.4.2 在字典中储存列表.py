# 一个key对应一个列表
student = {
    "name": "小明",
    "hobbies": ["打游戏", "踢球", "看番"],
    "scores": [95, 88, 92]
}

# 怎么取
print(student["hobbies"])          # ['打游戏', '踢球', '看番']
print(student["hobbies"][0])       # 打游戏
print(student["scores"][-1])       # 92