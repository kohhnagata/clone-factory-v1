require('dotenv').config();
const express = require('express');
const path = require('path');
const passport = require('passport');
const session = require('express-session');
const multer = require('multer');
const { execFile } = require('child_process');
const fs = require('fs');
const http = require('http');
const { spawn } = require('child_process');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();
const server = http.createServer(app);
const io = require('socket.io')(server);

const PORT = process.env.PORT || 3000;
const upload = multer({ dest: 'uploads/' });

app.use(express.static(path.join(__dirname, 'public')));

passport.serializeUser((user, done) => done(null, user));
passport.deserializeUser((obj, done) => done(null, obj));

app.use(session({ secret: "secret", resave: false, saveUninitialized: true }));
app.use(passport.initialize());
app.use(passport.session());
// Proxy endpoint
app.use('/chat', createProxyMiddleware({ 
    target: 'http://127.0.0.1:5000', // Target host
    changeOrigin: true, // needed for virtual hosted sites
}));

app.get('/', (req, res) => res.sendFile(path.join(__dirname, 'public', 'index.html')));

// Adjusted section for uploading and moving chat history
const cleanedDirPath = path.join(__dirname, 'cleaned_chat_history');
if (!fs.existsSync(cleanedDirPath)) fs.mkdirSync(cleanedDirPath);

// Function to process a single chat history file
function processSingleChatHistory(file, scriptName) {
    return new Promise((resolve, reject) => {
        const inputFilePath = file.path;
        const outputFilePath = path.join(cleanedDirPath, `${file.filename}.json`);
        execFile('python3', [scriptName, inputFilePath, outputFilePath], (error, stdout, stderr) => {
            if (error) {
                console.error(`Error: ${error.message}`);
                reject(`Error processing chat history file: ${file.filename}`);
            } else {
                resolve(stdout);
            }
        });
    });
}

// Modified processChatHistory function to handle multiple files
function processChatHistory(req, res, scriptName) {
    if (req.files && req.files.length > 0) {
        // Process all files using Promise.all
        Promise.all(req.files.map(file => processSingleChatHistory(file, scriptName)))
            .then(results => {
                // Once all files are processed successfully
                res.send('All chat history files processed successfully.');
            })
            .catch(error => {
                // If there's an error with any file
                res.status(500).send(error);
            });
    } else {
        res.status(400).send('No files uploaded.');
    }
}

// Function to process a single chat history file with customizable username
function processSingleChatHistory(file, scriptName, userName) {
    return new Promise((resolve, reject) => {
        const inputFilePath = file.path;
        const outputFilePath = path.join(cleanedDirPath, `${file.filename}.json`);
        // Adding userName as the last argument to pass to the Python script
        execFile('python3', [scriptName, inputFilePath, outputFilePath, userName], (error, stdout, stderr) => {
            if (error) {
                console.error(`Error: ${error.message}`);
                reject(`Error processing chat history file: ${file.filename}`);
            } else {
                resolve(stdout);
            }
        });
    });
}

// Define endpoints for each chat type
app.post('/upload-whatsapp-history', upload.array('chatHistory', 10), (req, res) => {
    const userName = req.body.userName; // Assuming the form field for the user's name is 'userName'
    Promise.all(req.files.map(file => processSingleChatHistory(file, 'clean-chat-history.py', userName)))
        .then(results => {
            res.send('All chat history files processed successfully.');
        })
        .catch(error => {
            res.status(500).send(error);
        });
});

app.post('/upload-telegram-history', upload.array('chatHistory', 10), (req, res) => {
    const userName = req.body.userName; // Assuming the form field for the user's name is 'userName'
    Promise.all(req.files.map(file => processSingleChatHistory(file, 'telegram-clean-chat-history.py', userName)))
        .then(results => {
            res.send('All chat history files processed successfully.');
        })
        .catch(error => {
            res.status(500).send(error);
        });
});

app.post('/upload-instagram-messenger-history', upload.array('chatHistory', 10), (req, res) => {
    const userName = req.body.userName; // Assuming the form field for the user's name is 'userName'
    Promise.all(req.files.map(file => processSingleChatHistory(file, 'instagram-messenger-clean-chat-history.py', userName)))
        .then(results => {
            res.send('All chat history files processed successfully.');
        })
        .catch(error => {
            res.status(500).send(error);
        });
});

app.post('/upload-chat-history', async (req, res) => {
    // Assuming 'cleanChatHistory' is a function that cleans and returns the cleaned chat content
    const cleanedChatContent = cleanChatHistory(req.file);
    await storeChatHistory(req.user.id, req.body.chatType, cleanedChatContent);
    res.send('Chat history uploaded and stored successfully');
  });  

// Endpoint to start the fine-tuning process
app.post('/start-fine-tuning', (req, res) => {
    // Replace 'python3' and 'fine-tune.py' with your actual Python executable and script path
    const fineTuneProcess = spawn('python3', ['./fine-tune.py']);

    fineTuneProcess.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    fineTuneProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    fineTuneProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });

    res.json({message: "Fine-tuning process started."});
});


app.get('/chat-history-upload', (req, res) => res.sendFile(path.join(__dirname, 'public', 'chat-history-upload.html')));

app.get('/chat-interface', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'chat-interface.html'));
});

app.get('/clone-creation', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'clone-creation.html'));
});

// After setting up the http server and before the listen method
io.on('connection', (socket) => {
    console.log('A user connected');

    socket.on('disconnect', () => {
        console.log('User disconnected');
    });

    socket.on('chat message', (msg) => {
        // Broadcast message to everyone, including the sender
        io.emit('chat message', msg);
    });
});

server.listen(PORT, () => console.log(`Server running on port ${PORT}`));

// Assuming you have Express set up
app.post('/send-message', (req, res) => {
    const userMessage = req.body.message;
    // Process the message using your AI model
    const aiReply = 'This is a placeholder response from AI'; // Placeholder
    res.json({ reply: aiReply });
});
