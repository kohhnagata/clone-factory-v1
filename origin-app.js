require('dotenv').config();
const express = require('express');
const path = require('path');
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20').Strategy;
const session = require('express-session');
const multer = require('multer');
const { execFile } = require('child_process');
const fs = require('fs');
const http = require('http');

const app = express();
const server = http.createServer(app);
const io = require('socket.io')(server);

const PORT = process.env.PORT || 3000;
const upload = multer({ dest: 'uploads/' });

const { Pool } = require('pg');
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: {
    rejectUnauthorized: false
  }
});

app.use(express.static(path.join(__dirname, 'public')));

passport.use(new GoogleStrategy({
    clientID: "578760609373-dtnp3q0pdgm2ob6t9ip9n6c6oa01mmeb.apps.googleusercontent.com",
    clientSecret: "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",
    callbackURL: "http://localhost:3000/auth/google/callback"
  }, (accessToken, refreshToken, profile, cb) => cb(null, profile)
));

passport.serializeUser((user, done) => done(null, user));
passport.deserializeUser((obj, done) => done(null, obj));

app.use(session({ secret: "secret", resave: false, saveUninitialized: true }));
app.use(passport.initialize());
app.use(passport.session());

app.get('/auth/google', passport.authenticate('google', { scope: ['profile', 'email'] }));
app.get('/auth/google/callback', passport.authenticate('google', { failureRedirect: '/sign-in' }), (req, res) => res.redirect('/user-profile'));
app.get('/sign-in', (req, res) => res.sendFile(path.join(__dirname, 'public', 'sign-in.html')));
app.get('/user-profile', (req, res) => req.isAuthenticated() ? res.sendFile(path.join(__dirname, 'public', 'user-profile.html')) : res.redirect('/sign-in'));
app.get('/logout', (req, res) => { req.logout(); res.redirect('/sign-in'); });
app.get('/delete-account', (req, res) => { if (req.isAuthenticated()) { req.logout(); res.redirect('/sign-in'); } else { res.redirect('/sign-in'); }});
app.get('/', (req, res) => res.sendFile(path.join(__dirname, 'public', 'sign-in.html')));

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

// Define endpoints for each chat type
app.post('/upload-whatsapp-history', upload.array('chatHistory', 10), (req, res) => {
    processChatHistory(req, res, 'clean-chat-history.py');
});

app.post('/upload-telegram-history', upload.array('chatHistory', 10), (req, res) => {
    processChatHistory(req, res, 'telegram-clean-chat-history.py');
});

app.post('/upload-instagram-messenger-history', upload.array('chatHistory', 10), (req, res) => {
    processChatHistory(req, res, 'instagram-messenger-clean-chat-history.py');
});

app.post('/upload-chat-history', async (req, res) => {
    // Assuming 'cleanChatHistory' is a function that cleans and returns the cleaned chat content
    const cleanedChatContent = cleanChatHistory(req.file);
    await storeChatHistory(req.user.id, req.body.chatType, cleanedChatContent);
    res.send('Chat history uploaded and stored successfully');
  });  


app.get('/chat-history-upload', (req, res) => res.sendFile(path.join(__dirname, 'public', 'chat-history-upload.html')));


// storing chat history function
async function storeChatHistory(userId, chatType, cleanedChatContent) {
    await pool.query('INSERT INTO chat_history(user_id, chat_type, content) VALUES ($1, $2, $3)', [userId, chatType, cleanedChatContent]);
  }
  

app.get('/chat-interface', (req, res) => {
    // Optional: check if the user is authenticated
    res.sendFile(path.join(__dirname, 'public', 'chat-interface.html'));
});

app.get('/clone-creation', (req, res) => {
    // Optional: Check if the user is authenticated
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
