# Enter script code
current = window.get_active_title()
if 'firefox' in current.lower():
    keyboard.send_keys('<ctrl>+<shift>+x')
else:
    window.activate('firefox', switchDesktop=True)
