# How to Contribute

Firstly, thanks for wanting to contribute back to this project. Below are
guidelines that should hopefully minimise the amount of backwards and forwards
in the review process.

## Getting Started

* Fork the repository on GitHub - well... duh :P
* Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
* Install the project and development dependencies: `uv sync --all-groups`
* Run the tests: `uv run pytest`

## Making Changes

* Create a topic branch from where you want to base your work.
  * This is usually the master branch.
  * Only target release branches if you are certain your fix must be on that
    branch.
  * To quickly create a topic branch based on master; `git checkout -b
    /my_contribution master`. Please avoid working directly on the
    `master` branch.
* Make commits of logical units.
* Check for unnecessary whitespace with `git diff --check` before committing.
* Run lint and formatting checks: `uv run pre-commit run --all-files`
* Make sure you have added the necessary tests for your changes.
* Run the tests with `uv run pytest`. CI checks Python 3.9 through 3.13.


## Submitting Changes

* Push your changes to a topic branch in your fork of the repository.
* Submit a pull request to the main repository
* After feedback has been given we expect responses within two weeks. After two
  weeks will may close the pull request if it isn't showing any activity.
