# Movie-review-sentiment-prediction

### Built an application which predicts the sentiment of a movie review

This application contains 3 phases:

Phase 1: Data Preparation and model building

- I used IMDB dataset from Kaggle, which contains 50,000 movie reviews, to train the model
- Performed text pre-processing which involves cleaning each review by removing html tags, punctuations, numbers, multiple spaces etc., along with data analysis
- Built text classification models with different types of Deep neural networks: Densely connected neural network, Convolutional Neural Network (CNN) and Long Short Term Memory Network (LSTM), a variant of Recurrent Neural Networks
- Opted Recurrent Neural Networks due to low difference for loss and accuracy between training set and the test set

Phase 2: Building the app using Flask and HTML

- This phase packages the model into web service that, when given the data through a POST request, returns the movie review prediction probability as a response
- I used the Flask web framework which is used for developing web services in Python

Phase 3: Deploying the app using Heroku

-  Used Heroku, a Platform as a Service tool, to deploy the Github repository in Heroku


