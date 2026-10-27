# Publish and share (once, all together)

Once everyone is set up, at a point the facilitator calls, each pair publishes its project to a **private** GitHub repository and adds the partner as a collaborator, together on the projector. It doesn't matter how far your project has got. From then on, both of you can reach the project from anywhere with a browser.

**Commit to save. Sync to share.**

## 1. Publish (on the pair's computer)

1. Click the **Source Control** icon on the left (it looks like a branching line).
2. Make sure everything is committed: type a message and click **Commit** (✓).
3. Click **Publish Branch** and choose **Publish to GitHub private repository**. Name it after your topic, for example `k1-study-rooms`.
4. When it finishes, click **Open on GitHub**, and paste the repository's address into your pair's row of the shared sheet.

## 2. Share

1. On the repository page: **Settings → Collaborators → Add people**. Add your partner's GitHub username, and the facilitator's if asked.
2. Partner: accept the invitation. It arrives by email and in your GitHub notifications (the bell icon).

## 3. Working outside workshop time

| What you're doing | Easiest way |
|---|---|
| Writing or editing text: `spec.md`, `HOW-IT-WORKS.md`, `ai-log.md`, your response in `REVIEW.md` | Open the file on **github.com**, click the **pencil icon**, edit, then **Commit changes**. No codespace needed. |
| Running or changing code | **Your own codespace** on the shared repository: on the repository page, **Code → Codespaces → Create codespace on main**. |

### The one rule: sync when you start, sync when you stop

- **Before you start**, click **Sync Changes** in Source Control to get your partner's latest work.
- **When you stop**, **Commit**, then **Sync Changes** to share yours.
- **Back in class**, the pair's computer syncs first, so everything done outside the workshop is there.

(Editing on github.com counts as committing and syncing at once. If you then switch to a codespace, sync it first.)

### Avoid editing the same file at the same time

Split the work **by file**: for example, one of you writes in `HOW-IT-WORKS.md` while the other changes the code and tests. If Sync reports a **conflict**, stop, don't force anything, and tell the facilitator at the start of the next session.

### Working together from different places

**Live Share** (optional) lets you both edit the same codespace at the same time, like remote pair programming. In the pair's codespace: **Extensions** (the squares icon) → install **Live Share** → **Share**, then send the link to your partner. You both need to be online at the same time.

## No GitHub account for one partner?

The account holder makes a zip of the project in the terminal:

```
python -m zipfile -c my-project.zip src tests warmup spec.md HOW-IT-WORKS.md ai-log.md REVIEW.md OWNERSHIP.md
```

Then right-click `my-project.zip` in Explorer, choose **Download…**, and share it. The other partner writes text in any document, and it's pasted in at the next session. It's clumsier, so a free GitHub account is better.

## After the workshop

Your private repository stays on GitHub with its full history. Make it public if you want it in your portfolio: **Settings → General → Danger Zone → Change visibility**. Codespaces stop when idle, and GitHub deletes unused ones after a while; delete yours at **github.com/codespaces** when you're done to free your allowance.
