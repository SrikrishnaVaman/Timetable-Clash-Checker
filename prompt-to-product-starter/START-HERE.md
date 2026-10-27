# Start here

You are in a **codespace**: a complete coding environment running in your browser, with Python, pytest and git already installed. Nothing to install on your computer.

Follow these steps together with the facilitator. **Don't move on until each step works.** The same steps are in the Journey slides ("Set up 1–4").

## 0. The pair's computer

- Your pair works in **one** codespace, on **one** computer: **the pair's computer**. It's signed in to one partner's GitHub account.
- Whoever is **driving** sits at the pair's computer. When you swap roles, **swap seats, not computers**.
- The **navigator** uses their own computer for the AI tool and for reading.
- **Both of you need a free GitHub account** (create one at github.com). The partner without the codespace can create theirs during setup; it's needed when we publish and share.

## 1. Find your way around

- **Explorer** (left, top icon): your files.
- **Editor** (centre): this file is open in it.
- **Terminal** (bottom): if it isn't open, press **Ctrl + `** (the key above Tab), or use the menu ☰ → **Terminal → New Terminal**.

## 2. Check that everything works

In the terminal, type:

```
pytest
```

You should see:

```
3 passed, 1 skipped
```

✅ **That's the green light.** Put a ✓ in your pair's row of the shared sheet. Not seeing it? Tick "help needed" in the sheet.

`pytest` runs every test (every function whose name starts with `test_`) and reports how many passed, failed or were skipped.

## 3. Commit: your save point

A **commit** is a save point you can always go back to.

1. Click the **Source Control** icon on the left (it looks like a branching line).
2. Type a short message, for example `setup works`.
3. Click **Commit** (✓). If asked whether to stage all changes, choose **Yes** or **Always**.

Your commit is saved inside the codespace. You'll also see a **Publish Branch** button: **leave it for now**. We publish and share together, once, when the facilitator calls it (see [PUBLISH.md](PUBLISH.md)).

**The rule for the whole workshop:** commit at the end of every sprint, before every swap and before every break.

## 4. Your AI tool

**Both of you** sign in to an AI tool on your own computer, so whoever is navigating can prompt straight away after a swap. Use any tool you like:

- **GitHub Copilot** in the codespace, if your account has it (the chat icon at the top or side).
- Any AI chat in a browser tab (copy code in and out).

Whichever you use, the ownership rule applies: *if you cannot explain a piece of code you submitted, you are not done with it.* That goes for **both** of you.

## 5. Swapping roles (every sprint)

1. The driver **commits**.
2. **30-second handover:** the driver says what they were doing and what comes next.
3. Swap seats. The new navigator opens their AI tool.

## 6. Coming back to the workshop

On the pair's computer:

1. Go to **github.com/codespaces** and click your codespace to reopen it. Don't create a new one from the template: that would start again from an empty project.
2. In Source Control, click **Sync Changes** first, to bring in anything either of you did outside workshop time.

## Stuck for more than 15 minutes?

Switch to the fallback in [LOCAL-SETUP.md](LOCAL-SETUP.md) so you can keep working, and tell the facilitator.

## What's next

- The warm-up is in the `warmup/` folder: start with `warmup/hard_mode.py`.
- After the warm-up, read [TOPICS.md](TOPICS.md) and claim a topic in the shared sheet.
- Then follow the Journey slides, sprint by sprint, starting with sprint 1: write `spec.md`.
