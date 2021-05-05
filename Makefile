.PHONY: clean
clean:
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -rf dist/
	@rm -rf build/

.PHONY: clean-docs
clean-docs:
	@rm -rf doc/ && mkdir -p doc

.PHONY: format
format:
	@black .
