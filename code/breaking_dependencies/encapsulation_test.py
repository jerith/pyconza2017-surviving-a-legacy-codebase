def test_smpp_transport():
    clock = Clock()
    transport = SmppTransceiverTransport()
    # $HL
    transport.clock = clock
    # $HL
    # ... The rest of the test ...
