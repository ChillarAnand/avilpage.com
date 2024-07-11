def pip_wtf(command):
    import os, os.path, sys
    t = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".pip_wtf." + os.path.basename(__file__))
    sys.path = [p for p in sys.path if "-packages" not in p] + [t]
    os.environ["PATH"] += os.pathsep + t + os.path.sep + "bin"
    os.environ["PYTHONPATH"] = os.pathsep.join(sys.path)
    if os.path.exists(t): return
    os.system(" ".join([sys.executable, "-m", "pip", "install", "-t", t, command]))



pip_wtf("diagrams")


from diagrams import Diagram
from diagrams.custom import Custom
from diagrams.aws.compute import EC2



with Diagram("HIS", show=True):
    t1 = EC2('EC2')
    t2 = EC2('EC2')
    t1 >> t2
    his = Custom('HIS', None)
    mirth = Custom('Mirth', None)
    his >> mirth
