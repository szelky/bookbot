def get_num_words(text):
    """
    Counts the number of words in a given text.
    Args:
        text (str): The text to count words in.
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())


def get_num_characters(text):
    """
    Counts the number of characters in a given text.
    Args:
        text (str): The text to count characters in.
    Returns:
        int: The number of characters in the text.
    """
    character_dict = {}
    for char in text:
        char = char.lower()
        # Count the character
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def sorted_characters(character_dict):
    """
    Sorts the characters in a dictionary by their frequency.
    Args:
        character_dict (dict): The dictionary of characters and their frequencies.
    Returns:
        list: A sorted list of dictionaries {"char": char, "count": count} sorted by count in descending order.
    """
    sorted_list = sorted(character_dict.items(), key=lambda x: x[1], reverse=True)
    return [{"char": char, "count": count} for char, count in sorted_list]
