import re

from itertools import chain
from typing import List, Callable


class LanguageModule:
    def __init__(self):
        self.function_name_snake_case = True
        self.variable_name_snake_case = True
        self.class_name_snake_case = True

    def _get_filter_files(self, file_paths: List[str], extention: str, limit: int) -> List[str]:
        filtered_files = [file_path for file_path in file_paths if file_path.endswith(f'.{extention}')]
        return filtered_files[:limit]

    def _get_splitted_names(self, names: List[str], snake_case: bool) -> List[str]:
        if snake_case:
            splitted_names = (name.split('_') for name in names)
        else:
            splitted_names = (re.findall(r'[A-Z][a-z\d]+', name) for name in names)

        flatted_names_list = chain.from_iterable(splitted_names)
        words = filter(None, flatted_names_list)
        lower_words = [word.lower() for word in words]
        return lower_words

    def _get_words_from_names(self, get_names_function: Callable, snake_case: bool = True) -> List[str]:
        names = get_names_function()
        words = self._get_splitted_names(names, snake_case)
        return words

    def get_words_from_function_names(self) -> List[str]:
        words = self._get_words_from_names(self._get_function_names, snake_case=self.function_name_snake_case)
        return words

    def get_words_from_variable_names(self) -> List[str]:
        words = self._get_words_from_names(self._get_variable_names, snake_case=self.variable_name_snake_case)
        return words

    def get_words_from_class_names(self) -> List[str]:
        words = self._get_words_from_names(self._get_class_names, snake_case=self.class_name_snake_case)
        return words

    def get_words_from(self, code_element: str) -> List[str]:
        get_words_function = {
            'function': self.get_words_from_function_names,
            'variable': self.get_words_from_variable_names,
            'class': self.get_words_from_class_names,
        }
        return get_words_function[code_element]()

    def _get_function_names(self) -> List[str]:
        raise NotImplementedError

    def _get_variable_names(self) -> List[str]:
        raise NotImplementedError

    def _get_class_names(self) -> List[str]:
        raise NotImplementedError
