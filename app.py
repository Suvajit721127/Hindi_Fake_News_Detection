from flask import Flask, request
import torch
import os

from model import (
    load_hinvec,
    load_trained_model,
    predict
)

app = Flask(__name__)

# ==============================
# DEVICE (FORCE CPU for deployment)
# ==============================
device = torch.device("cpu")
print("Using device:", device)

# ==============================
# LOAD MODELS (ONLY ONCE)
# ==============================
model = None
tokenizer = None
hinvec_model = None

try:
    print("Loading Hinvec model...")
    tokenizer, hinvec_model = load_hinvec()

    print("Loading trained classifier...")
    model = load_trained_model()

    print("✅ All models loaded successfully!")

except Exception as e:
    print("❌ ERROR while loading models:", e)

# ==============================
# HOME PAGE
# ==============================
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Fake News Detector</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: #fff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                padding: 30px;
                border-radius: 15px;
                width: 500px;
                text-align: center;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0,0,0,0.2);
            }
            h1 {
                margin-bottom: 20px;
            }
            textarea {
                width: 100%;
                padding: 12px;
                border-radius: 10px;
                border: none;
                resize: none;
                font-size: 14px;
                outline: none;
            }
            button {
                margin-top: 15px;
                padding: 12px 25px;
                border: none;
                border-radius: 10px;
                background: #ff7eb3;
                color: white;
                font-size: 16px;
                cursor: pointer;
                transition: 0.3s;
            }
            button:hover {
                background: #ff4f91;
            }
            .footer {
                margin-top: 15px;
                font-size: 12px;
                opacity: 0.7;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📰 Fake News Detector</h1>
            <form action="/predict" method="post">
                <textarea name="news" rows="8" placeholder="Paste your news here..." required></textarea>
                <br>
                <button type="submit">🔍 Analyze News</button>
            </form>
            <div class="footer">
                
            </div>
        </div>
    </body>
    </html>
    """

# ==============================
# PREDICT ROUTE
# ==============================
@app.route("/predict", methods=["POST"])
def predict_news():
    global model, tokenizer, hinvec_model

    if model is None:
        return "<h2>❌ Model not loaded. Check server logs.</h2>"

    text = request.form.get("news")

    if not text or text.strip() == "":
        return "<h2>❌ Please enter some text!</h2><a href='/'>Go Back</a>"

    try:
        result = predict(text, model, tokenizer, hinvec_model)

        if result == 1:
            output = "🛑 Fake News"
            color = "red"
        else:
            output = "✅ Real News"
            color = "green"

    except Exception as e:
        return f"<h2>❌ Prediction Error: {str(e)}</h2>"

    return f"""
    <html>
    <body style="font-family: Arial; text-align:center; margin-top:50px;">
        <h1 style="color:{color};">{output}</h1>
        <br>
        <a href="/">🔙 Try Again</a>
    </body>
    </html>
    """

# ==============================
# ENTRY POINT
# ==============================
if __name__ == "__main__":
    # Hugging Face Spaces uses port 7860
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)
