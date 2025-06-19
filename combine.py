import streamlit as st
from keras.models import load_model
from keras.datasets import imdb
from keras.preprocessing.sequence import pad_sequences

# Function to preprocess text and prepare model input
def preprocess_text(text):
    word_to_index = imdb.get_word_index()
    tokenized_review = [word.lower() for word in text.split()]
    text_indices = [word_to_index[word]+3 for word in tokenized_review if word in word_to_index.keys()]
    model_input = [text_indices]
    model_input = pad_sequences(model_input, maxlen=2494)
    return model_input

# Load CNN and LSTM models
cnn_model_path = 'C:\\Users\\AISWARYA SREEKUMAR\\Downloads\\IMDB_Sentiment_Analysis-master\\IMDB_Sentiment_Analysis-master\\CNN_model\\CNN_model.hdf5'
lstm_model_path = 'C:\\Users\\AISWARYA SREEKUMAR\\Downloads\\IMDB_Sentiment_Analysis-master\\IMDB_Sentiment_Analysis-master\\LSTM_model\\LSTM_model.hdf5'
cnn_model = load_model(cnn_model_path)
lstm_model = load_model(lstm_model_path)

# Title and description
st.title("IMDb Movie Review Sentiment Analysis")
st.write("Type a movie review to predict its sentiment.")

# Text input for user input
input_review = st.text_area("Enter the movie review:")

# Button to trigger prediction
if st.button("Predict"):
    if input_review.strip() == "":
        st.warning("Please enter a movie review.")
    else:
        # Preprocess text
        model_input = preprocess_text(input_review)
        # Predict sentiment using CNN model
        cnn_prediction = cnn_model.predict(model_input, verbose=0)
        # Predict sentiment using LSTM model
        lstm_prediction = lstm_model.predict(model_input, verbose=0)
        # Output prediction
        st.write("Prediction (CNN model):", "Positive" if cnn_prediction > 0.5 else "Negative")
        st.write("Prediction (LSTM model):", "Positive" if lstm_prediction > 0.5 else "Negative")