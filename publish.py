"""Publishes an approved briefing to briefings/YYYY-MM-DD.md.
Runs only in the 'publish' job, after a human approved it in GitHub.
Copyright (c) 2026 Pavel Pravosud. MIT License."""
import datetime as dt
import os
import sys


def main():
    if os.getenv("AGENT_ENABLED", "true").lower() == "false":
        print("Kill switch is ON (AGENT_ENABLED=false). Nothing published.")
        return 0
    if not os.path.exists("briefing.md"):
        print("No approved draft found.")
        return 1
    today = dt.date.today().isoformat()
    os.makedirs("briefings", exist_ok=True)
    path = f"briefings/{today}.md"
    with open("briefing.md", encoding="utf-8") as src, open(path, "w", encoding="utf-8") as dst:
        dst.write(f"# AI briefing · {today}\n\n" + src.read())
    print("Published (after your approval): " + path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
