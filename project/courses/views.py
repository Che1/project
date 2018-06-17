# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from project.courses.models import TreeItem
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render


class CatalogRootView(TemplateView):
    """ Срендерить корневую страницу курсов """
    template_name = 'courses/root.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogRootView, self).get_context_data(**kwargs)
        context['courses'] = TreeItem.objects.filter(show=True, level=0)
        context['object'] = {"title": "Курсы"}
        return context


def catalog_item(request, path=None):
    """ Идентифицировать по url элемент курса и срендерить его
        или вернуть 404 """
    if path.endswith('/'):
        path = path[:-1]
    slug = path.split('/')[-1]
    treeitem = None
    items = TreeItem.objects.filter(slug=slug)
    if not items.exists():
        return Http404
    else:
        if len(items) == 1:
            treeitem = items[0]
        else:
            for item in items:
                if item.get_complete_slug() == path:
                    treeitem = item

    if treeitem.level == 0:
        template = "courses/courseitem.html"
    else:
        template = "courses/treeitem.html"

    # Если у элемента курса нет контента и это не курс то редиркетить на 1 дочерний элемент(если они есть)
    if not treeitem.content and treeitem.level > 0:
        children = treeitem.get_children()
        if children.exists():
            return redirect(children[0])

    context = {
        "object": treeitem,
    }
    return render(request, template, context)
