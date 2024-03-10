
# Motivation

In most of the world, people imagine and look at Robot or AI from the productivity perspective.
Automation tools, alternative workforce etc.
I was born and grown up in Japan till 17.
This country is a bit weird that lots of robot comics and anime are about friendship, not tools or human replacement.
Since I cant remember, I was watching Doraemon and Atom.
Always dreamed that at some point in the future, I will have a robot friend that are strongly bond to each other just like Nobita and Doraemon.

Of course, building a robot that has human like intelegence and emotion is still far away.
But at least as a starting point, I wanted to create a chat clone of myself.
Imagine chatting to your clone, when you feel down, he/she reminds you about things that you deeply care about.
Or Asking your clone what you were thinking on the same day 3 years ago.

I feel this is a ouviues need but man, I couldn't find a easy way to create my clone.

GPTs only accepts 20 small files.
Most of AI clone products like Replika, c.ai, Delphi.ai don't allow users to fine-tune with original dataset or have high limitations.
fine-tuning GPT or other LLM requires dataset in a very specific format and data cleaning task is extremely stressful.
I guess for experienced devs, fine-tuning a model with your chat history is easy but non-technical ppl like me, it is a nightmare.
I also found many people on Reddit trying to fine-tune a model with their chat history but stuck in data cleaning and formatting task.

so I built this.
It's a simple web app where user can upload chat history to craft a clone and chat with them.
UIUX both sucks, but still it works and super easy.
Clone this repo, deploy it locally, and have fun chatting with your clone.

The app is not done yet.
There are so many things I wanna add like supporting other chat app, increase the fine-tuning quality, improve chat experience etc.
If you are interested in relationship building between Human and Machine too, feel free to reach me out @ https://twitter.com/koheingt

#Key Features
- Upload chat history from WhatsApp, Telegram, and Instagram Messenger
- Clean and reformat chat history for preparing dataset
- Fine-tune a chat model based on users chat history
- Engage in conversations with the your chat clone through a web interface

Prerequisites
Before starting, ensure you have the following:

Node.js
Python 3
Required npm modules (detailed below)
Necessary Python packages (specified below)
OpenAI API key
Your chat history files
Installation Guide
This guide is designed to be accessible for users of all technical backgrounds. If you're already familiar with the prerequisites, feel free to skip the corresponding steps. This guide is primarily for macOS users, but steps for Windows users may be added in the future.

Setting Up Your Environment
Install Homebrew:
Open Terminal and execute:

bash
Copy code
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Install Git:
In Terminal, run:

Copy code
brew install git
Clone the Repository:
Execute the following command in Terminal:

bash
Copy code
git clone [Repository URL]
Install Node.js and npm:

Visit Node.js official website and download the LTS version installer.
Follow the installation instructions.
Verify the installation by running the following commands in Terminal:
Copy code
node -v
npm -v
Install Node.js Dependencies:
In Terminal, execute:

Copy code
npm install
Install Required npm Modules:
Run the following command in Terminal:

lua
Copy code
npm install dotenv express passport express-session multer http-proxy-middleware socket.io
Install Python:
Execute in Terminal:

Copy code
brew install python3
Set Up Python Virtual Environment:

Locate the clone-factory-v1 directory in Finder and note its path.
In Terminal, replace /path/to/your/repository with your actual path and execute the following commands:
bash
Copy code
cd /path/to/your/clone-factory-v1
python3 -m venv myenv
source myenv/bin/activate
Install Python Dependencies:
In Terminal, run:

Copy code
pip install Flask flask-cors openai scikit-learn
Set Up OPENAI_API_KEY:

Visit OpenAI Platform, create an account, and navigate to the API keys tab.
Create a new secret key, copy it, and paste it into the .env file like so (ensure there are no spaces around the = sign):
makefile
Copy code
OPENAI_API_KEY=your_secret_key_here
Fund Your OpenAI Account:

Model fine-tuning requires funding. The cost depends on your data volume, but typically $5-$10 is sufficient.
Navigate to the Billing tab in Settings and add funds as needed.
Starting the Application
Start the Node.js Server:

Replace /path/to/your/repository with your actual path and run the following command in Terminal:
bash
Copy code
cd /path/to/your/clone-factory-v1
node app.js
Start the Flask Server:

Open another Terminal window, replace /path/to/your/repository with your actual path, and execute the following commands:
bash
Copy code
cd /path/to/your/clone-factory-v1
export FLASK_APP=chat_with_model.py
flask run
Explore the Application:

Open a web browser and navigate to http://localhost:3000.
Enjoy interacting with your personalized chat clone app!
