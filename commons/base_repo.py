# -*- coding: utf-8 -*-


def get(model, pk):
    return model.objects.get(pk=pk)


def update(model, pk, **kwargs):
    model_object = get(model=model, pk=pk)
    all_fields = model_object._meta.get_all_field_names()
    pk_name = model_object._meta.pk.name
    # Don't allow to edit pk name
    try:
        all_fields.remove(pk_name)
        all_fields = set(all_fields)
    except ValueError:
        # No need to worry since pk is missing
        pass

    update_fields = []
    for field, value in kwargs.items():
        # unless fields are in model don't set attribute
        if field in all_fields:
            update_fields.append(field)
            setattr(model_object, field, value)

    if 'modified' in all_fields:
        update_fields.append('modified')

    model_object.save(update_fields=update_fields)
    return model_object


def create(model, **kwargs):
    return model.objects.create(**kwargs)


def filter(model, **kwargs):
    limit = kwargs.pop('limit', 20)
    offset = kwargs.pop('offset', 0)
    return model.objects.filter(**kwargs)[offset:limit]


def count(model, **kwargs):
    if kwargs:
        return model.objects.filter(**kwargs).count()
    return model.objects.count()


def delete(model, pk):
    return get(model=model, pk=pk).delete()
