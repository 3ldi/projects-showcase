from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Project, Message
from .forms import NewProjectForm, NewMessageForm


# Login view
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse(index))
        else:
            return render(request, "portfolio_app/login.html", {
                "error": "Invalid username and/or password."
            })
    else:
        return render(request, "portfolio_app/login.html")


# Logout view
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))


# Create homepage view.
def index(request):
    # Get all the projects from database
    projects = Project.objects.all()

    # Set up a paginator to display only 3 projects per page
    paginator = Paginator(projects, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = NewMessageForm(request.POST)
        # check if form is valid and save to database
        if form.is_valid:
            form.save()

            # Create an empty form
            form = NewMessageForm()
            return render(request, 'portfolio_app/index.html', {
                'projects': page_obj,
                'form': form
            })

        # If errors are present, return the form to user again
        else:
            return render(request, "portfolio_app/index.html", {
                'form': form,
                'projects': page_obj
            })

    else:
        #  Render a blank form
        form = NewMessageForm()

        # Display existing objects on index page
        return render(request, 'portfolio_app/index.html', {
            'form': form,
            'projects': page_obj
        })


# Create a view for adding a new project
def new_project(request):

    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        # check if form is valid and save to database
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse(index))
        # If errors are present, return the form to user again
        else:
            return render(request, "portfolio_app/newproject.html", {
                'form': form
            })

    else:
        #  Render a blank form
        form = NewProjectForm()
        return render(request, "portfolio_app/newproject.html", {
            'form': form
        })


# Create a view for updating an existing record
def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'GET':
        form = NewProjectForm(instance=project)
        return render(request, "portfolio_app/update.html", {
            'project': project,
            'form': form
        })
    else:
        form = NewProjectForm(request.POST, request.FILES, instance=project)
        # check if form is valid and save to database
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('index'))
        # If errors are present, return the form to user again
        else:
            return render(request, "portfolio_app/update.html", {
                'form': form,
                'project': project
            })


# Create view to delete a project
def delete_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    project.delete()
    return HttpResponseRedirect(reverse(index))


# Create a view to get all messages
def messages_all(request):

    # Get all the projects from database
    messages = Message.objects.all().order_by('-timestamp')
    total_nr_msg = messages.count

    # Set up a paginator to display only 10 messages per page
    paginator = Paginator(messages, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Display existing objects on index page
    return render(request, 'portfolio_app/usermsgs.html', {
        'messages': page_obj,
        'total_nr_msg': total_nr_msg
    })


# Create view to delete a message
def delete_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    message.delete()
    return HttpResponseRedirect(reverse(messages_all))
