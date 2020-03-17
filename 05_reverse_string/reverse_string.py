def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    rebuild = ""

    if len(phrase) == 0:
        return ""

    rebuild = reverse_string(phrase[1: len(phrase)])
    
    return rebuild+phrase[0]
