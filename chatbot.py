# Import required libraries
import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Greetings!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine, thanks for asking."]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot. You can call me ChatBot.", "My name is ChatBot."]
    ],
    [
        r"what is nlp ?",
        ["NLP (Natural Language Processing) is a branch of AI that helps computers understand, interpret, and generate human language."]
    ],
    [
        r"what are the uses of nlp ?",
        ["NLP is used in chatbots, voice assistants, sentiment analysis, machine translation, and text summarization."]
    ],
    [
        r"why is nlp important ?",
        ["NLP is important because it enables machines to interact with humans naturally, improving communication and automation."]
    ],
    [
        r"how does nlp work ?",
        ["NLP works by processing text through tokenization, lemmatization, parsing, and machine learning techniques to understand meaning."]
    ],
    [
        r"what are examples of nlp ?",
        ["Examples of NLP include Google Translate, Siri, Alexa, chatbots, spam filters, and sentiment analysis tools."]
    ],
    [
        r"quit",
        ["Bye! Take care.", "It was nice talking to you. Goodbye!"]
    ]
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

# Function to start the chatbot conversation
def chatbot_conversation():
    print("Hello! I'm an NLP Chatbot. Ask me about NLP, its uses, importance, or anything related! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        if response:
            print(f"ChatBot: {response}")
        else:
            print("ChatBot: I’m not sure how to answer that. Can you ask about NLP, its uses, or importance?")

# Start the chatbot
if __name__ == "__main__":
    chatbot_conversation()
