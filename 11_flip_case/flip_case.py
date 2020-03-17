def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    flipped_case = ""
    for letter in phrase:
        """How do I make long lines more readable? """
        flipped_case = flipped_case + letter.swapcase() if letter.casefold() == to_swap.casefold() else flipped_case + letter
    
    return flipped_case

