# Actor Contracts: Twitter/X Followers + Email

## Xquik X Tweet Scraper

Actor: [Xquik X Tweet Scraper](https://apify.com/xquik/x-tweet-scraper)

The helper uses a bounded search payload:

```json
{
  "mode": "search",
  "searchTerms": ["product launch"],
  "queryType": "Latest + Top",
  "includeSearchTerms": true,
  "outputVariant": "rich",
  "fieldStyle": "camelCase",
  "outputPreset": "nested",
  "maxItems": 50,
  "maxItemsPerTarget": 50
}
```

Inspect the current default build schema before using another mode.

## Xquik X Follower Scraper

Actor: [Xquik X Follower Scraper](https://apify.com/xquik/x-follower-scraper)

The helper accepts handle-based relations:

```json
{
  "twitterHandles": ["example"],
  "relation": "followers",
  "outputMode": "compact",
  "includeTargetMetadata": true,
  "dedupeMode": "merge",
  "maxItems": 50,
  "maxItemsPerTarget": 50
}
```

Use the current input schema for list and community targets.

## Followers Actor

Default actor id: `bIYXeMcKISYGnHhBG`

### Input

```json
{
  "userNameList": ["elonmusk"],
  "userIdList": [],
  "maxFollowers": 1000,
  "maxFollowing": 1,
  "getFollowers": true,
  "getFollowing": false,
  "outputMode": "usernames"
}
```

### Expected output shape (examples)

Rows often contain one of these keys for username extraction:
- `username`
- `screenname`
- `userName`
- `handle`
- `value`

## Email Actor

Default actor id: `mSaHt2tt3Z7Fcwf0o`

### Input

```json
{
  "usernames": "user1\nuser2\nuser3",
  "max_results": 1000
}
```

### Expected output shape (examples)

- `screenname` or `username`
- `name`
- `email`

## Final normalized row

```json
{
  "targetUsername": "elonmusk",
  "username": "someuser",
  "sourceType": "followers",
  "collectedAt": "2026-02-28T11:00:00Z",
  "name": "Optional Name",
  "email": "optional@email.com"
}
```
