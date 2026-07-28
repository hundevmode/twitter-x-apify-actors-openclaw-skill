# Troubleshooting

## Common failures

### 401 / 403 from Apify
- Token is missing or invalid.
- Pass `--apify-token` or set `APIFY_TOKEN` in environment.
- Keep the token in the `Authorization` header. Never add it to a URL.

### 402 from Apify
- Stop the run.
- Review current Actor pricing and Apify billing.
- Request fresh approval before retrying.

### Actor returns empty array
- Username is invalid or actor did not find records.
- Verify target with `parse-username` command first.

### Email merge returns zero emails
- Enrichment actor may have no matches.
- Run pipeline with `--include-emails` only when needed.

### Bad collectType or limit
- Supported collect types: `followers`, `following`, `both`.
- `limit` must be a positive integer.

## Safe defaults
- Start with `collect-type=followers`
- Start with `limit=300` for initial tests
- Keep `--include-emails` disabled for fast low-cost checks
- Run Xquik commands without `--execute` until the exact plan is approved

## Minimal smoke test

```bash
APIFY_TOKEN='apify_api_xxx' \
python3 scripts/apify_twitter_actors.py run-pipeline \
  --target 'https://x.com/elonmusk' \
  --collect-type followers \
  --limit 100 \
  --include-emails
```
