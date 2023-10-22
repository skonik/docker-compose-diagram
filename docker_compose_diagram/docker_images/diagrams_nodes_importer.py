import importlib
import inspect
import pkgutil
from types import ModuleType
from typing import Any, Type

from diagrams import Node

from docker_compose_diagram.constants import DIAGRAMS_PACKAGE_NAME


FIRST_VARIABLE_INDEX = 0
FIRST_BASE_CLASS_INDEX = 0
PARENT_CLASS_PREFIX = "_"

PATTERNS_REFORMAT = {"r": r"^R$"}


def import_all_parent_nodes():
    """
    Diagrams packages has parent nodes like _Database
    which are inherited by actual icon nodes.
    We can search for all such subclasses.

    Firstly we can iterate over all packages inside diagrams nodes.
    Then iterate over each file in the package.
    And find classes that start with `_`.
    We will consider them as parent classes for our nodes.
    Then we can just return these parent nodes.
    """
    source_package_module: ModuleType = importlib.import_module(DIAGRAMS_PACKAGE_NAME)
    source_package_module_path = source_package_module.__path__

    all_parent_nodes = []
    # high_level_module is something like diagrams.aws, diagrams.onprem, etc
    for high_level_module in pkgutil.iter_modules(source_package_module_path):

        diagrams_high_level_package_name = ".".join(
            [DIAGRAMS_PACKAGE_NAME, high_level_module.name]
        )
        diagrams_high_level_package: ModuleType = importlib.import_module(
            diagrams_high_level_package_name
        )
        diagrams_high_level_package_path = diagrams_high_level_package.__path__

        # low level module is something like diagrams.onprem.database, etc
        for low_level_module in pkgutil.iter_modules(diagrams_high_level_package_path):
            diagrams_low_level_module_name = ".".join(
                [diagrams_high_level_package_name, low_level_module.name]
            )
            diagrams_low_level_module: ModuleType = importlib.import_module(
                diagrams_low_level_module_name
            )

            module_variables = inspect.getmembers(diagrams_low_level_module)

            name, obj = module_variables[FIRST_VARIABLE_INDEX]
            if name.startswith(PARENT_CLASS_PREFIX):
                all_parent_nodes.append(obj)
                continue

            first_parent_class = obj.__bases__[FIRST_BASE_CLASS_INDEX]
            all_parent_nodes.append(first_parent_class)

    return all_parent_nodes


def _create_docker_image_classes(
    diagrams_parent_class: Type[Node], base_class: Type[Any]
) -> list[Type[Any]]:
    new_classes = []
    for diagram_child_class in diagrams_parent_class.__subclasses__():
        pattern = str(diagram_child_class.__name__).lower()
        if pattern in PATTERNS_REFORMAT:
            pattern = PATTERNS_REFORMAT[pattern]

        new_class = type(
            f"{diagram_child_class.__name__}Image",
            (base_class,),
            {
                "pattern": pattern,
                "diagram_render_class": diagram_child_class,
            },
        )
        new_classes.append(new_class)

    return new_classes


def create_docker_image_patterns_from_diagrams(
    base_class: Type[Any],
) -> list[Type[Any]]:
    """
    Collect all diagrams nodes and create proper wrappers
    (classes which inherit our DockerImagePattern class)
    """
    all_nodes = []

    for parent_node in import_all_parent_nodes():
        nodes = _create_docker_image_classes(
            diagrams_parent_class=parent_node, base_class=base_class
        )
        all_nodes.extend(nodes)

    return all_nodes
