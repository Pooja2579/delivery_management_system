const http = require('http');
const socketIo = require('socket.io');

const server = http.createServer();
const io = socketIo(server);

io.on('connection', (socket) => {
    console.log('A user connected');

    // Handle events and emit messages
    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});

server.listen(8000, () => {
    console.log('Socket.io server listening on port 8000');
});
