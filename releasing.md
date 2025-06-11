### Release process

* Update Changelog (`changelog.md` file)

* Bump version number

```bash
# choose one based on semver rules
poetry version patch
poetry version minor
poetry version major
```

* Commit

* Make tag and upload to github

```bash
git tag -a major.minor.patch -m "Release vmajor.minor.patch"
git push origin major.minor.patch # refs/tags/major.minor.patch
# e.g.
git tag -a 0.1.2 -m "Release v0.1.2"
git push origin "0.1.2"
```

* Build and validate documentation

```bash
mkdocs build --clean
mkdocs serve
```

* Build package

```bash
poetry build
```

* Upload to PyPI

```bash
poetry publish
```
