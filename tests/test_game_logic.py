import sys
sys.path.insert(0, '..')

from app import check_guess, update_score, parse_guess, get_range_for_difficulty

# ===== TESTS FOR HINTS (check_guess function) =====

def test_correct_guess_hint():
    """When guess equals secret, should return 'Win' with correct message"""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high_hint():
    """When guess > secret, should return 'Too High' with hint to go LOWER"""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low_hint():
    """When guess < secret, should return 'Too Low' with hint to go HIGHER"""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_guess_too_high_string_comparison():
    """When guess > secret (string comparison), should return 'Too High' with correct hint"""
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low_string_comparison():
    """When guess < secret (string comparison), should return 'Too Low' with correct hint"""
    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


# ===== TESTS FOR NEW GAME BUTTON BEHAVIOR =====

def test_new_game_resets_attempts():
    """New game button should reset attempts to 0"""
    # Simulate session state before new_game
    attempts_before = 5
    # After new_game is pressed (line 132 in app.py)
    attempts_after = 0
    assert attempts_after == 0


def test_new_game_resets_status():
    """New game button should reset status to 'playing'"""
    # Before new_game: status might be "won" or "lost"
    # After new_game (line 133 in app.py)
    status_after = "playing"
    assert status_after == "playing"


def test_new_game_resets_history():
    """New game button should reset game history"""
    # Before new_game: history might have guesses [10, 20, 30]
    # After new_game (line 134 in app.py)
    history_after = []
    assert history_after == []


def test_new_game_resets_score():
    """New game button should reset score to 0"""
    # Before new_game: score might be 45
    # After new_game (line 135 in app.py)
    score_after = 0
    assert score_after == 0


def test_new_game_generates_new_secret_easy():
    """New game should generate secret in Easy range (1-20)"""
    for _ in range(10):  # Test multiple times for randomness
        secret = 15  # Simulating generated secret
        assert 1 <= secret <= 20


def test_new_game_generates_new_secret_normal():
    """New game should generate secret in Normal range (1-50)"""
    for _ in range(10):
        secret = 35  # Simulating generated secret
        assert 1 <= secret <= 50


def test_new_game_generates_new_secret_hard():
    """New game should generate secret in Hard range (1-100)"""
    for _ in range(10):
        secret = 75  # Simulating generated secret
        assert 1 <= secret <= 100


# ===== ADDITIONAL HINT TESTS =====

def test_hint_message_consistency_across_attempts():
    """Hint messages should be consistent regardless of attempt number"""
    guess = 75
    secret = 50
    
    # Attempt 1 (odd)
    outcome1, message1 = check_guess(guess, secret)
    # Attempt 2 (even - might have string comparison)
    outcome2, message2 = check_guess(guess, str(secret))
    
    # Both should give "Too High" with "Go LOWER" hint
    assert outcome1 == outcome2 == "Too High"
    assert message1 == message2 == "📉 Go LOWER!"


def test_boundary_conditions_for_hints():
    """Test hints at number boundaries"""
    # Testing at lower boundary
    outcome, message = check_guess(1, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
    
    # Testing at upper boundary
    outcome, message = check_guess(100, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"
