import subprocess, os

os.chdir("/root/wx-study-helper")

def run(cmd):
    print(f"$ {cmd}")
    env = os.environ.copy()
    env["GIT_SSL_NO_VERIFY"] = "1"
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300, env=env)
    if r.stdout: print(r.stdout[:500])
    if r.stderr: print(r.stderr[:500])
    return r.returncode

run("git add -A")
run('git commit -m "Phase 2: poems 209 + characters 154 + summaries 68 + quiz 130"')
run("git push -u origin main --verbose")
