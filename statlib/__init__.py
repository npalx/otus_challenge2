from statlib.downloaders import Github
from statlib.lang_modules import PythonModule
from statlib.analyse import get_top_verbs, get_top_nouns
from statlib.output import print_to_stdout, save_to_json, save_to_csv

language_modules = {
    'python': PythonModule,
}

downloaders = {
    'github': Github,
}

analysers = {
    'verbs': get_top_verbs,
    'nouns': get_top_nouns,
}

outputs = {
    'stdout': print_to_stdout,
    'csv': save_to_csv,
    'json': save_to_json,
}
