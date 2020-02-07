# Enter script code
current = window.get_active_class().lower()
if 'emacs' in current:
    keyboard.send_keys('<ctrl>+c')
    keyboard.send_key('f')
else:
    window.activate(title='emacs.Emacs', switchDesktop=True, matchClass=True)
