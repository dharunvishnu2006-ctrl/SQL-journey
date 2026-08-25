import os

if os.path.exists('agents.db'):
    os.remove('agents.db')
    print("agents.db deleted")
else:
    print("agents.db not found")

if os.path.exists('threats.db'):
    os.remove('threats.db')
    print("threats.db deleted")
else:
    print("threats.db not found")