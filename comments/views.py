from django.shortcuts import render
from .models import Comment
from django.views.generic import ListView

# Create your views here.
class CommentListView(ListView):
    model = Comment
    
    
    def get(self, request, *args, **kwargs):
        return None
    
    def post(self, request, *args, **kwargs):
        return None
    
    
    
    
    