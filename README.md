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

This game should randomly select a number and have the player try to guess it by inputting a number from 1 to 100. If the guess is higher than the number then a hint saying "go LOWER!" should apper. On the other hand if the guess is too low a hint saying "go HIGHER!" should appear.

- [ ] Detail which bugs you found.

1) The first bug that is the most obvious is the wrong hints. The hints are reversed, for exmaple if the secret number is 8 and you;
- Input anything < 8, the hint will say "go LOWER!"
- Input anything > 8, the hint will say "go HIGHER!"

2) The second bug that I encountered was, the new game button not restarting the game after your first win. If you correctly guess on your first try, it will tell you you won but when you click the "new game" button it outputs a message saying "You already won. Start a new game to play again." and doesn't actually start the next game.
notes: 
- It does work if you haven't correctly guessed the first time
- A new number is chosen and the attempts are reset, but the score isn't reset and the game doesn't allow any input.

3) The third bug I found was with the attemps, it says you are allowed 8 attemps, but the game starts you off with one attemp and only accepts 7 guesses. 

- [ ] Explain what fixes you applied.

None yet

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
