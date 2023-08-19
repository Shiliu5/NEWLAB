import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_exchange_rate(self, base_currency, target_currency):
        url = f"http://data.fixer.io/api/latest?access_key={self.api_key}&base={base_currency}&symbols={target_currency}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and data["success"]:
            return data["rates"][target_currency]
        else:
            print("获取汇率失败！")
            return None

    def convert(self, amount, base_currency, target_currency):
        exchange_rate = self.get_exchange_rate(base_currency, target_currency)

        if exchange_rate:
            converted_amount = amount * exchange_rate
            return converted_amount
        else:
            return None


def main():
    api_key = "YOUR_API_KEY"  # 替换为你的fixer.io API密钥
    converter = CurrencyConverter(api_key)

    while True:
        print("1. 汇率转换")
        print("2. 退出")
        choice = input("请选择操作：")

        if choice == "1":
            amount = float(input("请输入金额："))
            base_currency = input("请输入原始货币代码：")
            target_currency = input("请输入目标货币代码：")
            converted_amount = converter.convert(amount, base_currency, target_currency)

            if converted_amount:
                print(f"{amount} {base_currency} = {converted_amount} {target_currency}")
            else:
                print("汇率转换失败！")

        elif choice == "2":
            print("谢谢使用，再见！")
            break

        else:
            print("无效的选择，请重新输入！")


if __name__ == "__main__":
    main()
