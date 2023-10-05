import turtle

length = 5 # 线段长度
angle = 90 # 角度
setup(1280 ,720) # 设置画布大小
up() # 提起画笔
goto(300 , -100) # 移动到指定位置
down() # 落下画笔

def draw_path(path):
    for symbol in path:
        if symbol == 'f':
            import random
            colormode(255) # 设置颜色模式为RGB
            color(random.randint(0 ,255) , random.randint(0 ,255) , random.randint(0 ,255)) # 随机设置颜色
            fd(length) # 向前走一段距离
        elif symbol == '-':
            lt(angle) # 左转一定角度
        elif symbol == '+':
            rt(angle) # 右转一定角度

def apply_path(rules , path):
    lit = [x for x in path] # 把字符串转换成列表
    for i in range(len(lit)):
        symbol = lit[i]
        if symbol == 'x':
            lit[i] = rules[symbol] # 把x替换成规则中对应的字符串
        elif symbol == 'y':
            lit[i] = rules[symbol] # 把y替换成规则中对应的字符串
    path = ''.join(lit) # 把列表转换成字符串
    return path

rules = {
    'x':'x+yf+' , # x的替换规则
    'y':'-fx-y' # y的替换规则
}
path = 'fx' # 初始路径
speed(0) # 设置速度为最快
for i in range(13):
    path = apply_path(rules , path) # 重复应用规则13次
draw_path(path) # 绘制路径
done() # 结束绘图
