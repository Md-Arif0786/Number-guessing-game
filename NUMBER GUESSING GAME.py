#!/usr/bin/env python
# coding: utf-8

# <h1 style="color:blue;"># FAST PROJECT = MINI GAME FOR CODING
# # DATE = 23/03/2026
# # AAJ MUJHE SHAMJH AAYA KE PROJECT KIS TARH SHE KAAM KARTA HAIII</h1>

# In[ ]:


import random
secret = random.randint(1,10)
guess = int(input("guess number(1-10):"))
if guess == secret:
    print("currect guess❤️")
else:
    print("wrong guess😒")
    print("number was:👌", secret)


# <h1 style="color:blue;">USER SHE IMPORT LEKE AND KA USE KAR KE LOGIN KARWANA</h1>

# In[ ]:


username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    otp = input("Enter OTP: ")
    
    if otp == "0000":
        print("LOGIN SUCCESSFUL 😎")
    else:
        print("Wrong OTP ❌")
else:
    print("Wrong Username or Password ❌")


# <h1 style="color:blue;"> ☆☆☆THE MORNING STAR CAFE PROJECT☆☆☆ </h1>
# MADE BY = ☆ARIF ABBAS☆

# In[ ]:


menu = {
    "fulvic water": 200,
    "espresso": 180,
    "cappuccino": 280,
    "latte": 300,
    "americano": 210,
    "mocha": 350,
    "flat white": 300,
    "cold brew": 350,
    "macchiato": 350,
    "frappé": 450,
    "irish coffee": 700,
    "dalgona": 250,
    "turkish coffee": 400,
    "cortado": 280,
    "vienna coffee": 350,
    "galao": 300,
    "kopi luwak": 10000
}

total = 0
print("----------------------------------------------------☆The--Morning---Star☆--------------------------------------------------------------------")
print("___________________________________________________________Coffee_____________________________________________________________________________")
print("------------------------------------------------------------Cafe------------------------------------------------------------------------------")
print("____________________________________________________________✭✭✭______________________________________________________________________________")
print("\nHERE IS MENU☕:")
print("                                                                                   ")
for item,price in menu.items():
    print(f"{item.title()} : {price}")
    
while True:
    order = input("\nChoose an item (or type 'exit' to finish):").lower().strip()
    if order == "exit":
        print("exiting the program")
        break
    if order in menu:
        print("item added successfully:")
        total += menu[order]
    else:
        print("invalid input! please choose item from the menu:")

print("\nThanks for visiting:") 
print("Your Total Bill is",total)


# <h1 style="color:blue;"> ☆☆☆THE MORNING STAR CAFE PROJECT☆☆☆ </h1>
# PROJECT = 2 = ADD = QNT

# In[ ]:


menu = {
    "fulvic water": 200,
    "espresso": 180,
    "cappuccino": 280,
    "latte": 300,
    "americano": 210,
    "mocha": 350,
    "flat white": 300,
    "cold brew": 350,
    "macchiato": 350,
    "frappé": 450,
    "irish coffee": 700,
    "dalgona": 250,
    "turkish coffee": 400,
    "cortado": 280,
    "vienna coffee": 350,
    "galao": 300,
    "kopi luwak": 10000
}

total = 0
print("-------------------------------☆The--Morning---Star☆------------------------------")
print("_____________________________________Coffee________________________________________")
print("--------------------------------------Cafe-----------------------------------------")
print("______________________________________✭✭✭_________________________________________")
print("\nHERE IS MENU☕:")
print("                                                                                   ")
for item,price in menu.items():
    print(f"{item.title()} : {price}")
    
while True:
    order = input("\nChoose an item (or type 'exit' to finish):").lower().strip()
    if order == "exit":
        print("exiting the program")
        break
    if order in menu:
        qty = int(input("Enter Quantity:"))
        total = menu[order]
        item_total = price * qty
        total += item_total

        print(f"{order.title()} {qty} = {item_total}")
    else:
        print("invalid input! please choose item from the menu:")

print("\nThanks for visiting❤️❤️:") 
print("Your Total Bill is",total)


# <h1 style="color:blue;"> ☆☆☆THE MORNING STAR CAFE PROJECT☆☆☆ </h1>
# **PROJECT 3 = ADD = QNT + GST**

# In[ ]:


# ==========================
# ☕ THE MORNING STAR CAFE ☕
# ==========================

