def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    if len(sentences) == 0:
        return {}
    
    word_dict = {}
    for sentence in sentences:
        for word in sentence:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

    return word_dict