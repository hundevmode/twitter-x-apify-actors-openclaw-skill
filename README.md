# Twitter/X Apify Actors Skill for OpenClaw (Followers + Optional Email Enrichment)

A production-focused OpenClaw skill to run **Twitter/X lead collection** with Apify actors: collect followers/following and optionally enrich with emails.

This skill is built for teams that need repeatable **Twitter lead generation automation** without manually wiring actor payloads each time.

## Actor Links

- Followers / following actor: [https://console.apify.com/actors/bIYXeMcKISYGnHhBG](https://console.apify.com/actors/bIYXeMcKISYGnHhBG)
- Email enrichment actor: [https://console.apify.com/actors/mSaHt2tt3Z7Fcwf0o](https://console.apify.com/actors/mSaHt2tt3Z7Fcwf0o)

## What This Skill Does

- Extracts username from `x.com`, `twitter.com`, or `@handle`
- Builds actor-ready payloads for follower/following collection
- Runs follower actor and normalizes output rows
- Optionally runs email actor and merges email/name data
- Returns JSON with metrics and outreach-ready rows

## Why Use This Skill

If you are searching for workflows like:

- Twitter followers scraper automation
- X lead generation with Apify
- Twitter email enrichment pipeline
- OpenClaw skill for Apify actors

this skill gives you a clean, reusable pattern for those exact tasks.

## Repository Structure

- `SKILL.md` - trigger rules, workflow, execution guidance
- `agents/openai.yaml` - OpenClaw UI metadata
- `scripts/apify_twitter_actors.py` - actor runner CLI
- `references/actor-contracts.md` - payload and output contracts
- `references/troubleshooting.md` - common failures and fixes

## Requirements

- Python 3.10+
- `requests`
- Apify API token

Install dependencies:

```bash
pip install -r requirements.txt
```

## Authentication (Apify)

Two supported ways:

### Option A: Environment variable (recommended)

```bash
export APIFY_TOKEN='apify_api_xxx'
```

### Option B: CLI argument

```bash
--apify-token 'apify_api_xxx'
```

If both are provided, `--apify-token` wins.

## Quick Start

### 1) Parse username

```bash
python3 scripts/apify_twitter_actors.py parse-username --target 'https://x.com/elonmusk'
```

### 2) Collect followers/following only

```bash
APIFY_TOKEN='apify_api_xxx' \
python3 scripts/apify_twitter_actors.py run-followers \
  --target 'https://x.com/elonmusk' \
  --collect-type followers \
  --limit 1000
```

### 3) Full pipeline with optional email enrichment

```bash
APIFY_TOKEN='apify_api_xxx' \
python3 scripts/apify_twitter_actors.py run-pipeline \
  --target 'https://x.com/elonmusk' \
  --collect-type followers \
  --limit 1000 \
  --include-emails
```

## Commands

- `parse-username`
- `run-followers`
- `run-pipeline`

Supported collect types:

- `followers`
- `following`
- `both`

## Output Format

`run-pipeline` returns:

- `targetUsername`
- `collectType`
- `includeEmails`
- `totalCollected`
- `emailsFound`
- `rows[]` with `username`, `name`, `email`, `sourceType`, `collectedAt`

This is ready for n8n, CSV export, Google Sheets, or CRM staging.

## Install as OpenClaw Skill

If your OpenClaw/skills runtime supports GitHub install:

```bash
npx skills add hundevmode/twitter-x-apify-actors-openclaw-skill --skill twitter-x-apify-actors
```

List skills in repo:

```bash
npx skills add hundevmode/twitter-x-apify-actors-openclaw-skill --list
```

## ClawHub Publishing Notes

Before publishing to ClawHub:

1. Confirm `SKILL.md` frontmatter is correct
2. Ensure `agents/openai.yaml` metadata is present
3. Run a smoke test with valid `APIFY_TOKEN`
4. Keep actor IDs documented and configurable

## SEO Tags

Twitter scraper, X followers scraper, Apify actors, OpenClaw skill, email enrichment, Twitter lead generation, outbound automation, growth automation.

## License

MIT (free for commercial and private use).
