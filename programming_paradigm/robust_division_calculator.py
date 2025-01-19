def safe_divide(numerator, denominator):
    """
    Safely performs division, handling errors like division by zero
    and non-numeric inputs.
    :param numerator: The numerator as a string.
    :param denominator: The denominator as a string.
    :return: The result or an error message.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Perform division
        if denom == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / denom:.1f}"

    except ValueError:
        return "Error: Please enter numeric values only."
