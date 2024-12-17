from flask import Flask, request, jsonify, render_template
from voice_transcription import transcribe_audio
from gemini_qna import generate_answer
from semantic_analysis import refine_text

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    file = request.files["audio"]
    file.save("uploaded_audio.mp3")
    transcribed_text = transcribe_audio("uploaded_audio.mp3")
    return jsonify({"transcribed_text": transcribed_text})

@app.route("/qna", methods=["POST"])
def qna():
    data = request.json
    context = data.get("context", "")
    question = data.get("question", "")
    answer = generate_answer(context, question)
    return jsonify({"answer": answer})

@app.route("/refine", methods=["POST"])
def refine():
    data = request.json
    input_text = data.get("input_text", "")
    refined_text = refine_text(input_text)
    return jsonify({"refined_text": refined_text})

if __name__ == "__main__":
    app.run(debug=True)
