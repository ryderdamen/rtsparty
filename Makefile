.PHONY: publish-dev
publish-dev:
	@echo "Publishing Dev"; \
	twine upload --repository-url https://test.pypi.org/legacy/ dist/* --skip-existing

.PHONY: publish
publish:
	@echo "Publishing"
	twine upload dist/* --skip-existing

.PHONY: build
build:
	@echo "Building Dist...";
	@if [ -d "dist" ]; then rm -rf dist; fi
	@python setup.py sdist bdist_wheel

.PHONY: test
test:
	pytest tests/

.PHONY: test-local
test-local:
	@cd deployment && bash test_local.sh
