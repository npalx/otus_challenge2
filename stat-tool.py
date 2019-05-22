#!/usr/bin/python
import statlib
import argparse


class Statist:
    def __init__(self, arguments: argparse.Namespace):
        self.args = arguments

        self.downloader = statlib.downloaders[self.args.source]
        self.language_module = statlib.language_modules[self.args.language]
        self.analyser = statlib.analysers[self.args.part_of_speech]
        self.output = statlib.outputs[self.args.output_format]

    def get_statistic(self):
        downloader_object = self.downloader(self.args.url_path)
        file_paths = downloader_object.download()

        language_module_object = self.language_module(file_paths)
        words = language_module_object.get_words_from(self.args.code_element)

        analyzed_words = self.analyser(words, limit=self.args.limit)

        self.output(self.args, analyzed_words)


def get_arguments() -> argparse.Namespace:
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        'url_path',
        metavar='URL',
        type=str,
        help='URL path to repository.',
    )

    argparser.add_argument(
        '--part-of-speech', '--pos', '-p',
        type=str,
        choices=['verbs', 'nouns'],
        default='verbs',
        help='Parts of speech that will be searched.',
    )

    argparser.add_argument(
        '--code-element', '-c',
        type=str,
        choices=['function', 'variable', 'class'],
        default='function',
        help='Elements of the code in which the search will be performed.',
    )

    argparser.add_argument(
        '--output-format', '-o',
        type=str,
        choices=['csv', 'json', 'stdout'],
        default='stdout',
        help='Output format.'
    )

    argparser.add_argument(
        '--source', '-s',
        type=str,
        choices=['github'],
        default='github',
        help='Service with git repository.',
    )

    argparser.add_argument(
        '--language', '-l',
        type=str,
        choices=['python'],
        default='python',
        help='Programming language.'
    )

    argparser.add_argument(
        '--limit',
        type=int,
        default=20,
        help='Word output limit.'
    )

    args = argparser.parse_args()
    return args


if __name__ == '__main__':
    arguments = get_arguments()
    statist = Statist(arguments)
    statist.get_statistic()
