# code-stat-tool

A utility for parsing code in the git repository.

### Usage
```
stat-tool.py [-h] [--part-of-speech {verbs,nouns}]
                    [--code-element {function,variable,class}]
                    [--output-format {csv,json,stdout}] [--source {github}]
                    [--language {python}] [--limit LIMIT]
                    URL

positional arguments:
  URL                   URL path to repository.

optional arguments:
  -h, --help            show this help message and exit
  --part-of-speech, --pos, -p {verbs,nouns}
                        Parts of speech that will be searched.
  --code-element, -c {function,variable,class}
                        Elements of the code in which the search will be
                        performed.
  --output-format, -o {csv,json,stdout}
                        Output format.
  --source, -s {github}
                        Service with git repository.
  --language, -l {python}
                        Programming language.
  --limit LIMIT         Word output limit.
```
  
### Example
```
./stat-tool.py -c variable -p nouns --limit 5 https://github.com/ytdl-org/youtube-dl
[('video', 818), ('id', 763), ('tests', 467), ('title', 416), ('webpage', 408)]
```
