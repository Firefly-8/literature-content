#!/bin/sh
curl -s -X POST \
  -H "Authorization: token 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" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/user/repos \
  -d '{"name":"literature-content","private":true,"description":"文学作品赏析内容资产"}'
