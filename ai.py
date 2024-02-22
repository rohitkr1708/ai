import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    print("Welcome to the Random Number Generator!")
    
    while True:
        input("Press Enter to generate a random number...")
        
        random_number = generate_random_number()
        print(f"Your random number is: {random_number}")

        play_again = input("Do you want to generate another random number? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for using the Random Number Generator. Goodbye!")
            break

