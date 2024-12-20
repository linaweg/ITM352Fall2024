def determine_progress_with_ranges(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    # List tuples with (lower_bound, upper_bound, message)
    progress_ranges = [
        (0, 0, "Get going!"),
        (0.5, float('inf'), "You win!"),       # Infinite upper bound for ratios >= 0.5
        (0.25, 0.5, "Almost there!"),          # Ratios between 0.25 and 0.5
        (0, 0.25, "On your way!")              # Ratios between 0 and 0.25
    ]

    # Iterate over ranges and return the corresponding message
    for lower_bound, upper_bound, message in progress_ranges:
        if lower_bound <= hits_spins_ratio < upper_bound:
            return message
    
    return "Get going!"  # Fallback case, although it shouldn't be
