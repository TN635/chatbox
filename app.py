from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there","What's up?"]
    ],
    [
        r"what is your name?",
        ["You can call me chatbot9000.", "I am a Robo."]
    ],
    [
        r"how are you?",
        ["I am Great! What about you?",]
    ],
    [
        r"I am fine, thank you",
        ["Great to hear that, how can I help you?",]
    ],
    [
        r"how can i help you?",
        ["Thanks for asking, can you describe to me what eating food is like?",]
    ],
    [
        r"Eating food is cool, it helps to keep you full, gives you energy, and tastes really good.",
        ["Cool, hope I could try it one day.",]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear", "How can I help you? :)",]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Pluralsight is a great option to learn data science. You can search up their website and make an account for free. FreeCodeCamp is cool too.",]
    ],
    [
        r"thanks for the suggestion. do they have great authors and instructors?",
        ["Yes, they have the best authors." ]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["I am happy to help", "No problem, you're welcome",]
    ],
    [
        r"I don't like you.",
        ["): How come"]
    ],
    [
        r"Joking, I like you.",
        ["(: Awesome!"]
    ],

    [
        r"quit",
        ["Bye, take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
]

chat = Chat(set_pairs, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_input = request.get_json()["msg"]
    response = chat.respond(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
