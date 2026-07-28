import sys
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import apify_twitter_actors as runner


class FakeResponse:
    status_code = 200
    text = ""

    @staticmethod
    def json():
        return [{"username": "example"}]


class FakeRequests:
    def __init__(self):
        self.calls = []

    def post(self, url, **kwargs):
        self.calls.append((url, kwargs))
        return FakeResponse()


class XquikInputTests(unittest.TestCase):
    def test_post_plan_is_bounded(self):
        payload = runner.build_xquik_post_input("product launch", 25)

        self.assertEqual(payload["mode"], "search")
        self.assertEqual(payload["searchTerms"], ["product launch"])
        self.assertEqual(payload["maxItems"], 25)
        self.assertEqual(payload["maxItemsPerTarget"], 25)

    def test_audience_plan_preserves_source_metadata(self):
        payload = runner.build_xquik_audience_input(
            "https://x.com/example",
            "followers",
            40,
        )

        self.assertEqual(payload["twitterHandles"], ["example"])
        self.assertEqual(payload["relation"], "followers")
        self.assertTrue(payload["includeTargetMetadata"])
        self.assertEqual(payload["dedupeMode"], "merge")
        self.assertEqual(payload["maxItems"], 40)
        self.assertEqual(payload["maxItemsPerTarget"], 40)

    def test_actor_token_uses_authorization_header(self):
        fake_requests = FakeRequests()
        original_requests = runner.requests
        runner.requests = fake_requests
        self.addCleanup(setattr, runner, "requests", original_requests)

        rows = runner.run_actor_sync(
            runner.XQUIK_TWEET_ACTOR,
            "secret-token",
            {"mode": "search"},
        )

        self.assertEqual(rows, [{"username": "example"}])
        _, kwargs = fake_requests.calls[0]
        self.assertEqual(
            kwargs["headers"],
            {"Authorization": "Bearer secret-token"},
        )
        self.assertNotIn("token", kwargs["params"])

    def test_plan_does_not_require_a_token(self):
        payload = runner.build_xquik_post_input("launch", 10)

        plan = runner.run_xquik(
            runner.XQUIK_TWEET_ACTOR,
            payload,
            explicit_token=None,
            execute=False,
        )

        self.assertFalse(plan["execute"])
        self.assertEqual(plan["actorId"], runner.XQUIK_TWEET_ACTOR)
        self.assertEqual(plan["input"], payload)


if __name__ == "__main__":
    unittest.main()
