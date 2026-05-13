from flask import Flask, request, jsonify, render_template
import re
import random

app = Flask(__name__)

# Chatbot knowledge base with patterns and responses
knowledge_base = {
    'greeting': {
        'patterns': [r'\bhello\b', r'\bhi\b', r'\bhey\b', r'\bgreetings\b', r'\bwassup\b'],
        'responses': [
            'Hello! How can I help you today?',
            'Hi there! What can I do for you?',
            'Hey! Great to see you. What\'s on your mind?',
            'Greetings! How can I assist you?'
        ]
    },
    'goodbye': {
        'patterns': [r'\bbye\b', r'\bgoodbye\b', r'\bsee you\b', r'\blater\b', r'\bfarewell\b'],
        'responses': [
            'Goodbye! Have a great day!',
            'See you later! Take care!',
            'Bye! Feel free to chat anytime!',
            'Farewell! Come back soon!'
        ]
    },
    'name': {
        'patterns': [r'what.*your.*name', r'who.*are.*you', r'introduce.*yourself'],
        'responses': [
            'I\'m CodBot, your AI assistant created by CODSOFT. Nice to meet you!',
            'You can call me CodBot, an AI chatbot here to help!',
            'I\'m CodBot, your friendly AI assistant. What\'s your name?'
        ]
    },
    'help': {
        'patterns': [r'\bhelp\b', r'can you help', r'support', r'assistance'],
        'responses': [
            'Of course! I\'m here to help. You can ask me about CODSOFT, AI, or just chat!',
            'I\'d be happy to help! Try asking me questions about AI, internships, or anything else.',
            'Sure thing! Feel free to ask me anything. I\'m here to assist.'
        ]
    },
    'codsoft': {
        'patterns': [r'codsoft', r'what is codsoft', r'tell me about codsoft', r'codsoft internship'],
        'responses': [
            'CODSOFT is a vibrant community focused on leadership development, learning, and fostering shared interests. We provide platforms for individuals to develop skills and make a difference!',
            'CODSOFT is an amazing platform that brings together individuals with similar goals. We offer opportunities in leadership, learning, student engagement, and more!',
            'Great question! CODSOFT is dedicated to creating opportunities in leadership development, learning, and student engagement. Join our community!'
        ]
    },
    'ai': {
        'patterns': [r'\bai\b', r'artificial intelligence', r'machine learning', r'deep learning'],
        'responses': [
            'AI is fascinating! It\'s about creating intelligent machines that can learn and make decisions. Are you interested in learning more about specific AI topics?',
            'Artificial Intelligence is transforming the world! From chatbots like me to image recognition, AI has endless applications.',
            'Machine Learning and AI are at the core of modern technology. Is there a specific area you\'d like to explore?'
        ]
    },
    'internship': {
        'patterns': [r'internship', r'tasks', r'project', r'assignment'],
        'responses': [
            'Awesome! The CODSOFT AI internship includes tasks like chatbots, tic-tac-toe AI, image captioning, recommendation systems, and face detection!',
            'The internship is a great opportunity to build real-world AI projects. You need to complete at least 3 tasks for successful completion.',
            'Each internship task helps you learn different aspects of AI - from NLP to computer vision. Which task interests you most?'
        ]
    },
    'python': {
        'patterns': [r'python', r'coding', r'programming', r'code'],
        'responses': [
            'Python is an excellent language for AI and machine learning! It has great libraries like TensorFlow, PyTorch, and scikit-learn.',
            'Coding is a crucial skill for AI development. Python is my recommendation for beginners because it\'s simple yet powerful!',
            'Whether you\'re building chatbots, neural networks, or automation tools, Python is the way to go!'
        ]
    },
    'time': {
        'patterns': [r'what time', r'current time', r'what\'s the time'],
        'responses': [
            'I don\'t have access to real-time data, but you can check your device for the current time!',
            'Sorry, I can\'t tell you the exact time, but you can check your system clock!',
            'Time check? Your device should have that info readily available!'
        ]
    },
    'how_are_you': {
        'patterns': [r'how are you', r'how\'s it going', r'how do you do'],
        'responses': [
            'I\'m doing great! Thanks for asking. How are you doing today?',
            'I\'m functioning perfectly! How can I help you?',
            'All systems running smoothly! Ready to chat and help you out!'
        ]
    },
    'default': {
        'patterns': [],
        'responses': [
            'That\'s interesting! Can you tell me more or ask something else?',
            'I\'m not sure I understand. Could you rephrase that?',
            'I didn\'t quite catch that. Try asking me about CODSOFT, AI, or internship tasks!',
            'Hmm, interesting question! Try asking about AI, coding, or how I can help you!'
        ]
    }
}

def match_intent(user_input):
    """Match user input to an intent using pattern matching"""
    user_input = user_input.lower().strip()
    
    for intent, data in knowledge_base.items():
        if intent == 'default':
            continue
        for pattern in data['patterns']:
            if re.search(pattern, user_input, re.IGNORECASE):
                return intent
    
    return 'default'

def get_response(intent):
    """Get a random response for the matched intent"""
    responses = knowledge_base[intent]['responses']
    return random.choice(responses)

def chatbot_response(user_message):
    """Generate chatbot response based on user message"""
    intent = match_intent(user_message)
    response = get_response(intent)
    return response

@app.route('/')
def index():
    """Render the chatbot interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """API endpoint to handle chat messages"""
    data = request.json
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'error': 'Empty message'}), 400
    
    bot_response = chatbot_response(user_message)
    
    return jsonify({
        'user_message': user_message,
        'bot_response': bot_response
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
