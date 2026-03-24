import sys
from unittest.mock import MagicMock, patch

import pytest

from spadesdk.file_processor import File, FileProcessor, FileUpload
from spadesdk.user import User


class ConcreteFileProcessor(FileProcessor):
    @classmethod
    def process(cls, file, filename, data, user_params, user, *args, **kwargs):
        return FileUpload(file=file, result=FileUpload.Result.SUCCESS, rows=10)


def test_file_processor_cannot_be_instantiated_directly():
    with pytest.raises(TypeError):
        FileProcessor()


def test_concrete_file_processor_can_be_instantiated():
    fp = ConcreteFileProcessor()
    assert fp is not None


def test_process_returns_file_upload():
    file = File(name="test.csv", format="csv")
    user = User(id=1, email="a@b.com", first_name="Alice", last_name="Smith")
    result = ConcreteFileProcessor.process(file, "test.csv", b"data", {}, user)
    assert isinstance(result, FileUpload)
    assert result.result == FileUpload.Result.SUCCESS
    assert result.rows == 10


def test_file_upload_result_enum_values():
    assert FileUpload.Result.SUCCESS.value == "success"
    assert FileUpload.Result.WARNING.value == "warning"
    assert FileUpload.Result.FAILED.value == "failed"


def test_file_optional_fields():
    file = File(name="test.csv", format="csv")
    assert file.system_params is None
    assert file.schema is None


def test_validate_raises_import_error_when_pandera_missing():
    file = File(name="test.csv", format="csv", schema={"fields": []})
    with patch.dict(sys.modules, {"pandera": None, "pandera.io": None}):
        import spadesdk.file_processor as fp_module

        original = fp_module.PANDERA_PRESENT
        fp_module.PANDERA_PRESENT = False
        try:
            with pytest.raises(ImportError, match="spadesdk\\[pandera\\]"):
                FileProcessor.validate(file, MagicMock())
        finally:
            fp_module.PANDERA_PRESENT = original


def test_validate_raises_value_error_when_schema_is_none():
    file = File(name="test.csv", format="csv", schema=None)
    import spadesdk.file_processor as fp_module

    original = fp_module.PANDERA_PRESENT
    fp_module.PANDERA_PRESENT = True
    try:
        with pytest.raises(ValueError, match="schema is not defined"):
            FileProcessor.validate(file, MagicMock())
    finally:
        fp_module.PANDERA_PRESENT = original


@pytest.mark.skipif(
    not __import__("importlib.util", fromlist=["find_spec"]).find_spec("pandera"),
    reason="pandera not installed",
)
def test_validate_happy_path():
    import pandas as pd

    file = File(
        name="test.csv",
        format="csv",
        schema={
            "fields": [
                {"name": "id", "type": "integer"},
                {"name": "name", "type": "string"},
            ]
        },
    )
    df = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
    result = FileProcessor.validate(file, df)
    assert result is not None


@pytest.mark.skipif(
    not __import__("importlib.util", fromlist=["find_spec"]).find_spec("pandera"),
    reason="pandera not installed",
)
def test_validate_invalid_data_raises_schema_errors():
    import pandas as pd
    from pandera.errors import SchemaErrors

    file = File(
        name="test.csv",
        format="csv",
        schema={
            "fields": [
                {"name": "id", "type": "integer"},
            ]
        },
    )
    df = pd.DataFrame({"id": ["not_an_int", "also_not"]})
    with pytest.raises(SchemaErrors):
        FileProcessor.validate(file, df)
