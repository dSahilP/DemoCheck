import pickle
import sys

def load_data(serialized):
    # 🚨 Unsafe: untrusted pickle load
    data = pickle.loads(serialized)
    return data

if __name__ == "__main__":
    # Example: read base64 input on command line (for demonstration only)
    import base64
    s = input("base64> ")
    raw = base64.b64decode(s)
    print(load_data(raw))
