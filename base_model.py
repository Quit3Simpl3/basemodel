# Django Imports:
from django.db import models
# Python Imports:
from uuid import uuid4

class BaseModel(models.Model):
    ''' BaseModel is used for creating new models with some generic fields that should be in each object. '''
        # To guarantee uniqueness in case of copying to another table.
        uuid = models.UUIDField(
            verbose_name="UUID",
            unique=True,
            default=uuid4,
            editable=False,
            null=False,
            blank=False
            )
        # Timestamp at object's creation.
        timestamp = models.DateTimeField(
            verbose_name="Timestamp",
            auto_now_add=True,
            editable=False,
            null=True,
            blank=False
            )
        # Functions:
        # __unicode__ is for Python<3 compatibility.
        def __unicode__(self):
            return self.id
            
        # __str__ is for Python>3 compatibility.
        def __str__(self):
            return self.__unicode__()
            
        # Meta class.
        class Meta:
            # Setting the model as 'abstract' prevents Django from creating two objects when you create a child model's object.
            abstract = True
