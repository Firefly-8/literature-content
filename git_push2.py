import subprocess, os, time

os.chdir("/root/wx-study-helper")

def run(cmd):
    print(f"$ {cmd}")
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.stdout: print(r.stdout[:800])
    if r.stderr: print(r.stderr[:800])
    return r.returncode

# Retry push up to 3 times
for attempt in range(3):
    print(f"\n=== Push attempt {attempt+1} ===")
    rc = run("git push -u origin main")
    if rc == 0:
        print("PUSH SUCCESS!")
        break
    print(f"Failed, retrying in 10s...")
    time.sleep(10)
