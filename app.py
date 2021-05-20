#Importing required libraries
#from tensorflow import keras
import pickle
import keras
from keras.preprocessing.sequence import pad_sequences
from flask import Flask, render_template, request

token = pickle.load(open("token.pkl", "rb"))
model = keras.models.load_model('nlpModel')

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        instance = token.texts_to_sequences(review)
        flat_list = []
        for sublist in instance:
            for item in sublist:
                flat_list.append(item)
        flat_list = [flat_list]
        instance = pad_sequences(flat_list, padding='post', maxlen=100)
        pred = model.predict(instance)
        prediction = pred[0][0]
        prediction1 = round(prediction,2)
        if pred > 0.5:
            return render_template('result.html', data=f'Based on the review, this movie gets a positive response')
        else:
            return render_template('result.html', data=f'Based on the review, this movie gets a negative response.')


if __name__ == "__main__":
    app.run(debug=True)

