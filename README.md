
# Motivation

So, pretty much everywhere you look, people imagine and build Robot or AI from the productivity perspective. But growing up in Japan until I hit 17, I got a different vibe. Over there, robots in comics and anime are more like your friends or family than just automation tools. I mean, who hasn't wanted a pal like Doraemon? Growing up with these stories, I always dreamed that someday I’d have my own robot friend, someone as tight with me as Nobita is with Doraemon.

Of course, building a robot that has human like intelegence and emotion is still out there.
But, I figured, why not start small? I wanted to make a chat clone of myself.
Picture it, when you are feeling low and your clone picks you right up, reminding you of the stuff that really matters. 
Or think about having someone who gets you on a level that just seems beyond what anyone else can grasp.

But man, finding a simple way to make this clone was a mission.
GPTs only accepts 20 small files to add knoweldges.
AI clone apps like Replika, c.ai, Delphi.ai that don’t let you mess with your original data much.
fine-tuning GPT or other LLM requires dataset in a very specific format and this data cleaning task is absolutely nightmare.

I guess for experienced devs, tweaking a model with your original dataset is easy but non-technical ppl like me, it’s just alot.
And I'm not the only one – I've seen loads of folks on Reddit hitting the same wall.

So I thought, why not just build it?
Spent the past 1 month talking to LLMs and built a no-frills web app (designed for local use) where you can upload your chat history, create a clone, and start chatting away. 
Just clone the repo, set it up on your local machine, and you’re good to go.

It’s still a work in progress. I've got a whole list of things I want to add – like supporting more chat apps, bumping up the fine-tuning quality, and making the chat feel more natural. If you’re interested in improving this app or helping ppl to build relationship with machines, hit me up. @ https://twitter.com/koheingt

# Key Features
- Upload chat history from WhatsApp, Telegram, and Instagram Messenger
- Clean and reformat chat history for preparing dataset
- Fine-tune a chat model based on users chat history
- Engage in conversations with the your chat clone through a web interface

# Prerequisites
Before starting, ensure you have the following:

- Node.js
- Python 3
- Required npm modules (detailed below)
- Necessary Python packages (specified below)
- OpenAI API key
- Your chat history files

# Installation Guide
This guide is designed to be accessible for users of all technical backgrounds. If you're already familiar with the prerequisites, feel free to skip the corresponding steps. This guide is primarily for macOS users, but steps for Windows users may be added in the future.

# Setting Up Your Environment

## Install Homebrew:
Open Terminal and execute:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Install Git:
In Terminal, run:

```
brew install git
```

## Clone the Repository:
Execute the following command in Terminal:

```
git clone https://github.com/kohhnagata/clone-factory-v1
```

## Install Node.js and npm:

Visit Node.js official website and download the LTS version installer.
Follow the installation instructions.
Verify the installation by running the following commands in Terminal:

```
node -v
npm -v
```

## Install Node.js Dependencies:
In Terminal, execute:

```
npm install
```

## Install Required npm Modules:
Run the following command in Terminal:

```
npm install dotenv express passport express-session multer http-proxy-middleware socket.io
```

## Install Python:
Execute in Terminal:

```
brew install python3
```

## Set Up Python Virtual Environment:

Locate the clone-factory-v1 directory in Finder and note its path.
In Terminal, replace /path/to/your/repository with your actual path and execute the following commands:

```
cd /path/to/your/clone-factory-v1
python3 -m venv myenv
source myenv/bin/activate
```

## Install Python Dependencies:
In Terminal, run:

```
pip install Flask flask-cors openai scikit-learn
```

## Set Up OPENAI_API_KEY:

Visit OpenAI Platform, create an account, and navigate to the API keys tab.
Create a new secret key, copy it, and paste it into the .env file like so (ensure there are no spaces around the = sign):

```
OPENAI_API_KEY=your_secret_key_here
```

## Fund Your OpenAI Account:

Model fine-tuning requires funding. The cost depends on your data volume, but typically $5-$10 is sufficient.
Navigate to the Billing tab in Settings and add funds as needed.

# Starting the Application

## Start the Node.js Server:

Replace /path/to/your/repository with your actual path and run the following command in Terminal:

```
cd /path/to/your/clone-factory-v1
node app.js
```

## Start the Flask Server:

Open another Terminal window, replace /path/to/your/repository with your actual path, and execute the following commands:

```
cd /path/to/your/clone-factory-v1
export FLASK_APP=chat_with_model.py
flask run
```

## Explore the Application:

Open a web browser and navigate to http://localhost:3000.
Enjoy interacting with your personalized chat clone app!
