#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

