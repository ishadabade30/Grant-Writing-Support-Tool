import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyAgAmhWhxpWsJAc8Bgzx5xD4v4K8HYYH4E")

def generate_answer(context, question):
    """
    Generates answers based on context and user questions.
    """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Context: {context}\nQuestion: {question}")
    return response.text

# Test the function
if __name__ == "__main__":
    context = "This proposal focuses on building water filtration systems in rural areas."
    question = "What is the purpose of the project?"
    print("Answer:", generate_answer(context, question))
