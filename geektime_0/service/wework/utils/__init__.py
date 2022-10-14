import os


def project_dir(path=""):
    root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(root, path)
