# Tasks for the project

## build

> Builds all crates and packages

~~~sh
uv sync --all-packages
~~~

## fmt

> Formats the code

~~~sh
uv run ruff format
uv run isort .
~~~

## lint

> Lints the code

~~~sh
uv run ruff check
uv run isort --check-only --diff .
uv run mypy --strict --pretty .
~~~

## test

> Runs all tests

~~~sh
uv sync --all-packages > /dev/null 2>&1
uv run pytest
~~~
