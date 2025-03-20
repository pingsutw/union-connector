from union import ImageSpec, Resources, Secret
from union.app import FlyteConnectorApp

image = ImageSpec(
    name="flyteconnector",
    packages=[
        "flytekit[connector]>=1.16.0b0",
        "union",
        "union-runtime",
    ],
    env={"FLYTE_SDK_LOGGING_LEVEL": "10"},
    builder="union",
)

openai_connector_app = FlyteConnectorApp(
    name="my-connector-app",
    container_image=image,
    secrets=[Secret(key="my_connector_api_key")],
    limits=Resources(cpu="1", mem="1Gi"),
    include=["./myconnector"],
)
