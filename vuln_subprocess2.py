import subprocess

def vuln(cmd):
    subprocess.Popen(cmd, shell=True)  # 🚨 command injection risk

if __name__ == "__main__":
    vuln(input("cmd> "))
