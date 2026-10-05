# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [x] Explain what fixes you applied.

### Fixes applied

- **Swapped hints:** `check_guess` told players to go higher when the guess was too high. The hints now point the right way.
- **Secret turned into a string:** on even attempts the secret was converted to a string, which broke the comparison. It is now always compared as a number.
- **Hard range:** Hard was 1-50, easier than Normal. It is now 1-200.
- **New Game:** it now resets status, score and history, and picks the secret from the selected difficulty range.
- **Attempts and banner:** attempts start at 0, and the info banner shows the real range instead of always "1 and 100".
- **Scoring:** a win scores `100 - 10 * attempts` (minimum 10), and every wrong guess costs 5 points.
- **Difficulty change:** switching difficulty now starts a fresh game.
- **Refactor and tests:** the game logic moved from `app.py` into `logic_utils.py`, and `tests/test_game_logic.py` now has 5 passing pytest tests, including ones for hint direction and the Hard range.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run `streamlit run app.py`. The sidebar shows the difficulty (Easy 1-20, Normal 1-100, Hard 1-200), the range and the attempts allowed, and the banner shows the same range.
2. Type a guess and click Submit Guess. If it is too high the hint says "Go LOWER", and if it is too low it says "Go HIGHER". Each wrong guess costs 5 points and uses one attempt.
3. Keep guessing using the hints. A correct guess ends the game with balloons, the secret number, and your score (`100 - 10 * attempts`, minimum 10 points).
4. If you run out of attempts, the game shows "Out of attempts!" with the secret number and your score. Click New Game to reset the status, score and history and get a new secret in the current difficulty range.
5. Change the difficulty in the sidebar at any time to start a fresh game with the new range. Run `pytest` to check the game logic (5 tests pass).


## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
