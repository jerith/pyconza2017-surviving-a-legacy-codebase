@app.task(time_limit=60)
def updateServer(xenserver):
    # $HL
    session = getSession(
        xenserver.hostname, xenserver.username, xenserver.password)
    # $HL
    # ... Dozens of lines of code to update a server ...
    for vmref, vmobj in allvms.items():
        # $HL
        updateVm.delay(xenserver, vmref, vmobj)
        # $HL
    # ... Dozens more lines of server-related code ...

@app.task(time_limit=60)
def updateVm(xenserver, vmref, vmobj):
    # ... A few lines of check and setup code ...
    # $HL
    session = getSession(
        xenserver.hostname, xenserver.username, xenserver.password)
    # $HL
    # ... Dozens of lines of code to update the VM ...
