
# Hindi Fake News Detection System

A deep learning-based Fake News Detection System for Hindi news articles using **HinVec embeddings**, a **CNN classification model**, and **Flask deployment** for real-time prediction.

## Features

* Detects fake and real Hindi news
* Uses pretrained HinVec word embeddings
* CNN-based text classification
* Real-time prediction through Flask web app
* Simple and user-friendly interface

## Tech Stack

* Python
* PyTorch
* Flask
* CNN
* NLP
* HTML/CSS
* HinVec Embeddings

## Live Demo

🔗 [https://your-live-demo-link.com](https://huggingface.co/spaces/suvajit721127/fake-news-detector)

## Demo Screenshot

<img width="100%" alt="Project Demo" src="demo.png">

## Dataset

This project uses Hindi fake news datasets for training and evaluation.

## Hindi Fake News Detection Dataset (HFDND)
  [https://www.kaggle.com/datasets/arnavagrawal22/arnsin-dl-cleaned1](https://www.kaggle.com/datasets/arnavagrawal22/arnsin-dl-cleaned1)

## HinVec Embedding Model
HinVec Pretrained Hindi Word Embeddings
[https://github.com/anoopkunchukuttan/hindvec](https://huggingface.co/Sailesh97/Hinvec)

## Project Workflow

```text id="h6r3mk"
User Input
   ↓
Text Preprocessing
   ↓
HinVec Embedding
   ↓
CNN Model
   ↓
Prediction (Fake / Real)
```

## Installation

### Clone the repository

```bash id="k9v2pt"
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### Install dependencies

```bash id="b5q8wr"
pip install -r requirements.txt
```

### Run the Flask app

```bash id="a7n4ld"
python app.py
```

## Usage

1. Open the Flask web application
2. Enter Hindi news text
3. Click the predict button
4. View the prediction result

## Future Improvements

* Add confidence score
* Improve UI design
* Add multilingual support
* Compare CNN with LSTM/BiLSTM/Transformer models
* Deploy on cloud platforms

## Author

Suvajit Manna
