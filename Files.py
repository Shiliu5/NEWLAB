import os

def search_files(directory, keyword):
    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if keyword in filename:
                matches.append(os.path.join(root, filename))
    return matches

# 输入要搜索的目录和关键字
directory = input("请输入要搜索的目录：")
keyword = input("请输入要搜索的关键字：")

# 调用搜索函数并打印结果
results = search_files(directory, keyword)
if results:
    print("找到以下匹配的文件：")
    for file in results:
        print(file)
else:
    print("未找到匹配的文件。")
