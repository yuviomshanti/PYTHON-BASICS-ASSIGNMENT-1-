# QUESTION 9

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed

    if speeding <= 60:
        return "No Challan"
    elif 61 <= speeding <= 80:
        return "Small Challan"
    else:
        return "Heavy Challan"

# Examples
print(caught_speeding(81, True))   # Output: "Small Challan"
print(caught_speeding(81, False))  # Output: "Heavy Challan"

