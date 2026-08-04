import subprocess, os

os.chdir("/root/wx-study-helper")

def run(cmd):
    print(f"$ {cmd}")
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=120)
    if r.stdout: print(r.stdout[:1000])
    if r.stderr: print(r.stderr[:1000])
    return r.returncode

# Increase buffer, disable SSL verify (for push only), use single thread
run("git config http.postBuffer 524288000")
run("git config http.version HTTP/1.1")
run("git config http.sslVerify false")

# Try push with verbose to see what happens
rc = run("git push -u origin main --verbose")
print(f"\nFinal return code: {rc}")
