def determine_progress_custom(hits, spins, custom_messages):
    if spins == 0:
        return custom_messages.get("get_going", "Get going!")
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio <= 0:
        return custom_messages.get("get_going", "Get going!")
    elif hits_spins_ratio >= 0.5 and hits < spins:
        return custom_messages.get("you_win", "You win!")
    elif hits_spins_ratio >= 0.25:
        return custom_messages.get("almost_there", "Almost there!")
    elif hits_spins_ratio > 0:
        return custom_messages.get("on_your_way", "On your way!")
    
    return custom_messages.get("get_going", "Get going!")

# Example custom messages dictionary
custom_messages = {
    "get_going": "Start spinning!",
    "you_win": "Victory!",
    "almost_there": "Nearly done!",
    "on_your_way": "Keep going!"
}

# Testing the new customizable function
def test_determine_progress_custom(progress_function):
    # Test case 1: spins = 0 returns custom message “Start spinning!”
    assert progress_function(1, 0, custom_messages) == "Start spinning!", "Test case 1 failed"
    # Test case 2: hits_spins_ratio >= 0.5 and hits < spins
    assert progress_function(5, 10, custom_messages) == "Victory!", "Test case 2 failed"
    # Test case 3: hits_spins_ratio >= 0.25
    assert progress_function(3, 10, custom_messages) == "Nearly done!", "Test case 3 failed"
    # Test case 4: hits_spins_ratio > 0
    assert progress_function(1, 10, custom_messages) == "Keep going!", "Test case 4 failed"
    # Test case 5: hits_spins_ratio <= 0
    assert progress_function(0, 10, custom_messages) == "Start spinning!", "Test case 5 failed"
    print("All test cases passed!")

# Run tests
test_determine_progress_custom(determine_progress_custom)
