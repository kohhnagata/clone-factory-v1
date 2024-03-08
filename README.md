
#Motivation

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

#Things You Need To Prepare
- Node.js
- Python 3
- npm modules(see below)
- python modules(")
- OpenAI API key
- Chat History

#How To Install The App

*I will try to make the guide book even doable for non-technical ppl. Please skip them if you already have the prerequirements.
*I am a Mac user so I will put the guilde book only for Mac users first. Might add one for Window users if needed.

1: Install Homebrew
Open Terminal and run:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2; Install Git
run (on Terminal):
brew install git

3: Clone the repository to your local machine
run (on Terminal):
git clone https:

4: install npm

Go to https://nodejs.org/
cClick The LTS version to download the installer.
follow the installation prompts, and run below to verify the installation.

node -v
npm -v

5: Install Node.js dependencies
run (on Terminal):
npm install

6: install npm modules
run (on Terminal):
npm install dotenv express passport express-session multer http-proxy-middleware socket.io

7: Install python
run (on Terminal):
brew install python3

8: Set up python virtual enviroment
Find clone-factory-v1 file that you downloaded on Finder and click Get Info.
Look at Where section Replace /path/to/your/repository with the actual path.
run below one by one (on Terminal):
cd /path/to/your/clone-factory-v1
python3 -m venv myenv
source myenv/bin/activate

9: Install Python dependencies
run (on Terminal):
pip install Flask flask-cors openai scikit-learn

10: Set up OPENAI_API_KEY
Go to https://platform.openai.com/ and create your account.
Move to API keys tab, click Create new secret key and copy the SECRET KEY.
go to .env file and paste the key as below(no space around = sign).

OPENAI_API_KEY=sk-58nduZKAtpo8HCd1KiiWP7dg4wWuS4vp3JYw2TEST

11: Charge your OPENAI account
In order to fine-tune a model with your dataset, it costs a bit of money.
(Depends on the amount of your chat history data but $5~10 should be enough)
Go to Billing tab in Setting and Charge it.

#Start Your Application

1: Start the Node.js server
Replace /path/to/your/repository with the actual path and run (on Terminal):
cd /path/to/your/clone-factory-v1

node app.js

2: Start the Flask server
open another Terminal Window.
Replace /path/to/your/repository with the actual path and run below one by one(on Terminal):
cd /path/to/your/clone-factory-v1
export FLASK_APP=chat_with_model.py
flask run

3: Play with the app
Open your web browser and navigate to http://localhost:3000
Play with the app
