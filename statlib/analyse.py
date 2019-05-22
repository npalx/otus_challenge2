from nltk import pos_tag
from typing import List, Tuple, Callable
from collections import Counter


def _get_verbs(words: List[str]) -> List[str]:
    tagged_words = pos_tag(words)
    verbs = [word for word, tag in tagged_words if tag.startswith('VB')]
    return verbs


def _get_nouns(words: List[str]) -> List[str]:
    tagged_words = pos_tag(words)
    nouns = [word for word, tag in tagged_words if tag.startswith('NN')]
    return nouns


def _get_top_words(get_part_of_speech_function: Callable, words: List[str], limit: int) -> List[Tuple[str, int]]:
    filtered_words = get_part_of_speech_function(words)
    counted_words = Counter(filtered_words).most_common(limit)
    return counted_words


def get_top_verbs(words: List[str], limit: int) -> List[Tuple[str, int]]:
    return _get_top_words(_get_verbs, words, limit)


def get_top_nouns(words: List[str], limit: int) -> List[Tuple[str, int]]:
    return _get_top_words(_get_nouns, words, limit)
