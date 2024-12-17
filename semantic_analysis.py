import spacy

nlp = spacy.load("en_core_web_sm")

def refine_text(input_text):
    """
    Removes stopwords and performs lemmatization on the input text.
    """
    doc = nlp(input_text)
    refined_text = " ".join([token.lemma_ for token in doc if not token.is_stop])
    return refined_text

# Test the function
if __name__ == "__main__":
    text = "Can you help me write a proposal for clean water projects?"
    print("Refined Text:", refine_text(text))
