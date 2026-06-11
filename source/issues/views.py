from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View
from .forms import IssueForm

from issues.models import Issue


class IssueView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issues"] = Issue.objects.all().order_by("created_at")
        return context

class IssueDetailView(TemplateView):
    template_name = "issue_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issue"] = get_object_or_404(Issue, pk=kwargs["pk"])
        return context


class IssueCreateView(View):
    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return render(request, 'issue_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("issue_list")
        return render(request, 'issue_create.html',{'form':form})

class IssueUpdateView(View):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(instance=issue)
        context = {'form': form}
        return render(request, 'issue_update.html', context)


    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_list', )

        return render(request,'issue_update.html',{'form': form})

class IssueDeleteView(View):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        return render(request, 'issue_confirm_delete.html', {'issue': issue})

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        issue.delete()
        return redirect('issue_list')

