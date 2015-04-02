# -*- coding: utf-8 -*-


def get(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        return None
