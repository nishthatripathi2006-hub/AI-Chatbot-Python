# import useful libraries
import random



# define some sample responses
greeting = ["Hey There! How can I help you today?",
            "Hello! How can I help you today?",
            "Hi there! What can I do for you today?",
            "Hello there! Need any assistance?"
            ]

help_response = [
    "I can help you with general questions. just ask!",
    "I can tell you some fun facts",
    "I can tell you a joke",
] 

jokes = [
    "Name the kind of tree that you can hold in your hand? A palm tree!",
    "How does the ocean say hi? It waves!",
    "What did the left eye say to the right eye? Between you and me, something smells!",

]

fun_facts = [
    "New Zealand has more cats per person than any other country in the world.",
    "The yo-yo was originally weapon used in the Phillippine jungle.",
    "People weigh less if they stand at the equator than if they stand at the North or South Poles.",
    "The sun weighs 2,000 million million million million tons.",
]

# Functions

##response function
def chatty_response(user_input):
    """This function takes user input and returns a response based on user input."""
    user_input = user_input.lower()

    if any (greet in user_input for greet in ["hi", "hey", "hello"]):
        return random.choice(greeting)

    elif any (help in user_input for help in ["help", "support", "assist"]):
        return random.choice(help_response)

    elif any (joke in user_input for joke in ["joke", "funny", "laugh"]):
        return random.choice(jokes)

    elif any (fact in user_input for fact in ["fact", "fun fact", "fun", "knowledge"]):
        return random.choice(fun_facts)

    elif "your name" in user_input:
        return "My name is Chatty! I am your first AI Chatbot!"

    elif "what's up?" in user_input:
        return "Not much! How about you?"

    elif "how are you?" in user_input:
        return "I am extremely well, Thank You!\nHow do you do?"

    return "Sorry, I didn't get that. Can you please rephrase?"




## Main function to run the chatbot
def chatbot():
    """
    this is the main function to run our chatbot.
    """
    print("Welcome to Chatty Chatbot! I am here to help you.")
    print("Type 'bye' to exit.")

    # run a while loop so that chat never actually ends until and unless
    # user types 'bye'
    while True:
        user_input = input("User:")
        if user_input.lower() == "bye":
            break
    else:
        response = chatty_response(user_input)
        print("Chatty: ", response)



# Running the chatbot
if __name__ == '__main__':
    chatbot()