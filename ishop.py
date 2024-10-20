print("***Welcome to ishop calculator***")
basket =[]
item=[]
prices=[]
number =int(input(print("How many items are there in your basket today?")))
basket.append(number)
for i in  range(number):
  i=i+1
  print("Let´s get to counting them...")
  
  items = input(f"Please tell me the name of the item number {i}:").split(", ")
  item.append(items)
  price = int(input(print(f"What is the price of {items}:\n$")))
  prices.append(price)
choice = input(print("Would you  like to see how much it will cost?(Y/N)"))
if choice.lower() == "y":
  print(f"Buying these items will cost:\n {sum(prices)}")
  choice_1=input(print("Do you want ro see your entire basket items:(Y/N)"))
  if choice_1.lower() == "y":
    print(f"{item}")