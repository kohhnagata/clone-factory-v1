# Motivation

So, pretty much everywhere you look, people imagine and build Robot or AI from the productivity perspective. But growing up in Japan until I hit 17, I got a different vibe. Over there, robots in comics and anime are more like your friends or family than just automation tools. I mean, who hasn't wanted a pal like Doraemon? Growing up with these stories, I always dreamed that someday I’d have my own robot friend, someone as tight with me as Nobita is with Doraemon.

Of course, building a robot that has human like intelegence and emotion is still out there.
But, I figured, why not start small? I wanted to make a chat clone of myself.
Picture it, when you are feeling low and your clone picks you right up, reminding you of the stuff that really matters.
Or think about having someone who gets you on a level that just seems beyond what anyone else can grasp.

But man, finding a simple way to make this clone was a mission.
GPTs accepts up to only 20 small files to add knoweldges.
AI clone apps like Replika, [c.ai](http://c.ai/), [Delphi.ai](http://delphi.ai/) don’t let you mess with your original data much.
fine-tuning GPT or other LLM requires dataset in a very specific format and this data cleaning task is absolutely nightmare.

I guess for experienced devs, tweaking a model with your dataset is easy but non-technical ppl like me, it’s just alot.
And I'm not the only one – I've seen loads of folks on Reddit hitting the same wall.

if i cant find a simple solution, then fuck it i'll build it.
Spent the past 1 month talking to LLMs and built a no-frills web app (for local use) where you can upload your chat history, create a clone, and start chatting away.
Just clone the repo, set it up on your local machine, and you’re good to go.

It’s still a work in progress. I've got a whole list of things I want to add – like supporting more chat apps, bumping up the fine-tuning quality, and making the chat feel more natural. If you’re interested in improving this app or helping ppl to build relationship with machines, hit me up. @ https://twitter.com/koheingt

# Key Features

- Upload chat history from WhatsApp, Telegram, Instagram, and Facebook Messenger
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

# Privacy

Chat history is such a highly personal and confidential thing. That's why I've crafted this app to prioritize your privacy above all. To use it, simply clone the repository and deploy it locally on your computer. This way, your chat history remains securely within your own system, without the risk of exposure.

However, it's important to note there is one exception. During the model fine-tuning process, your chat history files will be uploaded to your OpenAI Platform account. This step is crucial for personalizing the model to better serve your needs. Rest assured, you have the option to delete these files from your account once fine-tuning is complete. I believe in transparency and want to ensure you're fully informed about how your data is handled.

# Installation Guide

This guide is designed to be accessible for everyone especially non-tech ppl. If you're already familiar with the prerequisites, feel free to skip the corresponding steps. This guide is primarily for macOS users, but steps for Windows users may be added in the future.

# Setting Up Your Environment

## Install Homebrew:

Open Terminal and execute:

```
/bin/bash -c "$(curl -fsSL <https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh>)"
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
Create a new secret key, copy it, and replace your_secrect_key_here in the .env file (ensure there are no spaces around the = sign):

```
OPENAI_API_KEY=your_secret_key_here
```

## Fund Your OpenAI Account:

Model fine-tuning requires funding. The cost depends on your data volume, but typically $5-$10 is sufficient.
Navigate to the Billing tab in Settings and add funds as needed.

# Getting Your Chat History

## Telegram

1. Make sure you have the desktop version of Telegram installed on your computer. If not, download it from Telegram's official website and log in with your credentials.
2. Click on the three lines (menu) icon in the top-left corner of the app. From the menu, select "Settings" or "Preferences" (this may vary depending on your operating system).
3. In the settings menu, look for an "Advanced" option. Click on it to access the advanced settings.
4. Within the advanced settings, you should find an option to "Export Telegram data" in the buttom. This feature allows you to download your chat history, along with other data like media and files. Click on this option.
5. Uncheck unnessesary data (ex. Account Information, Contact list, Story archive, Private groups, Photos) and only check “Personal chats”. 
    
    👉 And most importantly make sure to increase the Size Limit from 8MB to 4000MB and **choose “Machine-readable JSON” as data format**. 
    
6. Click on the "Export" button. Telegram will then prepare the data for download. This process can take some time, depending on the amount of data you are exporting. The data is typically saved in a ZIP archive. Unzip this archive to access your chat history.

## WhatsApp

1. Launch WhatsApp on your smartphone.
2. Navigate to the chat you wish to download the history of.
3. Tap on the chat name at the top of the screen or tap the three dots/menu button in the top right corner (this might vary slightly depending on your device) to access chat settings.
4. Scroll down and select "Export chat" and choose “Without Media”.
5. You'll be prompted to choose how you want to export the chat. You can email it to yourself, use cloud storage services like Google Drive or Dropbox, or save to files.

## Instagram

1. Launch the Instagram app or website and log in to your account.
2. On the mobile app, go to your profile, tap the menu (three lines) in the top right corner, and select "Settings". On the web, click your profile picture in the top right corner, select "Settings", and then click "Your activity".
3. Click Download or transfer information, check your instagram account and tap Next.
4. Click Some of your information, check only “Messages” and tap Next.
5. Check Download to device, and tap Next.
    
    👉on the next page, Choose All time as Data range (or customise as you wish), **Choose JSON as data format**, media quality is no-related since you are only downloading chat history.
6. Submit the request and wait for an email with the download link.

## Facebook Messenger

1. Log in to your Facebook account and go to "Settings & Privacy" > "Settings" > "Your Facebook Information" > "View" beside "Download Your Information."
2. Select "Request a download,"  check only “Messages” and tap Next.
3. Check Download to device, and tap Next.
    
    👉on the next page, Choose All time as Data range (or customise as you wish), **Choose JSON as data format**, media quality is no-related since you are only downloading chat history.
4. Submit the request and wait for an email with the download link.

# Starting the Application

## Start the Node.js Server:

Replace /path/to/your/ with your actual path to clone-factory-v1 file and run the following command in Terminal:

```
cd /path/to/your/clone-factory-v1
node app.js
```

## Start the Flask Server:

Open “another” Terminal window, replace /path/to/your/ with your actual path, and execute the following commands:

```
cd /path/to/your/clone-factory-v1
export FLASK_APP=chat_with_model.py
flask run
```

## Open the application:

Open a web browser and navigate to [http://localhost:3000](http://localhost:3000/).

# Playing the Application

## Upload chat history

Navigate to the Upload Chat History page within the application.
Follow [the getting-your-chat-history guide](https://www.notion.so/Guide-Book-Clone-Factory-v1-4acbdbb7d116419ca07ae6369be27427?pvs=21) to download your chat history and upload it to the application. Ensure your name matches exactly as it appears in the chat application to facilitate accurate message extraction.

## Start fine-tuning a model

Visit the Create Your Clone page.
Click the Start Fine-Tuning button and monitor the fine-tuning progress at https://platform.openai.com/finetune. The fine-tuning process includes several statuses: Created fine-tuning job, Validating training file, Fine-tuning job started, New fine-tuned model created, and The job has successfully completed.
If the OPENAI Platform's fine-tuning page doesn't display any model training, check your terminal for potential errors.

## Chat with your clone

After the fine-tuning job completes, copy the model ID (not the job ID) from https://platform.openai.com/finetune. The model ID looks like ft:gpt-3.5-turbo-0125:personal:clone-factory-v1:90UcjZ7r.
Navigate to the application's chat interface page and paste the model ID into the Enter your model name section.
Everything is now set up for you to enjoy chatting with your clone!
