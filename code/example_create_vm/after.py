@app.task(time_limit=120)
def create_vm(vm, xenserver, template, name, **others):
    session = getSession(
        xenserver.hostname, xenserver.username, xenserver.password)
    # $HL
    return _create_vm(session, vm, template, name, **others)

def _create_vm(session, vm, template, name, **others):
    # $HL
    storage = session.xenapi.SR.get_all()
    # ... Another 180 lines of VM creation using the session ...
