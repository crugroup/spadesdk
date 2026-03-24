"""Verify that all public classes are importable from the top-level package."""


def test_executor_importable():
    from spadesdk import Executor

    assert Executor is not None


def test_process_importable():
    from spadesdk import Process

    assert Process is not None


def test_run_result_importable():
    from spadesdk import RunResult

    assert RunResult is not None


def test_file_importable():
    from spadesdk import File

    assert File is not None


def test_file_processor_importable():
    from spadesdk import FileProcessor

    assert FileProcessor is not None


def test_file_upload_importable():
    from spadesdk import FileUpload

    assert FileUpload is not None


def test_history_provider_importable():
    from spadesdk import HistoryProvider

    assert HistoryProvider is not None


def test_user_importable():
    from spadesdk import User

    assert User is not None
