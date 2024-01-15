from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    students = Student.objects.all()

    for student in students:
        print(student.teachers.all())
        pass
    template = 'school/students_list.html'
    context = {'students': students}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
