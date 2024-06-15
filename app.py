from flask import Flask, render_template, request, jsonify, redirect, url_for
from chatbot import Chatbot
from solving import calculate_numerical_solutions, generate_response

app = Flask(__name__)

# Initialize the chatbot
chatbot = Chatbot('intents.json')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot_page():
    return render_template('home.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    
    if user_message.lower() == 'exit':
        return jsonify({'response': 'Goodbye!'})

    # Process user input and get responses
    if chatbot.recognize_intent(chatbot.process_input(user_message)) == 'calculate_numerical_solutions':
        results = calculate_numerical_solutions(user_message)

        if "error" in results:
            print("Chatbot: " + results["error"])
        else:
            response = generate_response(results)
            print("Chatbot:", response)
    else:
        response = chatbot.handle_intent(user_message)

    return jsonify({'response': response})

@app.route('/home')
def go_home():
    return redirect(url_for('home'))

@app.route('/static/js/alerts.js')
def alerts_js():
    return app.send_static_file('js/alerts.js')


if __name__ == '__main__':
    app.run(debug=True)
