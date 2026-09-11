# 🤖 Gemini AI Chatbot

## 📌 Project Overview

Gemini AI Chatbot is an interactive Artificial Intelligence chatbot web application developed using Python, Flask, and the Gemini API.

The application allows users to communicate with an AI assistant through a simple web-based chat interface. It sends user messages to the Gemini API and displays the generated AI responses.

The application also maintains conversation history during the session, allowing the chatbot to understand previous messages and provide context-aware responses.

This project was developed as part of the QSkill Python Development Internship.

---

## 🎯 Project Objective

The main objective of this project is to develop an interactive AI chatbot using the Gemini API and integrate it with a Python Flask web application.

The project aims to:

- Build an AI-powered chatbot.
- Integrate Gemini API with Python.
- Create a user-friendly web interface.
- Send user messages to the AI model.
- Display AI-generated responses.
- Maintain conversation history.
- Provide an option to clear the conversation.

---

## 💡 Problem Statement

Traditional chatbot applications may provide limited or predefined responses.

An AI-powered chatbot can understand natural language and generate meaningful responses dynamically.

This project provides a simple web-based AI assistant that can interact with users, answer questions, and maintain conversation context.

---

## ✨ Key Features

- 🤖 Gemini AI-powered chatbot
- 💬 Interactive chat interface
- 🧠 Conversation history
- 🔄 Context-aware conversation
- ⚡ Dynamic AI-generated responses
- 🗑️ Clear conversation option
- 🌐 Flask-based web application
- 📱 Responsive user interface
- 🔐 Secure API key management using `.env`
- 🧩 Simple and easy-to-use design

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| Gemini API | AI response generation |
| Google GenAI SDK | Gemini API integration |
| HTML | Web page structure |
| CSS | User interface styling |
| JavaScript | Frontend interaction |
| python-dotenv | Environment variable management |
| VS Code | Development environment |
| GitHub | Version control and project hosting |

---

## 🧠 What is Gemini AI?

Gemini is a generative AI model that can understand user prompts and generate natural-language responses.

In this project, the Gemini API is integrated with a Flask application so that users can communicate with the AI assistant through a web interface.

---

## 🔄 Product Interaction

The Gemini AI Chatbot provides a simple and interactive interface for users to communicate with an AI assistant.

### User Interaction Flow

1. **Open the Application**
   - Launch the Flask application.
   - Open the chatbot in a web browser.

2. **Enter a Message**
   - The user types a question or message in the input field.

3. **Send Message**
   - Click the **Send** button.
   - The message is sent to the Flask backend.

4. **Gemini API Processing**
   - The Flask backend sends the user's message to the Gemini API.
   - Gemini processes the input and generates an appropriate response.

5. **Display Response**
   - The generated AI response is displayed in the chatbot interface.

6. **Conversation History**
   - Previous messages are maintained during the conversation.
   - This helps the chatbot understand the context of the conversation.

7. **Clear Conversation**
   - The user can click the **Clear** button to remove the existing conversation and start a new session.

### Interaction Flow

```text
User
  ↓
Enter Message
  ↓
Web Interface
  ↓
Flask Backend
  ↓
Gemini API
  ↓
AI Processing
  ↓
Generated Response
  ↓
Chatbot Interface
  ↓
Conversation History
```

---

## ⚙️ How the Application Works

### Step 1: User Input

The user enters a message into the chatbot input field.

Example:

```text
What is Artificial Intelligence?
```

---

### Step 2: Frontend Request

JavaScript sends the user's message to the Flask backend using an HTTP POST request.

```text
POST /chat
```

---

### Step 3: Flask Backend

Flask receives the user message and retrieves the previous conversation history.

The application combines the previous messages with the new user input to maintain context.

---

### Step 4: Gemini API

The Flask backend sends the conversation context to the Gemini API.

Gemini processes the prompt and generates an AI response.

---

### Step 5: Response Generation

The generated response is returned from the Gemini API to the Flask backend.

---

### Step 6: Display Response

The Flask backend sends the response back to the browser.

The response is displayed inside the chatbot interface.

---

### Step 7: Conversation History

The application stores the conversation history during the current session.

This allows subsequent questions to use previous messages as context.

---

## 🧩 System Architecture

```text
                ┌─────────────────────┐
                │        User         │
                └──────────┬──────────┘
                           │
                           ↓
                ┌─────────────────────┐
                │   Web Chat Interface │
                │      HTML/CSS/JS     │
                └──────────┬──────────┘
                           │
                           ↓
                ┌─────────────────────┐
                │    Flask Backend    │
                │       Python        │
                └──────────┬──────────┘
                           │
                           ↓
                ┌─────────────────────┐
                │     Gemini API      │
                │    Generative AI    │
                └──────────┬──────────┘
                           │
                           ↓
                ┌─────────────────────┐
                │   Generated Reply   │
                └──────────┬──────────┘
                           │
                           ↓
                ┌─────────────────────┐
                │    Chat Interface   │
                └─────────────────────┘
```

---

## 📂 Project Structure

```text
QSkill-Gemini-AI-Chatbot/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
└── .env
```

> **Note:** The `.env` file contains the Gemini API key and must never be uploaded to GitHub.

---

## 📦 Requirements

The project requires the following Python packages:

```text
Flask
google-genai
python-dotenv
```

---

## 🚀 Installation and Setup

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

---

### Step 2: Open the Project

Open the project folder in Visual Studio Code:

```text
QSkill-Gemini-AI-Chatbot
```

---

### Step 3: Install Required Packages

Open the VS Code terminal and run:

```bash
pip install flask google-genai python-dotenv
```

---

