import asyncio
import typing
from dataclasses import dataclass
from flytekit import logger, FlyteContextManager
from flytekit.core.type_engine import TypeEngine
from flytekit.extend.backend.base_connector import (
    AsyncConnectorBase,
    Resource,
    ResourceMeta, ConnectorRegistry,
)
from flytekit.models.literals import LiteralMap
from flytekit.models.task import TaskTemplate
from flyteidl.core.execution_pb2 import TaskExecution


@dataclass
class Metadata(ResourceMeta):
    name: str


class MyConnector(AsyncConnectorBase):
    name = "My Webhook Connector"

    def __init__(self):
        super().__init__(task_type_name="my_connector", metadata_type=Metadata)

    async def create(
        self,
        task_template: TaskTemplate,
        inputs: typing.Optional[LiteralMap] = None,
        **kwargs,
    ) -> Metadata:
        logger.info("MyConnector is creating a task.")
        ctx = FlyteContextManager.current_context()
        logger.info(inputs)
        python_values = TypeEngine.literal_map_to_kwargs(ctx, inputs, literal_types=task_template.interface.inputs)
        logger.info(f"job_id = {python_values['job_id']}")
        # Mock API request
        await asyncio.sleep(0.25)
        return Metadata(name="union")

    async def get(self, resource_meta: Metadata, **kwargs) -> Resource:
        logger.info("MyConnector is getting the status of the task.")
        # Mock API request
        await asyncio.sleep(0.5)
        return Resource(phase=TaskExecution.SUCCEEDED)

    async def delete(self, resource_meta: Metadata, **kwargs):
        logger.info("MyConnector is deleting the task.")
        assert isinstance(resource_meta, Metadata)
        return


ConnectorRegistry.register(MyConnector(), override=True)