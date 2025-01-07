# Calc-it

This calculator was built with Python 3.12 and [Flask 3.0.3](requirements.txt).

The logic for this program uses several [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) to read the user input
and tokenize each part of the expression.

[functions.py](functions.py) contains the code for all the tokenization and operator logic.

[templates](templates/) contains [numberpad.html](templates/numberpad.html) which generates a numberpad for user input.

HTML styling coming from [styles.css](static/styles.css).

## Install and run

For convenience, create and activate a [python virtual environment](https://docs.python.org/3/library/venv.html)

and then install the required version of flask by running:

- for Windows

  ```markdown
  pip install -r requirements.txt
  ```

- for Ubuntu

  ```markdown
  pip install -r UBUrequirements.txt
  ```

Next open up a terminal and navigate to the directory with [app.py](app.py)

Flask shares the same command for both systems

- Run the app with:

  ```markdown
  python -m flask --app app.py run
  ```

- Open a browser and navigate to

  ```html
  http://127.0.0.1:5000
  ```

## Versions

- 1.1 (2025-01-07)

  - Added support for longer expressions
  - No error messages yet

- 1.0 (2024-09-11)

  - Accepts only single expression inputs in the form of:

    ```text
    Number operator Number
    ```
