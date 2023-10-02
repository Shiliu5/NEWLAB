# 定义敏感词列表
sensitive_words = ["敏感词1", "敏感词2", "敏感词3"]  # 替换成实际的敏感词列表

# 定义一个函数来检查文本中是否包含敏感词
def check_for_sensitive_words(text):
    for word in sensitive_words:
        if word in text:
            return True
    return False

# 输入待检查的文本
input_text = input("请输入要检查的文本：")

# 检查文本是否包含敏感词
if check_for_sensitive_words(input_text):
    print("文本包含敏感词，需要筛查。")
else:
    print("文本合规，无需筛查。")
