from typing import Any, Type

from diagrams import Node
from diagrams.onprem import _OnPrem


def import_on_prem_parent_nodes() -> list[Type[_OnPrem]]:
    from diagrams.onprem.aggregator import _Aggregator
    from diagrams.onprem.analytics import _Analytics
    from diagrams.onprem.auth import _Auth
    from diagrams.onprem.cd import _Cd
    from diagrams.onprem.certificates import _Certificates
    from diagrams.onprem.ci import _Ci
    from diagrams.onprem.client import _Client
    from diagrams.onprem.compute import _Compute
    from diagrams.onprem.database import _Database
    from diagrams.onprem.dns import _Dns
    from diagrams.onprem.etl import _Etl
    from diagrams.onprem.gitops import _Gitops
    from diagrams.onprem.inmemory import _Inmemory
    from diagrams.onprem.logging import _Logging
    from diagrams.onprem.network import _Network
    from diagrams.onprem.queue import _Queue
    from diagrams.onprem.storage import _Storage

    return [
        _Database,
        _Queue,
        _Network,
        _Inmemory,
        _Storage,
        _Logging,
        _Auth,
        _Client,
        _Analytics,
        _Aggregator,
        _Certificates,
        _Cd,
        _Ci,
        _Compute,
        _Dns,
        _Etl,
        _Gitops,
    ]


def _collect_subclasses(
    diagrams_parent_class: Type[Node], base_class: Type[Any]
) -> list[Type[Any]]:
    new_classes = []
    for diagram_child_class in diagrams_parent_class.__subclasses__():
        new_class = type(
            f"{diagram_child_class.__name__}Image",
            (base_class,),
            {
                "pattern": str(diagram_child_class.__name__).lower(),
                "diagram_render_class": diagram_child_class,
            },
        )
        new_classes.append(new_class)

    return new_classes


def register_all_icons_from_diagrams(base_class: Type[Any]) -> list[Type[Any]]:
    """Collect"""
    new_classes = []

    for on_prem_diagrams_parent in import_on_prem_parent_nodes():
        database_classes = _collect_subclasses(
            diagrams_parent_class=on_prem_diagrams_parent, base_class=base_class
        )
        new_classes.extend(database_classes)

    return new_classes
