# Fallback: working without a codespace

Use this if your codespace hasn't worked after 15 minutes, or if the Wi-Fi is too weak. You'll do the same work, just on your own computer.

## Option A: Python on your computer (preferred fallback)

1. Check Python is installed. In a terminal (Windows: **Command Prompt**; Mac: **Terminal**):

   ```
   python --version
   ```

   On Windows, try `py --version` if `python` isn't found. You need Python 3.10 or later. If it's missing, install it from python.org (tick **Add Python to PATH** on Windows).

2. On this repository's GitHub page, click **Code → Download ZIP**, and unzip it.

3. In the terminal, go into the unzipped folder and install pytest:

   ```
   cd prompt-to-product-starter-main
   python -m pip install -r requirements.txt
   ```

4. Run the tests:

   ```
   python -m pytest
   ```

   You should see `3 passed, 1 skipped`.

5. Edit the files in any editor (VS Code, IDLE, Notepad++).

## Saving your work without git

Your files live in the unzipped folder on the pair's computer; bring that computer to every session. To make save points, copy the whole folder at the end of each sprint (for example `project-sprint-1`, `project-sprint-2`). It's a crude version of a commit, but it lets you go back.

To share work with your partner outside workshop time, zip the folder and send it (see the end of [PUBLISH.md](PUBLISH.md)), or move to a codespace as soon as one works.

## Option B: use your partner's computer

If only one computer in your pair works, that's the pair's computer, in a codespace or locally. The navigator prompts, challenges and keeps the log on their own device. This is how the roles work anyway.
