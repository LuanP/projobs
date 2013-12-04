from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View

from .models import User


class AtivarView(View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(
            User, activation_key=self.kwargs.get('activation_key'),
            is_active=False,
        )
        user.is_active = True
        user.save()
        messages.success(request, 'Conta ativada com sucesso!')
        return redirect('home')
