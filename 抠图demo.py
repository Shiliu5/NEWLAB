# 导入removebg模块
import removebg

# 创建一个RemoveBg对象，参数是你的API key
rmbg = removebg.RemoveBg("your_api_key", "error.log")

# 调用remove_background_from_img_file方法，参数是图片的路径
rmbg.remove_background_from_img_file("image.jpg")

#运行这段代码后，会在图片所在的文件夹生成一个新的图片，文件名是原来的图片名加上_no_bg.png后缀，这个图片就是抠好的透明背景图片。你可以用任何支持png格式的图片查看器或编辑器打开它，或者用Pillow等模块进行进一步的处理。如果你想批量处理多张图片，你可以用os模块遍历文件夹中的所有图片文件，然后用循环调用remove_background_from_img_file方法。
