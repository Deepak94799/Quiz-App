from django.shortcuts import render, redirect
from .models import Question
import random

def dashboard(request):
    attempted = request.session.get('attempted', 0)
    correct = request.session.get('correct', 0)
    percentage = (correct / attempted * 100) if attempted > 0 else 0
    return render(request, 'dashboard.html', {
        'attempted': attempted,
        'correct': correct,
        'percentage': percentage
    })

def take_quiz(request):
    questions = Question.objects.all()
    if not questions:
        return render(request, 'quiz.html', {'error': 'No questions available.'})
    question = random.choice(questions)
    return render(request, 'quiz.html', {'question': question})

def submit_answer(request):
    if request.method == 'POST':
        question_id = request.POST['question_id']
        selected_option = request.POST['option']
        question = Question.objects.get(id=question_id)
        correct = selected_option == question.correct_option
        request.session['attempted'] = request.session.get('attempted', 0) + 1
        if correct:
            request.session['correct'] = request.session.get('correct', 0) + 1
            message = "Hooray! You are correct!"
        else:
            message = "Sorry! That’s incorrect."
        return render(request, 'feedback.html', {
            'correct': correct,
            'message': message,
            'question': question
        })
    return redirect('dashboard')