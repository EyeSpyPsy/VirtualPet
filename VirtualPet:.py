import random

class VirtualPet:
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 5  
        self.happiness = 5  

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
            print(f"You fed {self.name}. Hunger is now {self.hunger}.")
        else:
            print(f"{self.name} is already full!")

    def play(self):
        if self.happiness < 10:
            self.happiness += 1
            print(f"You played with {self.name}. Happiness is now {self.happiness}.")
        else:
            print(f"{self.name} is already very happy!")

    def check_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger} (0 is full, 10 is starving)")
        print(f"Happiness: {self.happiness} (0 is sad, 10 is very happy)\n")

    def talk(self):
        if self.hunger > 7:
            print(f"{self.name} says: I'm really hungry! Can you feed me?")
        else:
            responses = [
                "Woof! I'm so happy to see you!",
                "Meow! Can we cuddle?",
                "Squeak! Let's play together!",
                "Chirp! You're my favorite person!",
                "Thank you for taking care of me!",
                "I love spending time with you!"
            ]
            print(f"{self.name} says: {random.choice(responses)}")

def main():
    print("Welcome to the Virtual Pet Game!")
    name = input("What is your pet's name? ")
    print("Choose your pet type:")
    print("1. Dog\n2. Cat\n3. Bunny\n4. Bird")
    choice = input("Enter the number for your pet type: ")
    pet_type = {"1": "Dog", "2": "Cat", "3": "Bunny", "4": "Bird"}.get(choice, "Mystery Pet")

    pet = VirtualPet(name, pet_type)
    print(f"\nCongratulations! You adopted a {pet.pet_type} named {pet.name}!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Check your pet's status")
        print("4. Talk to your pet")
        print("5. Exit game")
        action = input("Enter your choice: ")

        if action == "1":
            pet.feed()
        elif action == "2":
            pet.play()
        elif action == "3":
            pet.check_status()
        elif action == "4":
            pet.talk()
        elif action == "5":
            print(f"Goodbye! {pet.name} will miss you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
