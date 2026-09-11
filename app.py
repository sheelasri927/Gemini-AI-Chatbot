from flask import Flask, render_template, request, jsonify, session
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-3.7-flash"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Please enter a message."}), 400

    # Get previous conversation history
    history = session.get("history", [])

    # Add the current user message
    history.append({
        "role": "user",
        "text": user_message
    })

    # Build conversation context
    conversation = ""

    for message in history:
        conversation += f"{message['role'].capitalize()}: {message['text']}\n"

    conversation += "Assistant:"

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=conversation
        )

        assistant_message = response.text

        # Save assistant response in history
        history.append({
            "role": "assistant",
            "text": assistant_message
        })

        session["history"] = history

        return jsonify({
            "response": assistant_message,
            "history": history
        })

    except Exception as e:
        return jsonify({
            "error": f"Gemini API error: {str(e)}"
        }), 500


@app.route("/clear", methods=["POST"])
def clear():
    session.pop("history", None)

    return jsonify({
        "message": "Conversation history cleared."
    })


if __name__ == "__main__":
    app.run(debug=True)