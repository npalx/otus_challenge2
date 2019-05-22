from statlib.lang_modules.lang_midule import LanguageModule

import ast
import logging
import re

from typing import List

FILTER_FILES_LIMIT = 500
PYTHON_FILE_EXTENTION = 'py'


class PythonModule(LanguageModule):
    def __init__(self, file_paths: List[str]):
        super().__init__()
        self.function_name_snake_case = True
        self.variable_name_snake_case = True
        self.class_name_snake_case = False

        self.python_files = self._get_filter_files(file_paths, extention=PYTHON_FILE_EXTENTION, limit=FILTER_FILES_LIMIT)
        self.syntax_trees = self._get_syntax_trees_in_repository()

    def _get_syntax_tree(self, file_path: str) -> ast.Module:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            try:
                syntax_tree = ast.parse(file_content)
            except SyntaxError as e:
                logging.warning(f'{e} {file_path}')
                syntax_tree = ast.Module()
        return syntax_tree

    def _get_syntax_trees_in_repository(self) -> List[ast.Module]:
        syntax_trees = [self._get_syntax_tree(file_path) for file_path in self.python_files]
        return syntax_trees

    def _nodes_iterator(self):
        for syntax_tree in self.syntax_trees:
            for node in ast.walk(syntax_tree):
                yield node

    def _get_function_names(self) -> List[str]:
        function_names = []
        for node in self._nodes_iterator():
            if isinstance(node, ast.FunctionDef) and not re.search(r'^__.*__$', node.name):
                function_names.append(node.name)
        return function_names

    def _get_variable_names(self) -> List[str]:
        variable_names = []
        for node in self._nodes_iterator():
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                variable_names.append(node.id)
        return variable_names

    def _get_class_names(self) -> List[str]:
        class_names = [node.name for node in self._nodes_iterator() if isinstance(node, ast.ClassDef)]
        return class_names
