import pytest

from spadesdk.executor import Executor, Process, RunResult
from spadesdk.user import User


class ConcreteExecutor(Executor):
    @classmethod
    def run(cls, process, user_params, user, *args, **kwargs):
        return RunResult(
            process=process,
            status=RunResult.Status.FINISHED,
            result=RunResult.Result.SUCCESS,
            user_id=user.id,
        )


def test_executor_cannot_be_instantiated_directly():
    with pytest.raises(TypeError):
        Executor()


def test_concrete_executor_can_be_instantiated():
    executor = ConcreteExecutor()
    assert executor is not None


def test_run_returns_run_result():
    process = Process(code="test_process")
    user = User(id=1, email="a@b.com", first_name="Alice", last_name="Smith")
    result = ConcreteExecutor.run(process, user_params={}, user=user)
    assert isinstance(result, RunResult)
    assert result.status == RunResult.Status.FINISHED
    assert result.result == RunResult.Result.SUCCESS
    assert result.user_id == user.id


def test_run_result_user_field():
    process = Process(code="test_process")
    user = User(id=42, email="x@y.com", first_name="Bob", last_name="Jones")
    result = RunResult(process=process, status=RunResult.Status.NEW, user_id=user.id)
    assert result.user_id == 42


def test_run_result_user_defaults_to_none():
    process = Process(code="test_process")
    result = RunResult(process=process, status=RunResult.Status.NEW)
    assert result.user_id is None


def test_run_result_status_enum_values():
    assert RunResult.Status.NEW.value == "new"
    assert RunResult.Status.RUNNING.value == "running"
    assert RunResult.Status.FINISHED.value == "finished"
    assert RunResult.Status.FAILED.value == "failed"


def test_run_result_result_enum_values():
    assert RunResult.Result.SUCCESS.value == "success"
    assert RunResult.Result.WARNING.value == "warning"
    assert RunResult.Result.FAILED.value == "failed"


def test_process_optional_system_params():
    process = Process(code="test_process")
    assert process.system_params is None

    process_with_params = Process(code="test_process", system_params={"key": "value"})
    assert process_with_params.system_params == {"key": "value"}
