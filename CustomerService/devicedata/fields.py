from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            #No current value
            try:
                qs = self.model.objects.all()
                if self.for_fields:
                    #Filter respect objects with the same value of column for columns in "for_fields"
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    qs = qs.filter(**query)
                #Take order last element
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(OrderField,
                         self.pre_save(model_instance, add))
