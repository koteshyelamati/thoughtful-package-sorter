def sort(width, height, length, mass):
    """
    Sort packages based on dimensions and mass criteria.
    
    Args:
        width (float): Width in cm
        height (float): Height in cm  
        length (float): Length in cm
        mass (float): Mass in kg
        
    Returns:
        str: Stack name where package should go
    """
    # Input validation
    if any(dim <= 0 for dim in [width, height, length]) or mass <= 0:
        raise ValueError("All dimensions and mass must be positive")
    
    # Calculate volume
    volume = width * height * length
    
    # Check if package is bulky
    is_bulky = (volume >= 1_000_000) or any(dim >= 150 for dim in [width, height, length])
    
    # Check if package is heavy  
    is_heavy = mass >= 20
    
    # Determine stack based on criteria
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Test cases
def run_tests():
    print("Running test cases...")
    
    # Test case 1: Standard package
    result = sort(10, 10, 10, 5)
    print(f"Test 1 - Standard (10x10x10, 5kg): {result}")
    assert result == "STANDARD", f"Expected STANDARD, got {result}"
    
    # Test case 2: Bulky by volume
    result = sort(100, 100, 100, 5) 
    print(f"Test 2 - Bulky by volume (100x100x100, 5kg): {result}")
    assert result == "SPECIAL", f"Expected SPECIAL, got {result}"
    
    # Test case 3: Bulky by dimension
    result = sort(150, 10, 10, 5)
    print(f"Test 3 - Bulky by dimension (150x10x10, 5kg): {result}")
    assert result == "SPECIAL", f"Expected SPECIAL, got {result}"
    
    # Test case 4: Heavy package
    result = sort(10, 10, 10, 20)
    print(f"Test 4 - Heavy (10x10x10, 20kg): {result}")
    assert result == "SPECIAL", f"Expected SPECIAL, got {result}"
    
    # Test case 5: Both heavy and bulky - REJECTED
    result = sort(150, 100, 100, 25)
    print(f"Test 5 - Heavy and bulky (150x100x100, 25kg): {result}")
    assert result == "REJECTED", f"Expected REJECTED, got {result}"
    
    # Test case 6: Edge case - exactly at bulky volume threshold
    result = sort(100, 100, 100, 10)  # volume = 1,000,000
    print(f"Test 6 - Edge volume (100x100x100, 10kg): {result}")
    assert result == "SPECIAL", f"Expected SPECIAL, got {result}"
    
    # Test case 7: Edge case - exactly at dimension threshold
    result = sort(150, 10, 10, 10)  # dimension = 150
    print(f"Test 7 - Edge dimension (150x10x10, 10kg): {result}")
    assert result == "SPECIAL", f"Expected SPECIAL, got {result}"
    
    # Test case 8: Edge case - exactly at mass threshold
    result = sort(10, 10, 10, 20)  # mass = 20
    print(f"Test 8 - Edge mass (10x10x10, 20kg): {result}")
    assert result == "SPECIAL", f"Expected SPECIAL, got {result}"
    
    # Test case 9: Just under thresholds
    result = sort(99.9, 99.9, 99.9, 19.9)
    print(f"Test 9 - Under thresholds (99.9x99.9x99.9, 19.9kg): {result}")
    assert result == "STANDARD", f"Expected STANDARD, got {result}"
    
    print("\nAll tests passed! ✅")

# Additional edge case testing
def test_edge_cases():
    print("\n" + "="*50)
    print("EDGE CASE TESTING")
    print("="*50)
    
    # Test with floating point numbers
    print(f"Float dimensions (10.5x10.5x10.5, 5.5kg): {sort(10.5, 10.5, 10.5, 5.5)}")
    print(f"Large package (200x50x50, 15kg): {sort(200, 50, 50, 15)}")
    print(f"Very heavy but small (5x5x5, 50kg): {sort(5, 5, 5, 50)}")
    
    # Test error handling
    try:
        sort(-10, 10, 10, 5)
    except ValueError as e:
        print(f"Error handling test passed: {e}")

if __name__ == "__main__":
    run_tests()
    test_edge_cases()