from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")


@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')

    # Process the user message with spaCy
    doc = nlp(user_message)

    # Basic responses for the chatbot
    if "hello" in user_message.lower():
        response = "Hello! How can I assist you at UNIOSUN today?"
    elif "courses" in user_message.lower():
        response = "UNIOSUN offers various courses in Arts, Sciences, Engineering, and more. Which one are you interested in?"
    elif "admission" in user_message.lower():
        response = "For admission information, you can visit the UNIOSUN website or contact the admissions office."
    elif "library" in user_message.lower():
        response = "The UNIOSUN library provides a wide range of resources for students and researchers. You can visit the library website for more details."
    elif "contact" in user_message.lower():
        response = "You can contact UNIOSUN through their official website or reach out to specific departments via email or phone."
    else:
        response = "I'm not sure I understand. Can you please rephrase your question?"

    return jsonify({"response": response})


if __name__ == '_main_':
    app.run(debug=True)