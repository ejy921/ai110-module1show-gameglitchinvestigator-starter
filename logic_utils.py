def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.

    fix: function was refactored out of `app.py` so the UI can
    request ranges without owning the logic. The UI uses the returned
    range to generate secrets and validate input.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str, low: int = 1, high: int = 100):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # Basic empty checks (keeps behavior consistent with original UI)
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    # Parse numeric input; accept floats by truncating to int like original
    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    # Enforce the allowed range provided by the caller (UI passes difficulty range)
    if value < low or value > high:
        return False, None, f"Please enter a number between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """Compare `guess` to `secret` and return an outcome string.

    Returns one of: "Win", "Too High", "Too Low".

    fix: function returns an outcome only (no UI message).
    The UI maps outcomes to messages via `get_hint_message()`. Used
    Agent Mode with Github Copilot to refactor out of `app.py`

    (original game intentionally sometimes stores `secret` as a
    string (the "glitch"). In that case numeric comparisons raise a
    TypeError)
    """
    try:
        if guess == secret:
            return "Win"

        if guess > secret:
            return "Too High"
        else:
            return "Too Low"
    except TypeError:
        # Fallback when comparing different types (e.g., int vs str).
        # We compare string forms to avoid crashing the UI; note this
        # produces lexicographic ordering ("9" > "10" is True).
        g = str(guess)
        if g == secret:
            return "Win"
        if g > secret:
            return "Too High"
        return "Too Low"


def get_hint_message(outcome: str):
    """Map an outcome to a user-facing hint message.

    fix: separating outcome from message makes unit testing simpler and
    fixes the inverted-hint bug by centralizing the mapping here with Agent Mode
    in Github Copilot.
    """
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too High":
        return "📉 Go LOWER!"
    if outcome == "Too Low":
        return "📈 Go HIGHER!"
    return ""


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number.

    Scoring rules mirror the original app's behavior and were
    kept intact during the refactor.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
