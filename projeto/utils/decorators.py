from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.urls import reverse

class LoginRequiredMixin(object):
    @classmethod
    def as_view(self, **initkwargs):
        view = super(LoginRequiredMixin, self).as_view(**initkwargs)
        return login_required(view)

class StaffRequiredMixin(object):
    """
    View mixin which requires that the authenticated user is a staff member
    (i.e. `is_staff` is True).
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.tipo == 'ADMINISTRADOR':
            messages.error(
                request,
                'Você não tem permissão para acessar esta área.'
                'requested operation.')
            return redirect('home')
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class ProfessorRequiredMixin(object):
    """
    View mixin which requires that the authenticated user is a staff member
    (i.e. `is_staff` is True).
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.tipo == 'PROFESSOR':
            messages.error(
                request,
                'Você não tem permissão para acessar esta área.'
                'requested operation.')
            return redirect('home')
        return super(ProfessorRequiredMixin, self).dispatch(request,*args, **kwargs)
