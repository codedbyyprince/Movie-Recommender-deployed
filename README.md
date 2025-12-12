🎬 Personalized Movie Recommender

Unsupervised Machine Learning • Similarity-Based Recommendations • Flask Deployment

📌 Overview

Personalized Movie Recommender is an unsupervised ML project that suggests movies similar to the ones a user already likes.
The system analyzes movie metadata, extracts meaningful features, and recommends films that share similar patterns — helping users re-experience the same vibe or theme.

This repository contains the deployment-ready version of the model using Flask, along with the web interface and API logic.

🚀 Features

Movie recommendations based on similarity

Processes genres, production companies, keywords, and other metadata

Embedding-based approach for improved results

Clean Flask backend for serving recommendations

Simple and user-friendly UI

Ready for hosting on Render / Railway / any cloud platform

🧠 Project Workflow
1. Data Preparation

Cleaning raw movie metadata

Encoding categorical features

Extracting and transforming key attributes

Scaling + embedding representation

2. Model Logic

Unsupervised similarity search

Nearest-neighbour retrieval

Final recommendation engine built on embeddings

3. Deployment

Flask backend for inference

HTML/CSS interface for user input

API route to generate movie recommendations

Production-ready structure

📂 Repository Structure
├── app.py               # Flask application  
├── static/              # CSS, JS, images  
├── templates/           # HTML UI  
├── model/               # Saved model + artefacts  
├── utils/               # Preprocessing & helper scripts  
├── requirements.txt     # Project dependencies  
└── README.md            # Documentation  

▶️ Running Locally
1. Clone the repository
git clone https://github.com/codedbyyprince/Movie-Recommender-deployed.git
cd Movie-Recommender-deployed

2. Install dependencies
pip install -r requirements.txt

3. Run the Flask app
python app.py

4. Open in browser
http://127.0.0.1:5000/

🌐 Live Demo

Deployed App: (Add your final deployed URL here)
GitHub Repo: https://github.com/codedbyyprince/Movie-Recommender-deployed

📝 Notes

This project is the deployment version of the main ML pipeline.

The core model was built in multiple versions (KNN → enhanced features → embeddings).

Only the final, polished version is deployed here.

🤝 Contribute / Connect

If you have suggestions, ideas, or improvements, feel free to open an issue or share your thoughts.
Always open to learning and collaborating.
