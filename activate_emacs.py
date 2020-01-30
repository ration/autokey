# Enter script code
current = window.get_active_title().lower()
if 'emacs' in current:
    keyboard.send_keys('<ctrl>+c')
    keyboard.send_key('f')
else:
    window.activate('emacs', switchDesktop=True)
