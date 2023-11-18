# 导入datetime模块，用于处理日期和时间
import datetime

# 定义一个Todo类，表示一个待办事项
class Todo:
    # 构造方法，接受事项名称和截止日期
    def __init__(self, name, deadline):
        self.name = name # 事项名称
        self.deadline = deadline # 截止日期，是一个datetime对象
        self.done = False # 事项是否完成，初始为False

    # 返回事项的剩余时间，单位为秒
    def get_remaining_time(self):
        # 如果事项已完成，返回0
        if self.done:
            return 0
        # 否则，返回当前时间和截止日期的差值的总秒数
        else:
            return (self.deadline - datetime.datetime.now()).total_seconds()

    # 返回事项的字符串表示，包括名称，截止日期和剩余时间
    def __str__(self):
        # 如果事项已完成，返回名称和"已完成"
        if self.done:
            return f"{self.name} - 已完成"
        # 否则，返回名称，截止日期和剩余时间
        else:
            # 将剩余时间转换为时分秒的格式
            remaining_time = self.get_remaining_time()
            hours = int(remaining_time // 3600)
            minutes = int((remaining_time % 3600) // 60)
            seconds = int(remaining_time % 60)
            # 返回字符串
            return f"{self.name} - 截止日期：{self.deadline} - 剩余时间：{hours}小时{minutes}分钟{seconds}秒"

# 定义一个TodoList类，表示一个待办事项列表
class TodoList:
    # 构造方法，接受一个列表作为初始的待办事项
    def __init__(self, todos=None):
        # 如果没有传入参数，就创建一个空列表
        if todos is None:
            self.todos = []
        # 否则，将参数赋值给self.todos
        else:
            self.todos = todos

    # 添加一个待办事项到列表中
    def add(self, todo):
        self.todos.append(todo)

    # 完成一个待办事项，将其done属性设为True
    def finish(self, todo):
        todo.done = True

    # 返回列表中未完成的待办事项的数量
    def get_unfinished_count(self):
        # 使用列表推导式，筛选出未完成的待办事项
        unfinished_todos = [todo for todo in self.todos if not todo.done]
        # 返回列表的长度
        return len(unfinished_todos)

    # 返回列表中的字符串表示，每个待办事项占一行
    def __str__(self):
        # 使用换行符连接每个待办事项的字符串表示
        return "\n".join([str(todo) for todo in self.todos])

# 创建一个待办事项列表的实例
todo_list = TodoList()

# 添加一些待办事项到列表中，示例代码，可以修改
todo_list.add(Todo("学习python",
                   datetime.datetime(2023, 11, 30, 23, 59, 59))) # 截止日期为2023年11月30日23点59分59秒
todo_list.add(Todo("看电影",
                   datetime.datetime(2023, 11, 20, 20, 0, 0))) # 截止日期为2023年11月20日20点
todo_list.add(Todo("打扫房间",
                   datetime.datetime(2023, 11, 19, 12, 0, 0))) # 截止日期为2023年11月19日12点

# 打印待办事项列表
print(todo_list)

# 完成一个待办事项，示例代码，可以修改
todo_list.finish(todo_list.todos[1]) # 完成第二个待办事项

# 打印待办事项列表
print(todo_list)

# 打印未完成的待办事项的数量
print(f"还有{todo_list.get_unfinished_count()}个待办事项未完成")
