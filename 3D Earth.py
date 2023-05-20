import vtk

# 创建一个球体表示地球
earth = vtk.vtkSphereSource()
earth.SetRadius(1.0)
earth.SetThetaResolution(100)
earth.SetPhiResolution(100)

# 创建一个纹理映射器
texture_mapper = vtk.vtkTextureMapToSphere()
texture_mapper.SetInputConnection(earth.GetOutputPort())
texture_mapper.PreventSeamOn()

# 读取地球纹理图片
texture = vtk.vtkTexture()
texture.InterpolateOn()
texture.SetInputConnection(vtk.vtkJPEGReader().SetFileName("earth.jpg").GetOutputPort())

# 创建一个多边形数据映射器
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(texture_mapper.GetOutputPort())

# 创建一个演员
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.SetTexture(texture)

# 创建一个渲染器
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(0.1, 0.1, 0.1)

# 创建一个窗口
window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)
window.SetSize(800, 800)

# 创建一个交互式渲染器
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)

# 开始交互渲染
interactor.Initialize()
interactor.Start()

#注意：这个示例需要一个名为earth.jpg的地球纹理图片。你可以在网上找到许多免费的资源，将其下载并保存在与代码相同的目录中。
