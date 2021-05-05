### Release process

* Make sure you have activated virtual environment and installed all the dev dependencies

```bash
$ pyenv activate python-dogecoin
$ pip install -e .[dev]
```

* Update Changelog (`changelog.md` file)

* Change version numbers in `setup.py` and `sphinx/source/conf.py` files

* Commit

* Make tag and upload to github

```bash
$ git tag -a vX.X
$ git push origin vX.X
```

* Build documentation

```bash
$ mkdocs build
```

* Update documentation on github

```bash
$ git checkout gh_pages
$ make clean-doc
$ cp -r sphinx/build/html/* doc/
$ git add doc
$ git commit -a
$ git push origin gh-pages:gh-pages
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
