(function() {
    var pebble = Reveal.getConfig().pebble;
    var socket = io(pebble.url);

    console.log(pebble.url);

    socket.on('pebble', function(data) {
        console.log("pebble: " + data.button);
        switch (data.button) {
        case "up": Reveal.prev(); break;
        case "down": Reveal.next(); break;
        }
        socket.emit('slide', Reveal.getIndices());
    });
}());
