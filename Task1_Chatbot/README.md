# CodBot - Rule-Based AI Chatbot

A simple yet powerful rule-based chatbot built with Flask that responds to user inputs based on predefined patterns and rules. This project demonstrates the fundamentals of Natural Language Processing (NLP) and conversational AI.

**CODSOFT AI Internship - Task 1**

---

## 🌟 Features

- **Pattern Matching**: Uses regex patterns to identify user intents
- **Multiple Intents**: Handles greetings, goodbyes, questions about CODSOFT, AI topics, and more
- **Random Responses**: Provides varied responses to keep conversations natural
- **Beautiful UI**: Modern web interface with real-time chat
- **Easy to Extend**: Simple structure to add new intents and patterns

---

## 📋 Intents Covered

1. **Greeting** - Hello, Hi, Hey
2. **Goodbye** - Bye, See you, Farewell
3. **Identity** - Who are you, What's your name
4. **Help** - Can you help, Support, Assistance
5. **CODSOFT** - Information about CODSOFT
6. **AI/ML** - Questions about Artificial Intelligence
7. **Internship** - Internship tasks and projects
8. **Python** - Programming and coding questions
9. **Time** - Time-related queries
10. **How Are You** - General conversation
11. **Default** - Fallback for unrecognized inputs

---

## 🛠️ Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/CODSOFT.git
cd CODSOFT/Task_1_Chatbot
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### Method 1: Run Directly
```bash
python chatbot_app.py
```

### Method 2: Using Flask CLI
```bash
set FLASK_APP=chatbot_app.py
flask run
```

The chatbot will start on `http://localhost:5000`

**Open your browser and navigate to `http://localhost:5000`**

---

## 💬 How It Works

### Architecture

```
User Input
    ↓
Pattern Matching (Regex)
    ↓
Intent Identification
    ↓
Response Selection (Random)
    ↓
Display to User
```

### Process Flow

1. **User submits a message** through the web interface
2. **Pattern Matching**: The message is compared against predefined regex patterns
3. **Intent Detection**: If a pattern matches, the corresponding intent is identified
4. **Response Generation**: A random response from that intent's pool is selected
5. **Display**: The response is sent back to the user in real-time

### Example

```
User: "Hello!"
Pattern Check: Matches greeting pattern (r'\bhello\b')
Intent: 'greeting'
Response: "Hello! How can I help you today?" (or one of 3 other responses)
```

---

## 📁 Project Structure

```
Task_1_Chatbot/
├── chatbot_app.py          # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── templates/
│   └── index.html         # Web UI
└── static/                # (Optional for CSS/JS if needed)
```

---

## 🎯 Understanding the Code

### Knowledge Base Structure
```python
knowledge_base = {
    'intent_name': {
        'patterns': [r'regex_pattern_1', r'regex_pattern_2'],
        'responses': ['response1', 'response2', 'response3']
    }
}
```

### Key Functions

- **`match_intent(user_input)`**: Matches user input to an intent using regex
- **`get_response(intent)`**: Returns a random response for the matched intent
- **`chatbot_response(user_message)`**: Main function that combines matching and response generation
- **`/chat` route**: API endpoint that handles incoming messages

---

## 🔧 Customization

### Adding New Intent

1. Open `chatbot_app.py`
2. Add to `knowledge_base`:
```python
'new_intent': {
    'patterns': [r'pattern1', r'pattern2', r'pattern3'],
    'responses': ['response1', 'response2', 'response3']
}
```

### Modifying Existing Responses
Simply edit the responses list for any intent:
```python
'greeting': {
    'patterns': [...],
    'responses': [
        'Your new response here',
        ...
    ]
}
```

---

## 📊 Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **NLP Technique**: Regex-based Pattern Matching
- **Server**: Flask Development Server

---

## 🎓 Learning Outcomes

After completing this project, you'll understand:

✅ Basics of Natural Language Processing (NLP)
✅ Pattern matching and intent recognition
✅ Conversational flow and dialogue management
✅ Flask web framework basics
✅ Client-server communication with APIs
✅ Real-time message handling with JavaScript

---

## 📝 Future Enhancements

- [ ] Add NLP library (NLTK, spaCy) for better pattern recognition
- [ ] Implement context awareness (remember conversation history)
- [ ] Add sentiment analysis
- [ ] Database integration to store conversations
- [ ] Voice input/output capabilities
- [ ] Multi-language support

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in chatbot_app.py
app.run(debug=True, port=5001)  # Use different port
```

### Module Not Found Error
```bash
# Make sure you installed requirements
pip install -r requirements.txt
```

### Connection Refused
- Check if Flask server is running
- Verify you're accessing `http://localhost:5000`
- Check firewall settings

---

## 📧 Support

For issues or questions, reach out to CODSOFT:
- Email: contact@codsoft.in
- Website: www.codsoft.in

---

## 📄 License

This project is part of the CODSOFT AI Internship Program.

---

## 🔗 Repository Link

[Add your GitHub repository link here]

---

**Happy Coding! 🚀**
