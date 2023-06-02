Introduction:

This function terminates a task from in OCI Data Integration using the event for exceeding max time duration which includes.
 - workspaceId
 - applicationKey
 - taskRunKey

Prequisites:
1. Go through the hello world OCI Functions example such that you have an environment for creating and testing functions - https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingfirst.htm
2.Create policies for the function below which depends on having access to OCI Data Integration, you will need and use on the workspace.
  eg allow dynamic-group your_faas_dyn_group to use dis-workspaces in compartment yourcompartment
3. Download the func.py func.yaml and requirements.txt files in this gist.

fn -v deploy --app YOUR_FN_APP_NAME

Introduction:

Test standalone first;

eg:
echo '{ "data" : {"additionalDetails" : {"taskRunKey" : "YOURTASKRUNKEY","applicationKey" : "YOURAPPLICATIONKEY", "workspaceId" : "YOURWORkSPACEID"}}}' | fn invoke YOUR_FN_APP_NAME terminate-taskrun

Ensure this works. Check function logs if it fails.
