import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# 创建一个3D坐标系
fig = plt.figure()
ax = plt.axes(projection='3d')

# 定义三维数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10] 
z = [3, 6, 9, 12, 15]

#绘制3D散点图
ax.scatter3D(x, y, z, c=z, cmap='Reds')

#添加坐标轴标签和标题
ax.set_xlabel('X Label') ax.set_ylabel('Y Label') ax.set_zlabel('Z Label') ax.set_title('3D Scatter Plot')

#显示图形
plt.show()
