var http    = require('http');
var express = require('express');
var io      = require('socket.io');
var ws      = require('express-ws');

var app     = express();
var server  = http.createServer(app);

io = io(server);
ws = ws(app, server);

var opts = {
    port: process.env.CONTROL_PORT || 1980
};

var brown = '\033[33m',
    green = '\033[32m',
    reset = '\033[0m';

app.use(function(req, res, next) {
    return next();
});

app.get('/', function(req, res, next) {
    console.log(brown + "http: " + reset + req.testing + " " + req);
    // io.emit('pebble', {button: "up"});
    res.end();
});

app.ws('/', function(ws, req) {
    ws.on('message', function(msg) {
        io.emit('pebble', {button: msg});
        console.log(brown + "pebble: " + reset + msg);
    });
    console.log(brown + "pebble connected: " + reset + ws);
});

io.on('connection', function(socket) {
    console.log(brown + "connection: " + reset + socket.id);
    socket.on('slide', function(data) {
        console.log(brown + "slide: " + reset + data.h + "." + data.v);
    });
});


server.listen(opts.port || null);
