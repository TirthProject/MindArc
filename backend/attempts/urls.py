from django.urls import path
from .views import VerifyQuizCodeView, GetQuizQuestionsView , SaveAttemptView , GetRecentQuizzesView, GetAttemptResultView
urlpatterns = [
    path("verify-code/", VerifyQuizCodeView.as_view(), name="verify-quiz-code"),
    path("<int:quiz_id>/questions/", GetQuizQuestionsView.as_view(), name="get-quiz-questions"),
    path("save/", SaveAttemptView.as_view(), name="save-attempt"),
    path("recent-quizzes/", GetRecentQuizzesView.as_view(), name="student_attempts"),
    path("result/<int:attempt_id>/", GetAttemptResultView.as_view(), name="get_attempt_result"), 
]
