class SmppTransceiverTransport(Transport):
    # $HL
    clock = reactor
    # $HL
    # ... Quite a lot of transport implementation code ...

    def check_stop_throttling(self, delay=None):
        # ... A few lines of throttle-stop-checking code ...
        # $HL
        self._unthrottle_delayedCall = self.clock.callLater(
            delay, self._check_stop_throttling)
        # $HL