menu = {
    "filter coffee": 200,
    "espresso": 180,
    "cappuccino": 280,
    "latte": 300,
    "americano": 210,
    "mocha": 350,
    "flat white": 300,
    "cold brew": 350,
    "macchiato": 350,
    "frappe": 450,
    "irish coffee": 700,
    "dalgona": 250,
    "turkish coffee": 400,
    "cortado": 280,
    "vienna coffee": 350,
    "galao": 300,
    "kopi luwak": 10000
}

total = 0
order_list = []

print("=" * 60)
print("              ☕ THE MORNING STAR CAFE ☕")
print("=" * 60)
print("               Welcome to Our Coffee Cafe")
print("=" * 60)
print("\n📋 MENU:\n")

# Display Menu
for item, price in menu.items():
    print(f"{item.title():20} : ₹{price}")

print("-" * 60)

# Order Loop
while True:

    order = input("\nChoose an item (or type 'exit' to finish): ").lower().strip()

    if order == "exit":
        print("\nPreparing your bill...\n")
        break

    if order in menu:

        try:
            qty = int(input("Enter Quantity : "))

            if qty <= 0:
                print("❌ Quantity must be greater than 0.")
                continue

        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        price = menu[order]
        item_total = price * qty
        total += item_total

        order_list.append((order.title(), qty, item_total))

        print(f"✅ {order.title()} x {qty} = ₹{item_total} added successfully.")

    else:
        print("❌ Item not available in the menu.")

# GST
gst_rate = 5
gst_amount = total * gst_rate / 100
final_bill = total + gst_amount

# Bill Summary
print("=" * 45)
print("             BILL SUMMARY")
print("=" * 45)

if order_list:
    for item, qty, amount in order_list:
        print(f"{item:20} x{qty:<3} ₹{amount}")

    print("-" * 45)
    print(f"Subtotal          : ₹{total:.2f}")
    print(f"GST ({gst_rate}%)           : ₹{gst_amount:.2f}")
    print(f"Final Bill        : ₹{final_bill:.2f}")
else:
    print("No items ordered.")

print("=" * 45)
print("🙏 Thank You For Visiting!")
print("☕ Visit Again - Have a Great Day!")
print("=" * 45)


# In[2]:


import random

# Random number generate
secret_number = random.randint(1, 100)

# Attempt counter
attempts = 0

print("=" * 50)
print("🎮 WELCOME TO THE NUMBER GUESSING GAME 🎮")
print("Guess a number between 1 and 100")
print("=" * 50)

while True:
    try:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if guess == secret_number:
            print("\n🎉 Congratulations!")
            print("✅ You guessed the correct number.")
            print(f"🏆 You guessed it in {attempts} attempts.")
            break

        elif guess < secret_number:
            print("📉 Too Low! Try Again.\n")

        else:
            print("📈 Too High! Try Again.\n")

    except ValueError:
        print("❌ Please enter a valid number.\n")

print("\n🙏 Thanks for Playing!")


# In[5]:


import random

best_score = None

print("=" * 60)
print("🎮 WELCOME TO THE NUMBER GUESSING GAME 🎮")
print("=" * 60)

while True:

    print("\nSelect Difficulty Level")
    print("1. Easy (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard (1 - 500)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        limit = 50
    elif choice == "2":
        limit = 100
    elif choice == "3":
        limit = 500
    else:
        print("❌ Invalid choice! Medium mode selected.")
        limit = 100

    secret_number = random.randint(1, limit)

    attempts = 0
    max_attempts = 5

    print(f"\nGuess the number between 1 and {limit}")
    print(f"You have only {max_attempts} chances.\n")

    while attempts < max_attempts:

        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > limit:
                print(f"⚠ Please enter a number between 1 and {limit}\n")
                continue

            attempts += 1

            if guess == secret_number:
                print("\n🎉 Congratulations!")
                print("✅ You guessed the correct number.")
                print(f"🏆 Attempts Used: {attempts}")

                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print("🌟 New Best Score!")

                break

            elif guess < secret_number:
                print("📉 Too Low!")

            else:
                print("📈 Too High!")

            print(f"❤️ Chances Left: {max_attempts - attempts}\n")

        except ValueError:
            print("❌ Please enter a valid number.\n")

    else:
        print("\n😢 Game Over!")
        print(f"The correct number was: {secret_number}")

    if best_score is not None:
        print(f"\n🥇 Best Score: {best_score} attempt(s)")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n🙏 Thanks for Playing!")
        print("See you again. 👋")
        break


# In[ ]:




