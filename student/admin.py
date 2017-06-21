# -*- coding: utf-8 -*-
from django.contrib import admin
from account.models import Student_Info
from student.models import Student_Answers_ActivityLog,  Student_Activity_Log_WithScroll, Student_Explanations, Student_Answer_Log, Student_Answers
import csv
from django.http import HttpResponse
from django.conf import settings
from datetime import date

#################################################################################################
# Student Answers Actvitiy log

class Student_Answers_ActivityLogAdmin(admin.ModelAdmin):

	def has_add_permission(self, request):
		return False
	
	def get_actions(self, request):
		actions = super(Student_Answers_ActivityLogAdmin, self).get_actions(request)
		del actions['delete_selected']
		return actions

	list_filter = ('question__course', 'activityTimeStamp', 'activity','source')

	actions = ['download_csv']
	list_display = ['student', 'question', 'activity','source','answerFlag',]
	def download_csv(self, request, queryset):
		f = open(settings.BASE_DIR+"/static/"+"some.csv", 'wb')
		writer = csv.writer(f)
		writer.writerow(['student', 'question', 'activity','source','answerFlag','activityTimeStamp'])

		for s in queryset:
			writer.writerow([s.student.id, s.question.id, s.activity,s.source,s.answerFlag,s.activityTimeStamp])

		f.close()

		f = open(settings.BASE_DIR+"/static/"+"some.csv", 'r')
		response = HttpResponse(f, content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=Activity-Log-'+str(date.today())+'.csv'
		return response

admin.site.register(Student_Answers_ActivityLog, Student_Answers_ActivityLogAdmin)

#################################################################################################
# Student Answers

class Student_AnswersAdmin(admin.ModelAdmin):

	def has_add_permission(self, request):
		return False
	
	def get_actions(self, request):
		actions = super(Student_AnswersAdmin, self).get_actions(request)
		del actions['delete_selected']
		return actions

	list_filter = ('question__course',)

	actions = ['download_csv']
	list_display = ['student', 'question', 'numCorrectAttempts','numAttempts']
	def download_csv(self, request, queryset):
		f = open(settings.BASE_DIR+"/static/"+"some.csv", 'wb')
		writer = csv.writer(f)
		writer.writerow(['student', 'question', 'numCorrectAttempts','numAttempts'])

		for s in queryset:
			writer.writerow([s.student.id, s.question.id, s.numCorrectAttempts ,s.numAttempts])

		f.close()

		f = open(settings.BASE_DIR+"/static/"+"some.csv", 'r')
		response = HttpResponse(f, content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=Answers-Aggregate-'+str(date.today())+'.csv'
		return response

admin.site.register(Student_Answers, Student_AnswersAdmin)

#################################################################################################
# Student Answer Log

class Student_Answer_LogAdmin(admin.ModelAdmin):

	def has_add_permission(self, request):
		return False
	
	def get_actions(self, request):
		actions = super(Student_Answer_LogAdmin, self).get_actions(request)
		del actions['delete_selected']
		return actions
	
	list_filter = ('question__course','answerTimestamp')

	actions = ['download_csv']	
	list_display = ['student', 'question', 'activityFK','answer','answerFlag','answerTimestamp']
	def download_csv(self, request, queryset):
			f = open(settings.BASE_DIR+"/static/"+"some.csv", 'wb')
			writer = csv.writer(f)
			writer.writerow(['student', 'question', 'activityFK','answer','answerFlag','answerTimestamp'])

			for s in queryset:
				writer.writerow([s.student.id, s.question.id, s.activityFK.id, s.answer, s.answerFlag, s.answerTimestamp])

			f.close()

			f = open(settings.BASE_DIR+"/static/"+"some.csv", 'r')
			response = HttpResponse(f, content_type='text/csv')
			response['Content-Disposition'] = 'attachment; filename=Answer-History-Log-'+str(date.today())+'.csv'
			return response

admin.site.register(Student_Answer_Log, Student_Answer_LogAdmin)

#################################################################################################
# Student Explanation log

class Student_ExplanationsAdmin(admin.ModelAdmin):
	
	list_filter = ('question__course', 'postTimeStamp')

	def has_add_permission(self, request):
		return False
	
	def get_actions(self, request):
		actions = super(Student_ExplanationsAdmin, self).get_actions(request)
		del actions['delete_selected']
		return actions
	
	actions = ['download_csv']	
	list_display = ['student', 'question', 'explanationText','score','upvotes','downvotes','postTimeStamp']
	def download_csv(self, request, queryset):
		f = open(settings.BASE_DIR+"/static/"+"some.csv", 'wb')
		writer = csv.writer(f)
		writer.writerow(['student', 'question', 'explanationText','score','upvotes','downvotes','postTimeStamp'])

		for s in queryset:
			writer.writerow([s.student.id, s.question.id, unicode(s.explanationText).encode("utf-8"),s.score,s.upvotes,s.downvotes,s.postTimeStamp])
		f.close()

		f = open(settings.BASE_DIR+"/static/"+"some.csv", 'r')
		response = HttpResponse(f, content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=Student-Notes-'+str(date.today())+'.csv'
		return response

admin.site.register(Student_Explanations, Student_ExplanationsAdmin)



################################## Time Recording admin ################################

class Student_Activity_Log_WithScrollAdmin(admin.ModelAdmin):
	
	list_filter = ('question', 'activity_type', 'browser')

	def has_add_permission(self, request):
		return False
	
	def get_actions(self, request):
		actions = super(Student_Activity_Log_WithScrollAdmin, self).get_actions(request)
		del actions['delete_selected']
		return actions
	
	actions = ['download_csv']	
	list_display = ['student', 'question', 'activity_type','blur_type','timestamp','time','browser', 'scrollTimestamp', 'scrollPoints', 'commentPostTimestamp','answerPostTimeStamp']
	def download_csv(self, request, queryset):
		f = open(settings.BASE_DIR+"/static/"+"some.csv", 'wb')
		writer = csv.writer(f)
		writer.writerow(['student', 'question', 'activity_type','blur_type','timestamp','time','browser', 'scrollTimestamp', 'scrollPoints', 'commentPostTimestamp','answerPostTimeStamp'])

		for s in queryset:
			writer.writerow([s.student.id, s.question.id, s.activity_type,s.blur_type,s.timestamp,s.time, s.browser, s.scrollTimestamp, s.scrollPoints, s.commentPostTimestamp,s.answerPostTimeStamp] )
		f.close()

		f = open(settings.BASE_DIR+"/static/"+"some.csv", 'r')
		response = HttpResponse(f, content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=Student-Time-Activity-'+str(date.today())+'.csv'
		return response

admin.site.register(Student_Activity_Log_WithScroll, Student_Activity_Log_WithScrollAdmin)


'''
class Dashboard_Activity_LogAdmin(admin.ModelAdmin):
	
	list_filter = ()

	def has_add_permission(self, request):
		return False
	
	def get_actions(self, request):
		actions = super(Dashboard_Activity_LogAdmin, self).get_actions(request)
		del actions['delete_selected']
		return actions
	
	actions = ['download_csv']	
	list_display = ['student', 'activity_type', 'blur_type','timestamp', 'time', 'browser']
	def download_csv(self, request, queryset):
		f = open(settings.BASE_DIR+"/static/"+"some.csv", 'wb')
		writer = csv.writer(f)
		writer.writerow(['student','activity_type', 'blur_type','timestamp', 'time', 'browser'])

		for s in queryset:
			writer.writerow([s.student.id, s.activity_type, s.blur_type, s.timestamp, s.time, s.browser ])
		f.close()

		f = open(settings.BASE_DIR+"/static/"+"some.csv", 'r')
		response = HttpResponse(f, content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=Student-Dashboard-Activity-'+str(date.today())+'.csv'
		return response

admin.site.register(Dashboard_Activity_Log, Dashboard_Activity_LogAdmin) '''
