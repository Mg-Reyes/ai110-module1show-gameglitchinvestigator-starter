# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

This game should randomly select a number and have the player try to guess it by inputting a number from 1 to 100. If the guess is higher than the number then a hint saying "go LOWER!" should apper. On the other hand if the guess is too low a hint saying "go HIGHER!" should appear.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1) The first bug that is the most obvious is the wrong hints. The hints are reversed, for exmaple if the secret number is 8 and you;
- Input anything < 8, the hint will say "go LOWER!"
- Input anything > 8, the hint will say "go HIGHER!"

2) The second bug that I encountered was, the new game button not restarting the game after your first win. If you correctly guess on your first try, it will tell you you won but when you click the "new game" button it outputs a message saying "You already won. Start a new game to play again." and doesn't actually start the next game.
notes: 
- It does work if you haven't correctly guessed the first time
- A new number is chosen and the attempts are reset, but the score isn't reset and the game doesn't allow any input.

3) The third bug I found was with the attemps, it says you are allowed 8 attemps, but the game starts you off with one attemp and only accepts 7 guesses. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
