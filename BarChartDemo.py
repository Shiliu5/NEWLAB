import matplotlib.pyplot as plt

# 定义数据
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 24, 36, 40, 15]

# 绘制柱状图
plt.bar(x, y)

# 添加标题和标签
plt.title('柱状图示例')
plt.xlabel('X轴标签')
plt.ylabel('Y轴标签')

# 显示图形
plt.show()
