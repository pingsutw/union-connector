from typing import Optional, Dict, Any, Type

from flytekit.configuration import SerializationSettings
from flytekit.core.base_task import PythonTask
from flytekit.core.interface import Interface
from flytekit.extend.backend.base_connector import (
    AsyncConnectorExecutorMixin,
)


class MyConnectorTask(AsyncConnectorExecutorMixin, PythonTask):
    _TASK_TYPE = "my_connector"

    def __init__(
        self,
        name: str,
        inputs: Optional[Dict[str, Type]] = None,
        outputs: Optional[Dict[str, Type]] = None,
        duration: int = 2,
        **kwargs,
    ):
        super().__init__(
            name=name,
            interface=Interface(inputs=inputs, outputs=outputs),
            task_type=self._TASK_TYPE,
            **kwargs,
        )
        self._duration = duration

    def get_custom(self, settings: SerializationSettings) -> Optional[Dict[str, Any]]:
        return {"duration": self._duration}
