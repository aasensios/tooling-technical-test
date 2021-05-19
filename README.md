# tooling-technical-test

Technical test for candidate selection for a fullstack developer job position.

Read the [questions](questions.md).

Set up the virtual environment:
```sh
git clone https://github.com/aasensios/tooling-technical-test.git
cd tooling-technical-test
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the linter and the tests:
```sh
pylint *.py
pytest
```

Inspect the code of the implementations (`*.py` files) and check the [responses](fundamentals_responses.txt) to the fundamentals questions.
