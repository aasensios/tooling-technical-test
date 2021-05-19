# tooling-technical-test

Technical test for candidate selection for a fullstack developer job position.

Read the [questions](questions.md).

Set up the Python virtual environment:
```sh
git clone https://github.com/aasensios/tooling-technical-test.git
cd tooling-technical-test
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

For questions 1 and 2, first run the linter and the tests and then inspect the code implementations in `fifo*.py` and `shape*.py` files.
```sh
pylint *.py
pytest -s
```

For question 3, check the [PostgreSQL syntax file](teachers_and_classes.sql).

For question 4, check the [response diagram](architecture_diagram.pdf).

For the questions about fundamentals, check the [multiple choice responses](fundamentals_responses.txt).
