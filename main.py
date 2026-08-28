stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 500
}

portfolio = []
total_investment = 0

while True:
    stock_name = input("Enter your stock name (or type 'DONE' to finish): ").upper()


    if stock_name == "DONE":
        break
    quantity = int(input("Enter your quantity: "))

    if stock_name not in stock_prices:
        print("the stock name does not exist! ")
        continue


    price = stock_prices[stock_name]

    investment = quantity * price

    portfolio.append({
        "name": stock_name,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })
    total_investment += investment

print("\n========== PORTFOLIO ==========")

for stock in portfolio:
    print(
        f"{stock['name']} | "
        f"{stock['quantity']} shares | "
        f"${stock['price']} | "
        f"${stock['investment']}"
    )
print("______________________________________\n")
print(f"Total investment: {total_investment}")


with open("portfolio.txt", "w") as file:
    file.write("========== STOCK PORTFOLIO ==========\n\n")

    for stock in portfolio:
        file.write(
            f"{stock['name']} | "
            f"{stock['quantity']} shares | "
            f"${stock['price']} | "
            f"${stock['investment']}\n"
        )

    file.write("\n")
    file.write(f"Total investment: ${total_investment}\n")

print("\nPortfolio saved to portfolio.txt")