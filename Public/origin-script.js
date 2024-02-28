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
