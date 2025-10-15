import os

def main():
    user_input = input("Enter command: ")
    os.system(user_input)  # 🚨 This will trigger CodeQL alert

if __name__ == "__main__":
    main()
