from ambient_toolbox.models import CommonInfo
from dirtyfields import DirtyFieldsMixin
from django.db import models
from treebeard.mp_tree import MP_Node

# Create your models here.


class TreeNodeType(models.IntegerChoices):
    UNASSIGNED = 0, "UNASSIGNED"
    MACHINE = 1, "MACHINE"
    MACHINE_SECTION = 2, "MACHINE_SECTION"
    MACHINE_MODULE = 3, "MACHINE_MODULE"
    EXCEPTION_GROUP = 4, "EXCEPTION_GROUP"
    EXCEPTION = 5, "EXCEPTION"


class Node(DirtyFieldsMixin, CommonInfo, MP_Node):
    name = models.CharField(max_length=255)
    object_type = models.IntegerField(
        choices=TreeNodeType.choices, default=TreeNodeType.UNASSIGNED
    )
    node_order_by = ["name"]

    def __str__(self):
        return self.name
