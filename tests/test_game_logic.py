from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_hint_messages():
    # fix: ensure the UI hint mapping matches the intended messages with
    # Github Copilot
    from logic_utils import get_hint_message

    assert get_hint_message("Win") == "🎉 Correct!"
    assert get_hint_message("Too High") == "📉 Go LOWER!"
    assert get_hint_message("Too Low") == "📈 Go HIGHER!"


def test_regression_string_secret_hint():
    # fix: makes sure that when the secret is stored as a string (the UI's
    # intentional glitch) the numeric guesses still produce the
    # correct outcome and hint mapping. This would have failed before
    # the hint-mapping fix (inverted hint text). Used Agent Mode with Github Copilot
    from logic_utils import check_guess, get_hint_message

    outcome = check_guess(60, "50")
    assert outcome == "Too High"
    assert get_hint_message(outcome) == "📉 Go LOWER!"
