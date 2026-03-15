# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

Firstly, the game allows me to put in numbers smaller than 1 and larger than 100. I expected it to at least print a message if I exceeded these boundaries.
Then it also gives me the wrong hint - it tells me to go higher when the answer is actually lower.
Thirdly, it doesn't let me play a new game after I won - it gives the message that I "already won". I expected it to let me play a new game regardless of whether I won or not.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Copilot with the GPT-5 mini model. Copilot correctly changed the game logic so that it would give the correct hint that aligns with the answer. I verified the result by running the game a few more times, and later writing tests to verify. Not too misleading, but during one the the fixes the AI changed 1 and 100 values to low and high, but didn't apply that to every intance, which was quite misleading. I had to check manually of each instance to make sure, and had to add the changes myself as I figured that was quicker than asing the AI to do it again, and then having to verify it again.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed when I could reproduce the failure, write a focused unit test that captured the incorrect behavior, make a minimal code change, and then see the test pass consistently. For the inverted-hint bug I added `test_hint_messages()` to assert that `get_hint_message("Too High")` returns "📉 Go LOWER!" and `get_hint_message("Too Low")` returns "📈 Go HIGHER!". I also added a regression test that simulates the UI glitch by making the secret a string (for example, `"50"`) and confirmed a numeric guess of `60` produced the `"Too High"` outcome and the correct mapped hint. AI suggested refactors and approaches to testing, but I wrote and verified the tests myself to be sure the fixes actually worked.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

I learned that Streamlit reruns the entire script on every interaction, so any top-level value will be recomputed on each rerun unless it's stored in `st.session_state`. The original app could appear to change the secret because different code paths or reruns regenerated it or used inconsistent ranges. Streamlit's `session_state` is the correct place to persist values across reruns; initializing `st.session_state.secret` only when it doesn't exist prevents accidental resets. The change that stabilized the secret was making sure we set the secret inside `if "secret" not in st.session_state:` and using the difficulty `low`/`high` range consistently for new games so the secret isn't overwritten unexpectedly.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I will keep is extracting pure logic out of the UI so it can be unit-tested, and writing small, focused tests for each bug before and after fixes. Next time I work with AI on code I'll ask for smaller, reviewable edits and back them with tests and quick manual checks — AI speeds up iteration but reliable fixes still need human review and automated tests.

```
