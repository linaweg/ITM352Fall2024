def determine_progress3(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio <= 0:
        return "Get going!"
    elif hits_spins_ratio >= 0.5 and hits < spins:
        return "You win!"
    elif hits_spins_ratio >= 0.25:
        return "Almost there!"
    elif hits_spins_ratio > 0:
        return "On your way!"
    
    return "Get going!"
# Test new function
def test_determine_progress3(progress_function):
    # Test case 1: spins = 0 returns “Get going!”
    assert progress_function(1, 0) == "Get going!", "Test case 1 failed"
    # Test case 2: hits_spins_ratio >= 0.5 and hits < spins
    assert progress_function(5, 10) == "You win!", "Test case 2 failed"
    # Test case 3: hits_spins_ratio >= 0.25
    assert progress_function(3, 10) == "Almost there!", "Test case 3 failed"
    # Test case 4: hits_spins_ratio > 0
    assert progress_function(1, 10) == "On your way!", "Test case 4 failed"
    # Test case 5: hits_spins_ratio <= 0
    assert progress_function(0, 10) == "Get going!", "Test case 5 failed"
    print("All test cases passed!")
#Run 
test_determine_progress3(determine_progress3)
