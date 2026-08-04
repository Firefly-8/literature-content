#!/bin/sh
cd /root/wx-study-helper

git init
git config user.name "Firefly-8"
git config user.email "1029299126@qq.com"

git add README.md .gitignore index.json content/
git commit -m "Phase 1: 90 books content asset (psychology 30 + economics 30 + philosophy 30)"

git branch -M main
git remote add origin https://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@github.com/Firefly-8/literature-content.git
git push -u origin main
