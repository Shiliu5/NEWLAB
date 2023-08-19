class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("余额不足！")

    def get_balance(self):
        return self.balance


def main():
    account = Account()

    while True:
        print("1. 存款")
        print("2. 取款")
        print("3. 查询余额")
        print("4. 退出")
        choice = input("请选择操作：")

        if choice == "1":
            amount = float(input("请输入存款金额："))
            account.deposit(amount)
            print("存款成功！")

        elif choice == "2":
            amount = float(input("请输入取款金额："))
            account.withdraw(amount)
            print("取款成功！")

        elif choice == "3":
            balance = account.get_balance()
            print("当前余额为：", balance)

        elif choice == "4":
            print("谢谢使用，再见！")
            break

        else:
            print("无效的选择，请重新输入！")


if __name__ == "__main__":
    main()
