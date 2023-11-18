# 导入comtypes模块，用于调用Microsoft Word的COM接口
import comtypes.client

# 定义一个函数，接受一个word文件的路径，转换为pdf文件，并保存在同一目录下
def word_to_pdf(word_file):
    # 创建一个Word应用对象
    word = comtypes.client.CreateObject("Word.Application")
    # 设置为不可见，避免打开Word窗口
    word.Visible = False
    # 打开word文件
    doc = word.Documents.Open(word_file)
    # 获取文件名，不包括扩展名
    file_name = word_file.split(".")[0]
    # 生成pdf文件的路径，与word文件同一目录，扩展名为.pdf
    pdf_file = file_name + ".pdf"
    # 将word文件另存为pdf文件
    doc.SaveAs(pdf_file, FileFormat=17) # 17是pdf文件格式的代码
    # 关闭word文件
    doc.Close()
    # 退出Word应用
    word.Quit()

# 调用函数，示例代码，可以修改
word_to_pdf("test.docx")
