 🎬 IMDB Sentiment Analysis using CNN and LSTM

This project performs *sentiment analysis* on IMDB movie reviews using two deep learning models — *Convolutional Neural Network (CNN)* and *Long Short-Term Memory (LSTM). The goal is to classify movie reviews as **positive* or *negative* based on their content using Natural Language Processing (NLP) techniques.

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- Numpy, Pandas
- HTML, CSS, JavaScript (for front-end)
- Jupyter Notebook
- Matplotlib (for visualizations)

---

## 🧠 Model Architectures

### ✅ CNN Model
- Text vectorization and embedding
- Convolutional + MaxPooling layers
- Dense layers for classification

### ✅ LSTM Model
- Embedding layer
- LSTM units for sequence learning
- Dense output layer
  
- Both models are stored under:
- CNN_model/cnn.source
- LSTM_model/lstm.source

🧠 Model outputs and architecture visuals:
- CNN_model_visual.png
- LSTM_model_visual.png


…
  ## 📁 Project Structure

imdb-sentiment-analysis/ ├── CNN_model/ │   └── cnn.source ├── LSTM_model/ │   └── lstm.source ├── CNN_predict.py ├── LSTM_predict.py ├── combine.py ├── index.html ├── script.js ├── styles.css ├── CNN_model_visual.png ├── LSTM_model_visual.png ├── .gitignore └── README.md

Install required packages:
pip install -r requirements.txt

Run prediction script:
python CNN_predict.py

 For web-based interaction:
 Open index.html
 
Dataset

The dataset used is the IMDB Movie Review Dataset containing 50,000 labeled reviews.
Only sample data is included for demo purposes.

🔗 Full dataset available at:
Stanford IMDB Dataset
