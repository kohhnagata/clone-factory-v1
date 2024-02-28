document.getElementById('setName').addEventListener('click', function() {
    const chatName = document.getElementById('chatName').value;
    fetch('/api/set-name', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: chatName }),
    })
    .then(response => response.json())
    .then(data => {
        alert('Chat name set successfully!');
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

document.getElementById('logout').addEventListener('click', function() {
    fetch('/api/logout')
    .then(() => {
        window.location.href = '/'; // Redirect to home or login page
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

document.getElementById('deleteAccount').addEventListener('click', function() {
    if (confirm('Are you sure you want to delete your account? This action cannot be undone.')) {
        fetch('/api/delete-account')
        .then(() => {
            window.location.href = '/'; // Redirect to home or login page
        })
        .catch((error) => {
        console.error('Error:', error);
        });
    }
});

document.getElementById('send-btn').addEventListener('click', function() {
    const input = document.getElementById('chat-input');
    const message = input.value.trim();
    if (message) {
        displayMessage(message, 'You');
        sendMessageToServer(message);
    }
    input.value = ''; // Clear input after sending
});

function displayMessage(message, sender) {
    const chatBox = document.getElementById('chat-box');
    const msgElement = document.createElement('div');
    msgElement.classList.add('message');
    msgElement.textContent = `${sender}: ${message}`;
    chatBox.appendChild(msgElement);
}

function sendMessageToServer(message) {
    // Implement AJAX request to send message to your server here
    // Example using Fetch API
    fetch('/send-message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
    })
    .then(response => response.json())
    .then(data => {
        displayMessage(data.reply, 'AI Friend');
    })
    .catch(error => console.error('Error:', error));
}
