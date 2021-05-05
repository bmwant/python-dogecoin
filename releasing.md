### Release process

* Make sure you have activated virtual environment and installed all the dev dependencies

```bash
$ pyenv activate python-dogecoin
$ pip install -e .[dev]
```

* Update Changelog (`changelog.md` file)

* Change version number in `setup.py` file

* Commit

* Make tag and upload to github

```bash
$ git tag -a vX.X
$ git push origin vX.X
```

* Build and validate documentation

```bash
$ mkdocs build --clean
$ mkdocs serve
```

* Build package

```bash
$ make clean
$ python -m build
```

* Upload to PyPI

```bash
$ twine upload dist/*
```
