import io
import os
import json
import oci
from fdk import response
from oci.data_integration.data_integration_client import DataIntegrationClient

#Main handler entry point
def handler(ctx, data: io.BytesIO=None):
  signer = oci.auth.signers.get_resource_principals_signer()

  body = json.loads(data.getvalue())
  workspaceid = None
  applicationkey = None
  taskrunkey = None
  data = body.get("data")
  if data is not None:
    workspaceid = data["additionalDetails"]["workspaceId"]
    applicationkey = data["additionalDetails"]["applicationKey"]
    taskrunkey = data["additionalDetails"]["taskRunKey"]

  resp = None
  if (taskrunkey is None):
    resp = {"status": 400, "message": "Task run key must be provided."}
  else:
    resp = do(ctx.Config(), signer, workspaceid, applicationkey, taskrunkey)

  return response.Response(
    ctx, response_data=resp,
    headers={"Content-Type": "application/json"}
  )

# Main body of code
def do(cfg, signer, workspaceid, applicationkey, taskrunkey):
  try:
    dip = DataIntegrationClient(config={}, signer=signer)

    print("Terminate DIS Task", flush=True)
    print(" Workspace "+workspaceid, flush=True)
    print(" Application "+applicationkey, flush=True)
    print(" Task Run Key "+taskrunkey, flush=True)

    taskrun = oci.data_integration.models.UpdateTaskRunDetails(status="TERMINATING")
    ret = dip.update_task_run(workspaceid, applicationkey, taskrunkey, update_task_run_details=taskrun)
    return {"status":"200", "message":"Terminating task run :"+taskrunkey}
  except Exception as inst:
    return {"status":"400", "message":"{0}".format(str(inst))}
