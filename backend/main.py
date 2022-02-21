# text preprocessing modules
from string import punctuation 
# text preprocessing modules
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re  # regular expression
import os
from os.path import dirname, join, realpath
import joblib
import uvicorn
from fastapi import FastAPI


nltk.download('stopwords')

stop_words =  stopwords.words('english')
def clean_text(text, remove_stop_words=True, lemmatize_words=False):
    """
        Put Doc Strings here
    """
    # Clean the text, with the option to remove stop_words and to lemmatize word
    # Clean the text
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    text = re.sub(r"\'s", " ", text)
    text =  re.sub(r'http\S+',' link ', text)
    text = re.sub(r'\b\d+(?:\.\d+)?\s+', '', text) # remove numbers
        
    # Remove punctuation from text
    text = ''.join([c.lower() for c in text if c not in punctuation])
    
    # Optionally, remove stop words
    if remove_stop_words:
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)
    
    # Optionally, shorten words to their stems
    if lemmatize_words:
        text = text.split()
        lemmatizer = WordNetLemmatizer() 
        lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
        text = " ".join(lemmatized_words)
    
    # Return a list of words
    return(text)

app = FastAPI(
    title="Question Souce Model API",
    description="A simple API that uses NLP model to predict the forum to which a question is coming from",
    version="0.1",
)

# load the sentiment model
with open(
    join("forum_classifer.pkl"), "rb"
) as f:
    model = joblib.load(f)

@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


@app.get("/predict-forum")
def predict_forum(question: str):
    """
    A simple function that receive a review content and predict the sentiment of the content.
    :param review:
    :return: prediction, probabilities
    """
    # clean the review
    cleaned_review = clean_text(question)
    
    # perform prediction
    prediction = model.predict([cleaned_review])
    
    #get the output of the prediction
    output = prediction[0]
    probas = model.predict_proba([cleaned_review])
    class_index = list(model.classes_).index(output)
    output_probability = "{:.2f}%".format(float(probas[:, class_index]) * 100)
    
#     # show results
    result = {"prediction": output, "Probability": output_probability}
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080)