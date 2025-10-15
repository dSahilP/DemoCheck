import os

def unsafe(user_input):
    os.system("echo " + user_input)  # 🚨 Command injection
