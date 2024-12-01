from graphviz import Digraph

# Create a flowchart for the GET operation with the updated process
flowchart = Digraph(format="png", name="GET_Operation_Proper")
flowchart.attr(rankdir="TB", size="8,10")

# Define nodes with descriptions
flowchart.node("Start", "Start")
flowchart.node("HashKey", "Hash the Key")
flowchart.node("FindCoordinator", "Identify Coordinator Node")
flowchart.node("SendToCoordinator", "Send GET Request to Coordinator Node")
flowchart.node("IdentifyReplicas", "Coordinator Identifies N Replicas")
flowchart.node("SendToReplicas", "Send Requests to Replicas")
flowchart.node("WaitForQuorum", "Wait for Responses (Read Quorum)")
flowchart.node("QuorumReached", "Quorum Reached?")
flowchart.node("RetryFail", "Retry or Fail")
flowchart.node("ReceiveVersions", "Receive Versions from Replicas")
flowchart.node("ConflictsDetected", "Conflicts Detected?")
flowchart.node("Reconcile", "Reconcile Conflicts")
flowchart.node("ReturnData", "Return Data to Client")
flowchart.node("ReadRepair", "Perform Read Repair")
flowchart.node("End", "End Process")

# Define edges with relationships
flowchart.edges([
    ("Start", "HashKey"),
    ("HashKey", "FindCoordinator"),
    ("FindCoordinator", "SendToCoordinator"),
    ("SendToCoordinator", "IdentifyReplicas"),
    ("IdentifyReplicas", "SendToReplicas"),
    ("SendToReplicas", "WaitForQuorum"),
    ("WaitForQuorum", "QuorumReached"),
    ("QuorumReached", "RetryFail", label="No"),
    ("QuorumReached", "ReceiveVersions", label="Yes"),
    ("ReceiveVersions", "ConflictsDetected"),
    ("ConflictsDetected", "Reconcile", label="Yes"),
    ("ConflictsDetected", "ReturnData", label="No"),
    ("Reconcile", "ReturnData"),
    ("ReturnData", "ReadRepair"),
    ("ReadRepair", "End")
])

# Render the flowchart and save
output_path = "/mnt/data/GET_Operation_Flowchart_Final"
flowchart.render(output_path, format="png", cleanup=False)

output_path + ".png"
