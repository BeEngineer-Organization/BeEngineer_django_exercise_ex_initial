from django.shortcuts import render, redirect
from .models import Topic, Message, Comment
from .forms import MessageForm, CommentForm
from django.db.models import Count, OuterRef, Subquery

def index(request):
    TOPIC_LIST = Topic.objects.all()
    return render(request, "forum/index.html", {"topics": TOPIC_LIST})

def forum(request, topic):

    topic = Topic.objects.get(name=topic)
    subquery = Comment.objects.filter(message=OuterRef('id')).order_by('-created_at')
    messages = (
        Message.objects.filter(topic=topic)
        .annotate(
            reply_num=Count("comment"),
            latest_reply_date=Subquery(subquery.values("created_at")[:1]),
        )
        .prefetch_related("tag", "comment")
        .order_by("created_at")
    )

    if request.method == "POST":

        if "message" in request.POST:

            message_form = MessageForm(request.POST)

            if message_form.is_valid():
                message_form.instance.topic = topic
                message = message_form.save()
                for tag in message_form.cleaned_data["tag"]:
                    message.tag.add(tag)

        elif "comment" in request.POST:

            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():

                message_id = request.POST["comment"]
                message = Message.objects.get(id=message_id)

                comment_form.instance.message = message
                comment_form.save()

        return redirect('forum:forum', topic=topic.name)

    message_form = MessageForm()
    comment_form = CommentForm()

    context = {
        "messages": messages,
        "topic": topic,
        "message_form": message_form,
        "comment_form": comment_form,
    }

    return render(request, "forum/forum.html", context)