import re


IMAGE_EXTENSION_RE = re.compile(r".*\.(png)$")
PACKAGE_CLASS_PATH = re.compile(r"^(?P<package_path>[^:]*)\.(?P<class_name>[A-z].*)")
DIAGRAMS_PACKAGE_NAME = "diagrams"
