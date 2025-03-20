from flytekit import workflow
from task import MyConnectorTask


t1 = MyConnectorTask(duration=2, name="my_webhook", inputs={"job_id": int})


@workflow
def wf():
     t1(job_id=3)
