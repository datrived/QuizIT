from __future__ import unicode_literals

from django.db import models
from account import models as account_models
from instructor import models as instructor_models
from datetime import datetime

class Student_Answers(models.Model):
	student = models.ForeignKey( account_models.Student_Info, on_delete=models.CASCADE )
	question = models.ForeignKey( instructor_models.MCQ_Question, on_delete=models.CASCADE )
	selAnswer = models.CharField(max_length=200)
	correctFlag = models.IntegerField(default = 0) # 0: Wrong, 1: Correct
	recFlag = models.IntegerField(default = 0)
	numCorrectAttempts = models.IntegerField(default = 0)
	numAttempts = models.IntegerField(default = 0)
	answerSequence = models.CharField(max_length=500)
	# X is entered as this column was added later

class Student_Explanations(models.Model):
	student = models.ForeignKey( account_models.Student_Info, on_delete=models.CASCADE )
	question = models.ForeignKey( instructor_models.MCQ_Question, on_delete=models.CASCADE )
	explanationText = models.CharField(max_length=1000, default='')
	score = models.IntegerField(default=0)
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)
	postTimeStamp = models.DateTimeField(default=datetime.now, blank=True)

class Student_Recommendations(models.Model):
	student = models.ForeignKey( account_models.Student_Info, on_delete=models.CASCADE )
	question = models.ForeignKey( instructor_models.MCQ_Question, on_delete=models.CASCADE )
	recommendation = models.ForeignKey( instructor_models.Recommendations, on_delete=models.CASCADE )
	voteFlag = models.IntegerField(default = 0) # 0: Not voted, 1: Upvote, 2: Downvote

class Student_Answers_ActivityLog(models.Model):
	student = models.ForeignKey( account_models.Student_Info, on_delete=models.CASCADE )
	question = models.ForeignKey( instructor_models.MCQ_Question, on_delete=models.CASCADE )
	activity = models.CharField(max_length=1000, default='')
	source = models.CharField(max_length=200, default = 'Old') # 'List'/'Calendar/Todaysquiz'
	answerFlag = models.IntegerField(default=0) # 0: did not answer, 1: answered correctly 2: Incorrect answer
	activityTimeStamp = models.DateTimeField(default=datetime.now, blank=True)
	
class Student_Answer_Log(models.Model):
	student = models.ForeignKey( account_models.Student_Info )
	question = models.ForeignKey( instructor_models.MCQ_Question)
	activityFK = models.ForeignKey( Student_Answers_ActivityLog , default=None)
	answer = models.CharField(max_length=200)
	answerFlag = models.IntegerField(default=0) # 2: incorrect, 1: correct
	answerTimestamp = models.DateTimeField(default=datetime.now, blank=True)

class Student_Marks(models.Model):
	student = models.ForeignKey( account_models.Student_Info, on_delete=models.CASCADE )
	numQues = models.IntegerField(default = 0)
	numEasyQues = models.IntegerField(default = 0)
	numModerateQues = models.IntegerField(default = 0)
	numHardQues = models.IntegerField(default = 0)
	numCorrAns = models.IntegerField(default = 0)
	numEasyCorrAns = models.IntegerField(default = 0)
	numModerateCorrAns = models.IntegerField(default = 0)
	numHardCorrAns = models.IntegerField(default = 0)
	totMarks = models.IntegerField(default = 0)
	marks = models.IntegerField(default = 0)
	bonus = models.IntegerField(default = 0)
	currStreak = models.IntegerField(default = 0)
	streak05 = models.IntegerField(default = 0)
	streak10 = models.IntegerField(default = 0)
	streak20 = models.IntegerField(default = 0)
	rank = models.IntegerField(default = 0)
	badge = models.CharField(max_length=200)
	


class Student_Activity_Log_WithScroll(models.Model):
	student = models.ForeignKey( account_models.Student_Info, related_name='fk_1' )
	question = models.IntegerField(default = 0) 
	activity_type = models.IntegerField(default = 0) # possible: 0 - today quiz,  1- retry, 2- review,3 - List , 4- Dash
	blur_type = models.IntegerField(default = 0)
	timestamp = models.DateTimeField(blank=True, null = True)
	time = models.BigIntegerField(default = 0)
	browser = models.IntegerField(default = 0) # 0-chrome, 1-firefox, 2 - safari
	scrollTimestamp = models.DateTimeField(blank=True, null=True)
	scrollPoints = models.BigIntegerField(default = 0)
	commentPostTimestamp = models.DateTimeField(blank=True, null = True)
	answerPostTimeStamp = models.DateTimeField(blank=True, null = True)
	
	

'''	
class Dashboard_Activity_Log(models.Model):
	student = models.ForeignKey( account_models.Student_Info )
	activity_type = models.IntegerField(default = 0) # 0-dashboard, 1-list
	blur_type = models.IntegerField(default = 0)
	timestamp = models.DateTimeField(blank=True)
	time = models.BigIntegerField(default = 0) #in seconds
	browser = models.IntegerField(default = 0) # 0-chrome, 1-firefox, 2 - safari '''
	