## 🔑 API Configuration

The application requires a Gemini API key.

Create a `.env` file in the project root directory.

Add:

```text
GEMINI_API_KEY=YOUR_API_KEY_HERE
FLASK_SECRET_KEY=YOUR_SECRET_KEY_HERE
```

Replace the placeholder values with your own keys.

### ⚠️ Security Warning

Never:

- Upload `.env` to GitHub.
- Share your Gemini API key publicly.
- Put the API key directly inside `app.py`.
- Include the API key in screenshots.

The `.gitignore` file should contain:

```text
.env
__pycache__/
*.pyc
.venv/
venv/
```

---

## ▶️ How to Run the Application

Open the terminal inside the project folder.

Run:

```bash
python app.py
```

If the application starts successfully, Flask will display a local address similar to:

```text
Running on http://127.0.0.1:5000
```

Open the displayed address in a web browser.

---

## 🧪 Testing

The chatbot should be tested with different types of questions.

### Test 1 — General Question

Input:

```text
What is Python?
```

Expected:

The chatbot should provide an AI-generated explanation of Python.

---

### Test 2 — AI Question

Input:

```text
What is Artificial Intelligence?
```

Expected:

The chatbot should generate an explanation of Artificial Intelligence.

---

### Test 3 — Conversation History

First message:

```text
My name is Sheela.
```

Then:

```text
What is my name?
```

Expected:

The chatbot should use the previous conversation context to answer the question.

---

### Test 4 — Follow-up Question

First:

```text
What is machine learning?
```

Then:

```text
Explain it in simple words.
```

Expected:

The chatbot should understand that "it" refers to the previous topic.

---

### Test 5 — Clear Conversation

Click:

```text
🗑️ Clear
```

Expected:

The previous conversation should be removed and a new conversation should start.

---

## 📊 Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| General Question | What is Python? | AI-generated answer |
| AI Question | What is Artificial Intelligence? | AI-generated answer |
| Conversation History | What is my name? | Uses previous context |
| Follow-up | Explain it simply | Uses previous topic |
| Clear Chat | Click Clear | Conversation removed |

---

## 📸 Screenshots

Screenshots can be added to demonstrate the working application.

Recommended screenshots:

```text
screenshots/
│
├── chatbot-home.png
├── ai-response.png
├── conversation-history.png
├── clear-conversation.png
└── terminal-running.png
```

### Suggested Screenshot Demonstrations

**1. Chatbot Home Page**

Shows the initial chatbot interface.

**2. AI Response**

Shows a successful Gemini AI response.

**3. Conversation History**

Shows the chatbot remembering information from a previous message.

**4. Clear Conversation**

Shows the conversation being cleared successfully.

**5. Terminal**

Shows the Flask application running successfully.

---

## 🌍 Real-World Applications

AI chatbots can be used in many real-world applications.

### 1. Education

Students can use AI assistants to understand concepts and get explanations.

### 2. Customer Support

Businesses can use chatbots to answer frequently asked customer questions.

### 3. Personal Assistance

AI assistants can help users with general information and everyday tasks.

### 4. Software Development

Developers can use AI assistants for programming explanations and debugging support.

### 5. Information Retrieval

Chatbots can provide natural-language answers to user queries.

---

## 🎓 Learning Outcomes

Through this project, the following skills were practiced:

- Python programming
- Flask web development
- REST API interaction
- Generative AI integration
- Gemini API usage
- HTML and CSS
- JavaScript
- Environment variable management
- Session-based conversation history
- Frontend and backend integration
- API error handling
- Git and GitHub
- Project documentation

---

## ⚠️ Limitations

The current project has some limitations:

- The chatbot depends on Gemini API availability.
- Internet connectivity is required for API requests.
- API usage may be subject to service limits.
- AI-generated responses may occasionally contain incorrect information.
- Conversation history is maintained only for the current application session.
- The application is primarily designed for educational and internship purposes.

---

## 🔮 Future Enhancements

The chatbot can be improved by adding:

1. User authentication.
2. Database-based conversation storage.
3. Multiple conversation sessions.
4. Chat history sidebar.
5. Voice input.
6. Text-to-speech responses.
7. File upload support.
8. Image understanding.
9. Markdown response rendering.
10. Code syntax highlighting.
11. Advanced responsive UI.
12. Cloud deployment.
13. Streaming AI responses.
14. Multi-language support.
15. Admin dashboard.

---

## 🔐 Security Considerations

Security is important when working with API-based applications.

The project follows these basic practices:

- API keys are stored in environment variables.
- `.env` is excluded using `.gitignore`.
- API credentials are not hard-coded in the application.
- Sensitive information should not be committed to GitHub.

For production deployment, additional security measures should be implemented.

---

## 📋 Project Status

```text
✅ Completed
```

The application provides an interactive Gemini-powered chatbot interface with conversation history and a clear conversation feature.

---

## 🏢 Internship Information

**Internship:** QSkill Python Development Internship

**Project:** Gemini AI Chatbot

**Domain:** Python Development / Generative AI

---

## 👩‍💻 Author

**Sheelasri K**

B.Tech – Artificial Intelligence & Machine Learning

SNS College of Technology

---

## ⭐ Conclusion

The Gemini AI Chatbot demonstrates how Generative AI can be integrated into a Python Flask web application.

The project connects a web-based chat interface with the Gemini API and maintains conversation history to provide a more interactive user experience.

This project provides a foundation for developing advanced AI assistants with additional features such as voice interaction, database storage, file processing, and cloud deployment.

---

## 📬 Contact

For project-related information, collaboration, or queries, please connect with the author through GitHub or LinkedIn.
