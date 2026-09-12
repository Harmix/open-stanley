.PHONY: test lint validate
test:
	python3 evals/run_audit_tests.py && python3 -m unittest discover -s tests
lint:
	python3 -m py_compile skills/stanley/scripts/stanley-audit skills/stanley/scripts/stanley-vault skills/stanley/scripts/stanley-stats skills/stanley/scripts/stanley-preview
validate:
	claude plugin validate .
