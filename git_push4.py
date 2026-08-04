import subprocess, os

os.chdir("/root/wx-study-helper")

def run(cmd, timeout=300):
    print(f"$ {cmd}")
    env = os.environ.copy()
    env["GIT_SSL_NO_VERIFY"] = "1"
    env["GIT_HTTP_LOW_SPEED_LIMIT"] = "1000"
    env["GIT_HTTP_LOW_SPEED_TIME"] = "60"
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout, env=env)
    if r.stdout: print(r.stdout[:1000])
    if r.stderr: print(r.stderr[:1000])
    return r.returncode

# Push with SSL verify disabled
rc = run("git push -u origin main", timeout=300)
print(f"\nFinal return code: {rc}")
