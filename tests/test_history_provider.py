import pytest

from spadesdk.executor import Process, RunResult
from spadesdk.history_provider import HistoryProvider


class ConcreteHistoryProvider(HistoryProvider):
    @classmethod
    def get_runs(cls, process, request, *args, **kwargs):
        return [RunResult(process=process, status=RunResult.Status.FINISHED, result=RunResult.Result.SUCCESS)]


def test_history_provider_cannot_be_instantiated_directly():
    with pytest.raises(TypeError):
        HistoryProvider()


def test_concrete_history_provider_can_be_instantiated():
    hp = ConcreteHistoryProvider()
    assert hp is not None


def test_get_runs_returns_iterable_of_run_results():
    process = Process(code="test_process")
    results = list(ConcreteHistoryProvider.get_runs(process, request=None))
    assert len(results) == 1
    assert isinstance(results[0], RunResult)
    assert results[0].status == RunResult.Status.FINISHED
