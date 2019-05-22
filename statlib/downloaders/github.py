from .downloader import Downloader

import re
import logging

from typing import List
from git import Repo
from git.exc import GitCommandError


class Github(Downloader):
    def __init__(self, repository_url: str):
        self.repository_url = repository_url
        self.repository_name = self._get_repository_name()

    def _get_repository_name(self) -> str:
        search_result = re.search(r'github\.com/[\w\-]+/([\w\-.]+)', self.repository_url)
        if search_result:
            repository_name = search_result[1]
        else:
            raise AttributeError
        return repository_name

    def download(self) -> List[str]:
        try:
            Repo.clone_from(self.repository_url, self.repository_name)
        except GitCommandError as e:
            logging.error(e)

        return self.get_file_paths(self.repository_name)
