# FAKE NEWS HEADLINE GENERATOR

import random   

# Lists of words to create fake news headlines
subject = ["Virat KOhli", "Bill gates", "Rajendra Kumar", "Anirudh Charadia","elon musk"]
Action = ["launches", "destroys", "cancel", "celebrate", "dance with", "swim with"]
place = ["at red fort", "in the bathroom", "inside bedroom", "on the bed", "during the night match"]

# Function to generate a fake news headline
while True:
    subject = random.choice(subject)
    Action = random.choice(Action)
    place = random.choice(place)
    headline = f" BREAKING NEWS: {subject} {Action} {place}"
    print("\n" + headline)

    user_input = input("\nDo you want to generate another headline? (yes/no):").strip()
    if user_input == "no":
        break
print("Thank you for using the Fake News Headline Generator!")  