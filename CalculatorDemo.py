import math

print("欢迎使用Python计算器")

while True:
    print("请选择要进行的操作：")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("5. 平方根")
    print("6. 退出")

    choice = input("请输入您的选择（1/2/3/4/5/6）：")

    if choice == '1':
        num1 = float(input("请输入第一个数字： "))
        num2 = float(input("请输入第二个数字： "))
        print("结果：", num1 + num2)

    elif choice == '2': 
      num1 = float(input("请输入第一个数字： ")) 
      num2 = float(input("请输入第二个数字： ")) 
      print("结果：", num1 - num2)
    elif choice == '3':
      num1 = float(input("请输入第一个数字： "))
      num2 = float(input("请输入第二个数字： "))
      print("结果：", num1 * num2)

    elif choice == '4':
      num1 = float(input("请输入第一个数字： "))
      num2 = float(input("请输入第二个数字： "))
      if num2 == 0:
        print("除数不能为0！")
    else:
        print("结果：", num1 / num2)

    elif choice == '5':
      num = float(input("请输入一个数字： "))
      if num < 0:
        print("负数没有实数平方根！")
    else: 
      print("结果：", math.sqrt(num))
    elif choice == '6':
    print("感谢使用Python计算器！")
    break

else:
    print("无效的选择，请重新输入。")
