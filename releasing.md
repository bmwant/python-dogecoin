### Release process

```bash
$ pyenv activate python-dogecoin
$ pip install -e .[dev]
$ make clean
$ python -m build
$ twine upload dist/*
```

* Update Changelog (using git history output from dist-tools/changelog.sh)

* Change version numbers in setup.py and sphinx/source/conf.py

* Commit

* Make tag and upload to github

    - git tag -a vX.X
    - git push origin vX.X

* Run make in doc/

* Update documentation on github

```bash
$ git checkout gh_pages
$ rm -r doc
$ mkdir doc
$ cp -r sphinx/build/html/* doc/
$ git add doc
$ git commit -a
$ git push origin gh-pages:gh-pages
```

* Upload to PyPI

```bash
$ twine upload dist/*
```
