# Suggesti: Movie & Series Recommendation Chatbot
**Suggesti** is a chatbot that provides movie and TV series recommendations based on a user-provided title. It uses cosine similarity to compare various attributes (genres, ratings, etc.) and is powered by **Dialogflow** to manage the conversational interface.
# Overview
The goal of **Suggesti** is to help users discover new movies and TV series by suggesting titles similar to the ones they already like. Users can provide the name of a movie or TV series, and the chatbot will return a list of similar titles based on attributes like genres, ratings, and other factors, while engaging in a natural conversation.
# Features
* Movie/TV Series Recommendations: Get similar recommendations based on a provided title.
* Cosine Similarity Algorithm: Uses NLP techniques to Compares multiple features (genres, ratings, etc.) to suggest similar titles.
* Dialogflow Integration: Manages conversations, allowing users to interact naturally with the chatbot.
* Real-time Suggestions: Quick responses with recommendations.
# Tech Stack
* Python: Django For backend logic.
* Dialogflow: For natural language understanding (NLU) and dialog management.
* Cosine Similarity:  For matching titles based on multiple attributes.
* scikit-learn: 
* Other Libraries: Includes libraries like pandas, Numpy.
# How It Works
1. User Input: The user provides a movie or TV series title to the chatbot.
2. Data Preparation: A dataset of over 1.1 million movies and 1 million series is processed, with several columns like genres, ratings, and other metadata vectorized using cosine similarity.
3. Cosine Similarity: The algorithm computes the similarity between the provided title and other titles based on these multiple attributes.<br/>
4. Precomputed Results: The similarity calculations are precomputed and exported into a CSV file. This CSV file is used in the backend for faster real-time recommendations.
5. Recommendation: The chatbot uses the precomputed similarity scores to quickly suggest the most similar titles.
6. Dialogflow: Handles the conversation flow, ensuring natural interaction between the user and the chatbot.
# Installation
* Clone this repository: `git clone "https://github.com/meedouazane/Suggesti"`
* Access TrueDetective directory: `cd Suggesti`
* Run pip to install dependence : `pip3 install -r requirements.txt`
* Export precomputed files from the following modules:
    * [Movies Recommendation Module](https://www.kaggle.com/code/medouazane/movies-suggestion-cosine-similarity)
    * [Series Recommendation Module](https://www.kaggle.com/code/medouazane/series-suggestions-cosine-similarity)
* Set up your Dialogflow account and import the chatbot agent.
* Connect your Python backend to Dialogflow using API keys.
# Usage
Once everything is set up, you can interact with Suggesti by asking for recommendations like:

![usage1](https://i.ibb.co/QrkbNsY/1.png)
![usage2](https://i.ibb.co/60RqQf7/2.png)
![usage3](https://i.ibb.co/XCDn4wG/3.png)

# Contributing
If you'd like to contribute to the project, feel free to submit a pull request or open an issue.