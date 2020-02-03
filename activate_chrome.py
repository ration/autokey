# Enter script code
# Activate chrome, and if it is's active activate quick tabs
import time
current = window.get_active_title().lower()
if 'chrome' in current:
    keyboard.send_keys('<ctrl>+q')   
else:
    window.activate('chrome', switchDesktop=True)
