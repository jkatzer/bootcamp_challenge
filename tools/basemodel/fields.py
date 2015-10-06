from django.db.models import DateTimeField

class CreationDateTimeField(DateTimeField):
    """ 
    CreationDateTimeField
    By default, sets editable=False, blank=True, auto_now_add=True

    from Django-Extensions: 
    https://github.com/django-extensions/django-extensions/blob/master/django_extensions/db/fields/ 

    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('editable', False)
        kwargs.setdefault('blank', True)
        kwargs.setdefault('auto_now_add', True)
        DateTimeField.__init__(self, *args, **kwargs)

    def get_internal_type(self):
        return "DateTimeField"

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        # We'll just introspect ourselves, since we inherit.
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.DateTimeField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(CreationDateTimeField, self).deconstruct()
        if self.editable is not False:
            kwargs['editable'] = True
        if self.blank is not True:
            kwargs['blank'] = False
        if self.auto_now_add is not False:
            kwargs['auto_now_add'] = True
        return name, path, args, kwargs


class ModificationDateTimeField(CreationDateTimeField):
    """ 
    ModificationDateTimeField
    By default, sets editable=False, blank=True, auto_now=True
    Sets value to now every time the object is saved.

    from Django-Extensions: 
    https://github.com/django-extensions/django-extensions/blob/master/django_extensions/db/fields/ 
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('auto_now', True)
        DateTimeField.__init__(self, *args, **kwargs)

    def get_internal_type(self):
        return "DateTimeField"

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        # We'll just introspect ourselves, since we inherit.
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.DateTimeField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(ModificationDateTimeField, self).deconstruct()
        if self.auto_now is not False:
            kwargs['auto_now'] = True
        return name, path, args, kwargs