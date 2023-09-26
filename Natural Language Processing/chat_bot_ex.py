import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi, how can I assist you?"]
    ],
    [
        r"my name is (.*)",
        ["Hello, %1! How can I help you today?"]
    ],
    [
        r"what is your name?",
        ["You can call me ChatBot. How can I assist you?"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Have a nice day!", "Take care!"]
    ],
    [
        r"(.*) (hungry|tired|sleepy)",
        [
            "I understand. Take a break and have some rest.",
            "Try having a snack to boost your energy.",
            "Maybe it's time for a little nap."
        ]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't have an answer for that at the moment."]
    ]
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

# Start the conversation loop
print("Hello! How can I assist you today?")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        break
    print(chatbot.respond(user_input))
