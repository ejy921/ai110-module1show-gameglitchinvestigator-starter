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

 - [x] Describe the game's purpose. - A simple Streamlit number-guessing game where the player guesses a secret number within a difficulty-specific range.
 - [x] Detail which bugs you found. - Hints were inverted (suggesting the wrong direction), the secret could be reset or generated inconsistently across reruns, and input wasn't validated against the displayed range.
 - [x] Explain what fixes you applied. - Refactored logic into `logic_utils.py`, fixed the hint/message mapping, added input range validation, persisted the secret in `st.session_state`, and added pytest test coverage.

## 📸 Demo

<img src="demo1.png" alt="Demo 1" width="300">
<img src="demo2.png" alt="Demo 2" width="300">
<img src="demo3.png" alt="Demo 3" width="300">
<img src="demo4.png" alt="Demo 4" width="300">

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
