# Contributing to Days Off

Hello! Thank you for considering contributions to Days Off. All forms of contribution are greatly appreciated! Whether it's reporting bugs, suggesting enhancements, or writing code, every bit helps to improve our project.

## Our Git Workflow

Our project uses a typical Git workflow consisting of two main branches:

- `main`: This is a stable branch and it is meant for production use. It contains the latest released version of the application. Any commits here should only be for new releases or hotfixes.

- `development`: This is the branch for day-to-day work. It contains the newest changes and contributions should be proposed to this branch.

When contributing, please create a new branch off the `development` branch, not directly on `development`. Once your changes are ready for review, open a Pull Request against `development`.

## Reporting Bugs

We track bugs as GitHub issues. Please check existing issues to avoid reporting duplicates. When creating a new issue:

- Provide a descriptive issue title
- Detailed steps for how to reproduce the issue
- Describe the expected and actual behaviour
- Include screenshots if relevant

## Suggesting Enhancements

Suggestions for enhancements are also tracked as GitHub issues. When creating an enhancement suggestion:

- Provide a clear and descriptive title
- Detailed explanation of the suggested enhancement
- Include examples if applicable

## First Time Contributors

We mark some issues as "Good First Issue" for newcomers. Feel free to start there!

## Pull Requests

For your contribution to be accepted:

1. Make sure all tests pass
2. If you add code, please also add test coverage
3. Try to follow our Python coding style
4. Reference the issue ticket in your Pull Request

## Style Guidelines

We follow [PEP8](https://pep8.org/) style guide for Python code, and we use pre-commit hooks with "black" and "flake8" for auto-formatting and linting respectively.

## Commit Messages

- Keep first line under 72 characters
- Use imperative mood
- Reference the issue ticket, if applicable

We want to keep Days Off an open, welcoming environment. By participating in this project, you agree to adhere to our Code of Conduct.
