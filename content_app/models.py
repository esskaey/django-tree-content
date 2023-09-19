from ambient_toolbox.models import CommonInfo
from django.conf import settings
from django.db import models

from tree_node.models import Node, TreeNodeType


# Create your models here.
class ContentModel(CommonInfo):
    language = models.CharField(choices=settings.LANGUAGES, max_length=24)
    node = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
        limit_choices_to={"object_type": TreeNodeType.EXCEPTION},
    )

    class Meta:
        abstract = True
