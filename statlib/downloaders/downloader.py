import os
import logging

from typing import List


class Downloader:
    def get_file_paths(self, root_path: str) -> List[str]:
        file_paths = []

        if not os.path.exists(root_path):
            logging.info(f'{root_path} not found.')

        for dir_name, _, file_names in os.walk(root_path, topdown=True):
            for file_name in file_names:
                file_paths.append(os.path.join(dir_name, file_name))

        return file_paths

    def download(self) -> List[str]:
        raise NotImplementedError
