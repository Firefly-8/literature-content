import requests, subprocess, os

# Test GitHub API connectivity
print("=== Testing GitHub API ===")
try:
    r = requests.get("https://api.github.com", timeout=10)
    print(f"API status: {r.status_code}")
except Exception as e:
    print(f"API error: {e}")

# Test raw GitHub HTTPS
print("\n=== Testing github.com HTTPS ===")
try:
    r = requests.get("https://github.com", timeout=10)
    print(f"github.com status: {r.status_code}")
except Exception as e:
    print(f"github.com error: {e}")

# Check if repo exists
print("\n=== Check repo exists ===")
TOKEN = "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"
try:
    r = requests.get("https://api.github.com/repos/Firefly-8/literature-content",
                     headers={"Authorization": "token " + TOKEN}, timeout=10)
    print(f"Repo status: {r.status_code}")
    if r.status_code == 200:
        print("Repo exists!")
except Exception as e:
    print(f"Error: {e}")
