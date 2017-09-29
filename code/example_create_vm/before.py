@app.task(time_limit=120)
def create_vm(vm, xenserver, template, name, **others):
    session = getSession(
        xenserver.hostname, xenserver.username, xenserver.password)

    storage = session.xenapi.SR.get_all()
    # ... Another 180 lines of VM creation using the session ...
