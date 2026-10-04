import json
from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture(scope="session")
def expected_cases():
    return json.loads((FIXTURES / "expected_cases.json").read_text())
