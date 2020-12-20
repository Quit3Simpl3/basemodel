# basemodel
### A very basic abstract model for Django>2.0.
### Included fields:
- uuid: unique ID to guarantee uniqueness across different systems. Can be used for safely merging tables while preventing Primary Key conflicts.
- timestamp: registeres a timestamp of the object's creation.
### Included functions:
- __unicode__(self): returns a string representing the object (for Python<3 compatibility).
- __str__(self): returns a string representing the object.
