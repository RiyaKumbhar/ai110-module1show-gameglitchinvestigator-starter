# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  Hints are swapped
  
  When I first ran the game, it looked normal, but it played wrong. A guess that was too high told me to go higher, so I could never narrow in on the number. The Hard difficulty was also easier than Normal, and New Game left me stuck on "Game over". I also noticed the attempt counter started at 1, so I lost an attempt before guessing.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Select Hard difficulty | Hard range should be bigger than Normal (fixed to 1 - 200) | 1 - 50 (smaller than Normal) | |
| Guess 62 (secret 50) | Should say "Go LOWER" | Said "Go HIGHER" (hints swapped) | |
| Click New Game after losing | Reset status, score, history and start a new game | Game stays stuck on "Game over" | |
| Guess on an even attempt | Compare numbers normally | Secret was converted to a string, so comparison was wrong | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  **What the AI suggested:** Claude noticed that on every even-numbered attempt `app.py` converted the secret to a string (`str(st.session_state.secret)`) before calling `check_guess`. It suggested always passing the secret as an integer and removing that branch.
  **Why it was correct:** comparing an int guess with a string secret raises a `TypeError`, and the fallback then compared strings, so "9" > "10" and the hints were wrong on every other guess. The secret is always a number, so there was no reason to convert it.
  **How I verified it:** I checked in `app.py` that `check_guess` now gets `st.session_state.secret` directly, and the pytest tests for Too High, Too Low and Win all pass with integer inputs.
  
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

  **What the AI suggested:** Claude's code review pointed out that the "Developer Debug Info" expander exposes the secret number (line 115 in the original file), and that it should be removed in a finished game. It also flagged duplicate logic between `app.py` and `logic_utils.py`.

  **Why I did not accept it as written:** this project is a debugging exercise, and I needed to see the secret, attempts and history to confirm each fix, so removing the expander would have made my verification harder. It is out of scope for this assignment, so I kept it and would remove it before shipping a real game. I did accept the duplicate-logic point and moved the functions into `logic_utils.py`.

  **How I verified my version:** I kept the debug panel and used it to check that the secret stays an integer, the attempts and history reset on New Game, and the secret stays inside the selected difficulty range.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I treated a bug as fixed when the code no longer had the faulty behaviour and a pytest case covering it passed. I also read each changed line in the diff to make sure the fix matched the bug.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran `pytest -v` and all 5 tests passed:
  - `test_winning_guess`: guess 50, secret 50 gives "Win".
  - `test_guess_too_high`: guess 60, secret 50 gives "Too High".
  - `test_guess_too_low`: guess 40, secret 50 gives "Too Low".
  - `test_hint_direction`: guess 60, secret 50 says "LOWER". This targets the swapped-hints bug.
  - `test_hard_range_harder_than_normal`: Hard's maximum is higher than Normal's. This targets the Hard range bug.
  The starter tests failed at first because `check_guess` returns an (outcome, message) pair and they compared it to a plain string, so I updated them to unpack the pair. The tests also failed to import `logic_utils` when run from the parent folder, which I fixed with a `conftest.py` in `tests/`.

- Did AI help you design or understand any tests? How?
  Yes. Claude Code wrote the tests so each one targets a single fixed bug, and explained why the starter tests needed updating. I checked that each test would have failed on the original buggy code, for example the original `check_guess` returned "Go HIGHER" for a too-high guess.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit re-runs the whole script from top to bottom every time you click a button or type something. Normal variables reset on each rerun, so anything the game must remember, like the secret number, attempts and score, is kept in `st.session_state`, which survives reruns. Many of my bugs came from this: New Game didn't reset every session value, and changing difficulty kept the old secret.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Writing a small test for each bug right after fixing it, so I know it stays fixed.

- What is one thing you would do differently next time you work with AI on a coding task?
  I would read and understand the code first and ask the AI to explain the bugs before it changes anything, instead of letting it fix everything at once.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  AI-generated code can look polished and still be full of bugs, so it needs testing and review like any other code. The game claimed to be "production-ready" and was clearly not.
