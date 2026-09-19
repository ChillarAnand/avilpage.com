from diagrams import Diagram, Cluster, Edge
from diagrams.generic.compute import Rack
from diagrams.programming.language import Python

with Diagram("Local LLM stack", show=False, direction="LR", filename="how-i-run-llms-locally-on-mac"):

    with Cluster("Harness"):
        pi = Rack("Pi")
        oc = Rack("OpenCode")

    with Cluster("Inference Server"):
        omlx = Python("omlx")

    with Cluster("Models"):
        m1 = Rack("Qwen3.8-27B-4bit")
        m2 = Rack("Qwen3.6-35B-A3B-4bit")

    for node in (pi, oc):
        node >> Edge(label="API", color="#0056b3", dir="both") >> omlx

    omlx >> Edge(label="serves", color="#6c757d") >> [m1, m2]
