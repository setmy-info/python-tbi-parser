# python-tbi-parser

Training Backlog Item file parser

## Development

### Preparations

```shell
# Win
py -3.9 -m venv ./.venv
# *nix
python -m venv ./.venv
# Win
.\.venv\Scripts\activate
# *nix
source ./.venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For developing depending project/module, dependency can be added into **requirements.txt** as:

    python-commons @ file:///C:/sources/setmy.info/submodules/python-commons

### PyCharm

"File" -> "Settings" -> Python Integrated Tools -> Default test runner: Unittest

Running tests have a problem: working directory has to be set for tests.

### Run unit tests

```shell
python -m unittest discover -s ./test/info/setmy
```

### Run integration tests

```shell
python -m unittest discover -s ./test/info/setmy -p it_*.py
```

### Run behave (Cucumber) integration tests

```shell
behave
```

### All tests

```shell
python -m unittest discover -s ./test/info/setmy && python -m unittest discover -s ./test/info/setmy -p it_*.py && behave
```

### Update version info

```shell
# Win
set NAME=smi_python_tbi_parser
set VERSION=0.4.0
# *nix
NAME=smi_python_tbi_parser
VERSION=0.4.0
# Win
python -m smi_python_commons.scm_version %NAME% %VERSION%
# *nix
python -m smi_python_commons.scm_version ${NAME} ${VERSION}
git add ./${NAME}/project.py
git commit -m "project.py updated"
git push
```

## Deploy

```shell
python setup.py sdist bdist_wheel
twine upload dist/*
git tag -a ${VERSION} -m "${VERSION}"
git push --tags
```

## Release

1. Update version info
2. Deploy

```shell
python setup.py sdist bdist_wheel && twine upload dist/*
```
