import subprocess, os, sys

os.chdir("/root/wx-study-helper")

def run(cmd, check=True):
    print(f"$ {cmd}")
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.stdout: print(r.stdout[:500])
    if r.stderr: print(r.stderr[:500])
    if check and r.returncode != 0:
        print(f"FAILED with code {r.returncode}")
    return r.returncode

run("git init")
run('git config user.name "Firefly-8"')
run('git config user.email "1029299126@qq.com"')
run("git add README.md .gitignore index.json content/")
run("git status")
run('git commit -m "Phase 1: 90 books content asset (psychology 30 + economics 30 + philosophy 30)"')
run("git branch -M main")
run("git remote add origin https://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@github.com/Firefly-8/literature-content.git")
run("git push -u origin main")
