from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Message

from .forms import MessageForm


@login_required
def inbox(request):

    messages = Message.objects.filter(
        receiver=request.user,
        is_archived=False
    ).order_by('-created_at')

    return render(
        request,
        'messaging/inbox.html',
        {'messages': messages}
    )


@login_required
def send_message(request):

    if request.method == 'POST':

        form = MessageForm(request.POST)

        if form.is_valid():

            message = form.save(commit=False)

            message.sender = request.user

            message.save()
            messages.success(request, 'Message sent successfully.')

            return redirect('inbox')

    else:

        form = MessageForm()

    return render(
        request,
        'messaging/send_message.html',
        {'form': form}
    )


@login_required
def archive_message(request, message_id):

    message = get_object_or_404(
        Message,
        id=message_id,
        receiver=request.user
    )

    message.is_archived = True

    message.save()
    messages.success(request, 'Message archived.')

    return redirect('inbox')