#!/usr/bin/env python3
"""Check whether OPENAI_API_KEY can authenticate with the OpenAI API."""

from __future__ import annotations

import hashlib
import json
import os
import sys
import urllib.error
import urllib.request


API_URL = "https://api.openai.com/v1/models"


def fingerprint(secret: str) -> str:
    return hashlib.sha256(secret.encode("utf-8")).hexdigest()[:12]


def main() -> int:
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        print("OPENAI_API_KEY is not set.")
        print("Set it in this shell, then rerun:")
        print('$env:OPENAI_API_KEY = "sk-..."')
        return 2

    request = urllib.request.Request(
        API_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="GET",
    )

    print(f"Checking key fingerprint sha256:{fingerprint(api_key)}...")

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(f"OpenAI API returned HTTP {exc.code}.")
        try:
            error = json.loads(body).get("error", {})
            message = error.get("message") or body
            print(f"Message: {message}")
        except json.JSONDecodeError:
            print(body[:1000])
        return 1
    except urllib.error.URLError as exc:
        print(f"Network error: {exc.reason}")
        return 1
    except TimeoutError:
        print("Request timed out.")
        return 1

    models = payload.get("data", [])
    print(f"Authentication succeeded. Visible models: {len(models)}")
    for model in models[:10]:
        model_id = model.get("id", "<unknown>")
        print(f"- {model_id}")
    if len(models) > 10:
        print(f"... and {len(models) - 10} more")
    return 0


if __name__ == "__main__":
    sys.exit(main())
