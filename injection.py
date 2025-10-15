import subprocess

def main():
    cmd = input("Enter command: ")
    subprocess.call(cmd, shell=True)  # 🚨 definite command injection

if __name__ == "__main__":
    main()
