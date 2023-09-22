from ambient_toolbox.models import CommonInfo
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from tree_node.models import Node, TreeNodeType


# Create your models here.
class ContentModel(CommonInfo):
    language = models.CharField(choices=settings.LANGUAGES, max_length=24)
    node = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        limit_choices_to={"object_type": TreeNodeType.EXCEPTION},
    )

    class Meta:
        abstract = True


class ExceptionContentModel(ContentModel):
    description = models.TextField(help_text="Enter some description on the exception")
    operator_text = models.TextField(help_text="Enter some operator text here")
    service_text = models.TextField(help_text="Enter some service text here")

    def clean(self):
        if self.node.object_type != TreeNodeType.EXCEPTION:
            raise ValidationError(
                "Cannot link content model to a node other than exception type"
            )
