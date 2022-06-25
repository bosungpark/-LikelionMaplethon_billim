from django import forms
from ..models.solution_model import Solution

class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['title', 'content', 'img']