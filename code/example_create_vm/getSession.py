def getSession(hostname, username, password):
    session = xenapi.Session('https://%s:443/' % (hostname))
    session.xenapi.login_with_password(username, password)
    return session
