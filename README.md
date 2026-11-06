# AI Morning Briefing

**Your first AI employee, running free while you sleep.**
A small, read-only AI agent that reads the AI news every weekday morning and sends you a 3-minute briefing written by Claude. It works anywhere GitHub works, including Europe.

> Built in the video *"Your First AI Employee: Muse vs Dots vs Claude"* by **Pavel Pravosud, The AI Person**.

## What it does

| Step | What happens |
| --- | --- |
| 1. Wakes up | GitHub Actions starts it at 06:00 UTC, Monday to Friday |
| 2. Reads | The sources in `sources.txt` (RSS feeds, Hacker News, GitHub releases). Read-only, no logins |
| 3. Thinks | Claude turns the fresh items into a short briefing, following `prompt.md` |
| 4. Reports | Posts the briefing as an issue in your copy of this repo. GitHub e-mails it to you |

## Set it up in 5 steps (about 10 minutes, no coding)

1. **Copy the repo:** click **Use this template** (or **Fork**) at the top of this page.
2. **Add your Claude API key:** in your copy go to **Settings → Secrets and variables → Actions → New repository secret**. Name: `ANTHROPIC_API_KEY`. Value: your key from [console.anthropic.com](https://console.anthropic.com).
3. **Pick your sources:** edit `sources.txt`. One line per source: `Name | URL`. For GitHub releases write `github:owner/repo`.
4. **Pick your time:** in `.github/workflows/briefing.yml` change the `cron` line. `0 6 * * 1-5` means 06:00 UTC on weekdays.
5. **Test it now:** go to **Actions → AI Morning Briefing → Run workflow**. Your first briefing appears under **Issues** in about a minute. Turn on *Watch → All activity* to get it by e-mail.

## Cost

GitHub Actions is free for this. The only cost is Claude: with the default `claude-sonnet-5-5` a daily briefing reads roughly 5-20K tokens, which is about **1-5 cents a day**.
Want deeper analysis? Add a repository **variable** `CLAUDE_MODEL` = `claude-opus-5-5` (about twice the price).

## Safety by design

- **Read-only first:** the agent only reads public feeds. The draft job can post one issue; nothing else can write without your approval (see v2 above).
- **Secrets stay secret:** your key lives in GitHub Secrets, never in the code or the prompt.
- **Prompt-injection guard:** feed items are passed as data, and `prompt.md` tells Claude to ignore any instructions inside them.

## v2: give it hands, safely (Episode 2)

Version 2 turns the agent into a **Level 1 agent**: it drafts, you approve, and only then does it act.
Its one action is to publish the approved briefing to `briefings/YYYY-MM-DD.md` in your repo, so you build a public archive.

| Control | How it works here | Where you set it |
| --- | --- | --- |
| **Approve button** | The `publish` job waits for you. GitHub e-mails you; you press **Review deployments → Approve** | **Settings → Environments → New environment** `publish` **→ Required reviewers** = you **→ Save protection rules** |
| **Least privilege** | Nothing is allowed by default. The draft job can only read the repo and post an issue. Only the publish job can write, and only after approval | Already in `.github/workflows/briefing.yml` |
| **Kill switch** | Stops every job and the script itself | **Settings → Secrets and variables → Actions → Variables →** `AGENT_ENABLED` = `false` (or **Actions → AI Morning Briefing → ... → Disable workflow**) |
| **Spending cap** | The script estimates the cost before calling Claude and trims or stops if a run would cost more than the cap | Variable `MAX_COST_USD` (default `0.05`). Also set a monthly spend limit in the Anthropic Console |

**Set up v2 in 3 extra minutes:** create the `publish` environment with yourself as required reviewer, run the workflow once, then open the waiting run and press **Approve**.

Note: required reviewers work on **public** repositories on every GitHub plan. For a private copy you need GitHub Pro or Team.

## Customise

- Change the tone, length or format: edit `prompt.md`.
- Look back further: set a variable `BRIEFING_HOURS` (default 24).
- Try it locally without a key: `python briefing.py --dry-run`

## Free checklist

[Hire your first AI employee: one-page checklist (PDF)](docs/Hire_Your_First_AI_Employee_Checklist.pdf)

## Licence

MIT. Copyright (c) 2026 Pavel Pravosud.
