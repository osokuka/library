from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Member, Process
from .forms import MemberForm, ProcessForm

# Create your views here.

class MemberCreateView(View):
    form_class = MemberForm
    template_name = 'members/member_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            member = form.save()
            return redirect('member-detail', pk=member.pk)
        return render(request, self.template_name, {'form': form})


class MemberUpdateView(View):
    model = Member
    form_class = MemberForm
    template_name = 'members/member_form.html'

    def get_object(self, pk):
        return self.model.objects.get(pk=pk)

    def get(self, request, *args, **kwargs):
        member = self.get_object(kwargs['pk'])
        form = self.form_class(instance=member)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        member = self.get_object(kwargs['pk'])
        form = self.form_class(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member-detail', pk=member.pk)
        return render(request, self.template_name, {'form': form})


class MemberListView(ListView):
    model = Member
    template_name = 'members/member_list.html'
    context_object_name = 'members'


class MemberDetailView(DetailView):
    model = Member
    template_name = 'members/member_detail.html'
    context_object_name = 'member'


class ProcessCreateView(View):
    form_class = ProcessForm
    template_name = 'members/process_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            process = form.save()
            return redirect('process-detail', pk=process.pk)
        return render(request, self.template_name, {'form': form})


class ProcessUpdateView(View):
    model = Process
    form_class = ProcessForm
    template_name = 'members/process_form.html'

    def get_object(self, pk):
        return self.model.objects.get(pk=pk)

    def get(self, request, *args, **kwargs):
        process = self.get_object(kwargs['pk'])
        form = self.form_class(instance=process)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        process = self.get_object(kwargs['pk'])
        form = self.form_class(request.POST, instance=process)
        if form.is_valid():
            form.save()
            return redirect('process-detail', pk=process.pk)
        return render(request, self.template_name, {'form': form})


class ProcessListView(ListView):
    model = Process
    template_name = 'members/process_list.html'
    context_object_name = 'processes'


class ProcessDetailView(DetailView):
    model = Process
    template_name = 'members/process_detail.html'
    context_object_name = 'process'
