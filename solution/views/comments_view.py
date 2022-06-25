from django.shortcuts import render, redirect, get_object_or_404
from ..models.solution_model import Solution
from ..models.comment_model import Comment
from ..forms.comment_form import CommentForm

def create_comment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.solution_id = Solution.objects.get(pk=id)
            comment.writer = request.user
            comment.save()
    return redirect('solution_detail', id)


def create_re_comment(request, id, comment_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.solution_id = Solution.objects.get(pk=id)
            comment.comment_id = Comment.objects.get(pk=comment_id)
            comment.writer = request.user
            comment.save()
    return redirect('solution_detail', id)


def update_comment(request, comment_id, id):
    my_com = Comment.objects.get(id=comment_id)
    com_form = CommentForm(instance=my_com)
    if request.method == "POST":
        update_form = CommentForm(request.POST, instance=my_com)
        if update_form.is_valid():
            update_form.save()
            return redirect('solution_detail', id)
    return render(request, 'solution_detail', {'com_form': com_form})


def delete_comment(request, comment_id, id):
    mycom = Comment.objects.get(id=comment_id)
    mycom.delete()

    return redirect('solution_detail', id)