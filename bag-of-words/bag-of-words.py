import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    output = []
    word_count_map = {}

    for word in tokens:
        if word in vocab:
            if word in word_count_map:
                word_count_map[word] += 1
            else:
                word_count_map[word] = 1

    for word in vocab:
        output.append(word_count_map.get(word, 0))

    return np.array(output, dtype=int)