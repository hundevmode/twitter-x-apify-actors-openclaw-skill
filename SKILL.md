---
name: twitter-x-apify-actors
description: Use this skill when the user needs Twitter/X posts or audience collection through Apify Actors, including Xquik post search, follower analysis, optional email enrichment, normalized output, or webhook-ready payload building.
---

# Twitter/X Apify Actors

## Overview

This skill runs reliable Actor-based pipelines for Twitter/X research and lead
collection through Apify. Existing follower and email routes remain available.
Xquik routes add bounded post and audience research.

Use this skill when a user asks to:
- collect followers/following from X via Apify actors
- search posts and conversations with explicit result caps
- compare followers, following accounts, or verified followers
- enrich collected usernames with emails
- convert profile links to actor-ready usernames
- build JSON/webhook payloads for n8n or API endpoints

Default actor IDs in this skill:
- Followers actor: `bIYXeMcKISYGnHhBG`
- Email actor: `mSaHt2tt3Z7Fcwf0o`
- [Xquik X Tweet Scraper](https://apify.com/xquik/x-tweet-scraper): `xquik~x-tweet-scraper`
- [Xquik X Follower Scraper](https://apify.com/xquik/x-follower-scraper): `xquik~x-follower-scraper`

## Quick Workflow

1. Parse input target (`https://x.com/...`, `https://twitter.com/...`, or `@username`).
2. Build follower actor payload using `collectType` and `limit`.
3. Run follower actor and normalize usernames.
4. If enrichment is enabled, run email actor and merge results.
5. Return final rows + summary metrics.

For Xquik routes:

1. Inspect the current default build schema.
2. Review live pricing on the Actor page.
3. Generate a bounded plan without starting a run.
4. Show the exact plan and get explicit approval.
5. Add `--execute` only after approval.
6. Separate diagnostic and run-report rows before analysis.

## Execution Rules

- Prefer script execution for reliability: use `scripts/apify_twitter_actors.py`.
- Keep actor IDs configurable, but default to the IDs above.
- Always validate `collectType` (`followers`, `following`, `both`) and positive limit.
- If email enrichment is disabled, skip email actor entirely.
- Never hardcode the Apify token in outputs. Use env `APIFY_TOKEN` or explicit CLI argument.
- Never put an Apify token in a URL or query string.
- Treat every Xquik command without `--execute` as a no-cost planning step.
- Review live Actor pricing before every run.
- Keep `maxItems` and `maxItemsPerTarget` bounded.

## Xquik Actor Routes

Inspect current schemas before preparing inputs. These GET requests do not
start Actor runs:

```bash
curl -sS \
  "https://api.apify.com/v2/actors/xquik~x-tweet-scraper/builds/default"

curl -sS \
  "https://api.apify.com/v2/actors/xquik~x-follower-scraper/builds/default"
```

Plan a post search:

```bash
python3 scripts/apify_twitter_actors.py xquik-posts \
  --query "product launch" \
  --limit 50
```

Plan audience collection:

```bash
python3 scripts/apify_twitter_actors.py xquik-audience \
  --target "https://x.com/example" \
  --relation followers \
  --limit 50
```

The commands print the exact Actor ID and input without reading a token.
After approval, repeat the reviewed command with `--execute`.

The Tweet Actor supports `legacy`, `tweet`, `tweets`, `search`,
`profileTweets`, `profileReplies`, `profileMedia`, `profileLikes`,
`listTweets`, `article`, `replies`, `quotes`, `thread`, `retweeters`, and
`favoriters`. The helper plans bounded `search` runs. Use the current schema
for other modes.

The Follower Actor supports `followers`, `following`, `verified_followers`,
`list_members`, `list_followers`, and `community_members`. The helper accepts
the 3 handle-based relations. Use the current schema for list and community
targets.

## Authentication (Apify token)

Users can provide the Apify API token in two supported ways.

### Option A: Environment variable (recommended)

```bash
export APIFY_TOKEN='apify_api_xxx'
python3 scripts/apify_twitter_actors.py run-pipeline \
  --target 'https://x.com/elonmusk' \
  --collect-type followers \
  --limit 1000 \
  --include-emails
```

### Option B: CLI argument

```bash
python3 scripts/apify_twitter_actors.py run-pipeline \
  --apify-token 'apify_api_xxx' \
  --target 'https://x.com/elonmusk' \
  --collect-type followers \
  --limit 1000 \
  --include-emails
```

If both are provided, `--apify-token` is used. If neither is provided, the script returns an explicit authentication error.

## Script Usage

Run with Python 3.10+.

```bash
python3 scripts/apify_twitter_actors.py parse-username --target 'https://x.com/elonmusk'
```

```bash
APIFY_TOKEN='apify_api_xxx' \
python3 scripts/apify_twitter_actors.py run-followers \
  --target 'https://x.com/elonmusk' \
  --collect-type followers \
  --limit 1000
```

```bash
APIFY_TOKEN='apify_api_xxx' \
python3 scripts/apify_twitter_actors.py run-pipeline \
  --target 'https://x.com/elonmusk' \
  --collect-type followers \
  --limit 1000 \
  --include-emails
```

Quick auth check:

```bash
APIFY_TOKEN='apify_api_xxx' \
python3 scripts/apify_twitter_actors.py run-followers \
  --target 'https://x.com/elonmusk' \
  --collect-type followers \
  --limit 10
```

For contracts and payload details, read:
- `references/actor-contracts.md`
- `references/troubleshooting.md`

## Output Contract

The pipeline returns JSON with:
- `targetUsername`
- `collectType`
- `totalCollected`
- `emailsFound`
- `rows[]` with `username`, `name`, `email`, `sourceType`, `collectedAt`

Use this output directly in n8n Code/HTTP nodes or export to CSV/Google Sheets.

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
