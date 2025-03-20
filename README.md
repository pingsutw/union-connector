# Install the required packages
```
pip install union flytekit==1.16.0b0
```

To deploy the connector
```
union deploy apps app.py my-connector-app
```

To run the workflow
```
union run --remote workflow.py wf
```