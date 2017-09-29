def test_updateServer(monkeypatch):
    from xenserver import tasks
    from xenserver.tests.helpers import XenServerHelper
    xshelper = XenServerHelper()
    # $HL
    monkeypatch.setattr(tasks, 'getSession', xshelper.get_session)
    # $HL
    # ... Way too many lines of code to test updateServer() ...
