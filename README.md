# Single Expression Calculator

This flask app was written using Python 3.12 and [Flask 3.0.3](requirements.txt).

The logic for this program uses several [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) to read the user input
and tokenize each part of the expression.

[functions.py](functions.py) contains the code for all the tokenization and operator logic.

[templates](templates/) contains [numberpad.html](templates/numberpad.html) which generates a numberpad on localhost for user input.

The colours are funky, coming from [styles.css](static/styles.css).



# Install and run

Download and extract zip folder.

For convenience, create and activate a [python virtual environment](https://docs.python.org/3/library/venv.html)

and then install the required version of flask by running: <br/>
```markdown 
pip install -r requirements.txt
```

Next open up a terminal and navigate to the directory with [app.py](app.py)

- if using powershell,
  run<br/> 
  ```markdown
  python -m flask run --debug
  ```

- if using wsl,
  run<br/>
  ```markdown
  $ flask --app hello run
  ```

# Version 1.0 (2024-09-11)

- Accepts only single expression inputs in the form of:
  ``` Number operator Number ```
