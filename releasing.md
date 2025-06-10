### Release process

* Make sure you have activated virtual environment and installed all the dev dependencies

```bash
$ pyenv activate python-dogecoin
$ pip install -e .[dev]
```

* Update Changelog (`changelog.md` file)

* Bump version number

* Commit

* Make tag and upload to github

```bash
$ git tag -a major.minor.patch -m "Release vmajor.minor.patch"
$ git push origin major.minor.patch # refs/tags/major.minor.patch
# e.g.
$ git tag -a 0.1.2 -m "Release v0.1.2"
$ git push origin "0.1.2"
```

* Build and validate documentation

```bash
$ mkdocs build --clean
$ mkdocs serve
```

* Build package

```bash
poetry build
```

* Upload to PyPI

```bash
poetry publish
```
