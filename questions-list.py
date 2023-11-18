# 导入csv模块，用于处理csv文件
import csv

# 定义一个Question类，表示一个问卷问题
class Question:
    # 构造方法，接受问题内容和选项列表
    def __init__(self, content, options):
        self.content = content # 问题内容，是一个字符串
        self.options = options # 选项列表，是一个字符串列表
        self.answer = None # 用户的答案，初始为None

    # 显示问题和选项
    def show(self):
        # 打印问题内容
        print(self.content)
        # 遍历选项列表，打印每个选项的序号和内容
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

    # 获取用户的答案
    def get_answer(self):
        # 用一个循环，直到用户输入有效的答案
        while True:
            # 提示用户输入答案的序号
            answer = input("请输入你的答案的序号：")
            # 尝试将答案转换为整数
            try:
                answer = int(answer)
            # 如果出现异常，说明答案不是一个数字，打印错误信息，继续循环
            except ValueError:
                print("答案必须是一个数字，请重新输入。")
                continue
            # 如果答案的序号不在选项列表的范围内，打印错误信息，继续循环
            if answer < 1 or answer > len(self.options):
                print("答案的序号必须在选项列表的范围内，请重新输入。")
                continue
            # 如果答案有效，跳出循环
            break
        # 将用户的答案赋值给self.answer
        self.answer = answer

# 定义一个Survey类，表示一个问卷
class Survey:
    # 构造方法，接受一个问题列表
    def __init__(self, questions):
        self.questions = questions # 问题列表，是一个Question对象的列表

    # 显示问卷
    def show(self):
        # 遍历问题列表，显示每个问题
        for question in self.questions:
            question.show()

    # 获取用户的答案
    def get_answers(self):
        # 遍历问题列表，获取每个问题的答案
        for question in self.questions:
            question.get_answer()

    # 保存问卷结果到本地csv文件
    def save_results(self, filename):
        # 以写入模式打开文件
        with open(filename, "w", newline="") as file:
            # 创建一个csv写入对象
            writer = csv.writer(file)
            # 写入一行表头，包括问题内容和用户答案
            writer.writerow(["问题内容", "用户答案"])
            # 遍历问题列表，写入每个问题的内容和答案
            for question in self.questions:
                writer.writerow([question.content, question.answer])
            # 关闭文件
            file.close()

# 创建一个问卷的实例
survey = Survey([
    Question("你喜欢什么颜色？", ["红色", "绿色", "蓝色", "黄色"]),
    Question("你喜欢什么动物？", ["猫", "狗", "兔子", "鸟"]),
    Question("你喜欢什么水果？", ["苹果", "香蕉", "橘子", "葡萄"])
])

# 显示问卷
survey.show()

# 获取用户的答案
survey.get_answers()

# 保存问卷结果到本地csv文件
survey.save_results("survey_results.csv")
