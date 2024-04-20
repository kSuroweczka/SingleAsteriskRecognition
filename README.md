# SingleAsteriskRecognition

The aim of this program is to find a single asterisk in input JSON `Resource` field.

Method return logical `False` if an input contains a single asterisk and `True` in any other case.

### Technologies

    - Python
    - Pytest

### How to run

    1. Clone the repository to your local machine.
    2. Make sure you have Python, Pytest installed.
    3. Run the application using `pytest --no-header -vv` or `pytest`.

### Tested cases:

1. Single Asterisk in Resource field.
2. Double Asterisk in Resource field.
3. Single Asterisk with other text in in Resource field.
4. Double Asterisk with other text in in Resource field.
5. Empty Resource field.
6. Empty Policy Document field.
7. Invalid JSON file.
8. No Resource field.
9. Single Asterisk in two of two Statements.
10. Single Asterisk in one of two Statements.
