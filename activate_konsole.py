# Enter script code
import time
current = window.get_active_title().lower()
if 'konsole' in current.lower():
   keyboard.send_keys('<ctrl>+l')
   # Activate fzf from home
   keyboard.send_keys('cd ~/**')
   keyboard.send_keys('<tab>')
else: 
   window.activate('konsole', switchDesktop=True)
