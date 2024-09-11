from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to get the chatbot's response
def chatbot_response(user_input):
    user_input = user_input.lower()
    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! How can I assist you?",
        "help": "I am here to assist you. You can ask me questions like 'What can you do?' or 'Tell me a joke!'",
        "what can you do": "I can chat with you, answer some basic questions, and make you smile!",
        "tell me a joke": "Why did the computer go to the doctor? Because it had a virus!",
        "bye": "Goodbye! Have a great day!",
    }

    return responses.get(user_input, "I'm sorry, I didn't understand that. Can you please rephrase?")

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle chatbot interaction
@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
