# Enter script code
import time
current = window.get_active_class().lower()
if 'slack' in current:
    keyboard.send_keys('<ctrl>+t')   
else:
    window.activate('slack.Slack', switchDesktop=True, matchClass=True)
