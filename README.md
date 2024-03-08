#Overview

This application allows users to create their chat clone for engaging chat experiences. By uploading their chat history, users can craft an chat clone that embodies their values and behaviors, offering a unique and tailored interaction.

#Key Features
- Upload chat history from WhatsApp, Telegram, and Instagram Messenger
- Clean and reformat chat history for preparing dataset
- Fine-tune a chat model based on users chat history
- Engage in conversations with the your chat clone through a web interface

Getting Started

#Prerequisites
- Node.js
- Python 3
- Flask
- OpenAI API key

#Installation

1: Clone the repository to your local machine.

2: Install Node.js dependencies

npm install

3: Install Python dependencies

pip install flask openai flask_cors

4: Set up OPENAI_API_KEY
go to https://platform.openai.com/ and create your account, move to API KEY tab, create a secret key and copy it
go to .env file and paste the key like this ""

#Start Your Application

1: Start the Node.js server
go to Terminal
cd to clone-factory-v1

node app.js

2: Start the Flask server
open another Terminal
cd to clone-factory-v1

export FLASK_APP=chat_with_model.py
flask run

3: Play with the app
go to http://localhost:3000
play with the app 
