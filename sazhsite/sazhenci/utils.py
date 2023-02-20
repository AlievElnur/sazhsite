from .models import *

menu = [{'title': "Каталог", 'url_name': 'home'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Контакты", 'url_name': 'kontakti'}
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        lefts = Left.objects.all()
        
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        
        context['menu'] = user_menu
        
        context['lefts'] = lefts
        if 'lef_selected' not in context:
            context['lef_selected'] = 0
        return context