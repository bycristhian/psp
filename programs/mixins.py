
# Django
from django.http.response import Http404, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

# Models
from programs.models import Program

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsOwnerProgram(BasePermission):

    def has_object_permission(self, request, view, obj):

        if obj.program.programmer != request.user:
            return False
        return True


class OwnerReportPIPMixin():

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('users:login'))

        if self.get_object().program.programmer != request.user:
            raise PermissionDenied()

        return super().dispatch(request, *args, **kwargs)


# Permission REST Framework
class IsProgrammerProgram(BasePermission):

    def __init__(self, program):
        self.program = program
        super().__init__()

    def has_permission(self, request, view):
        if self.program.programmer == request.user or request.user.get_profile.type_user == 'administrador':
            return True
        return False
        


# Mixin allow us verify if program exists
class ProgramExistMixin(object):

    def dispatch(self, request, *args, **kwargs):
        try:
            self.program = Program.objects.get(pk=kwargs['pk_program'])
        except Program.DoesNotExist:
            raise Http404("The program doesn't exists")

        return super().dispatch(request, *args, **kwargs)