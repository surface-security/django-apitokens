.PHONY: style
style:
	uv run ruff format apitokens testapp
	uv run ruff check --fix apitokens testapp

.PHONY: style_check
style_check:
	uv run ruff format --check apitokens testapp
	uv run ruff check apitokens testapp

.PHONY: build_lib
build_lib:
	uv build
