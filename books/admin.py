from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from books.resources import BookResource 

# Register your models here.
from books.models import Book_Issue_Details , Book , Employee


class EmployeeAdmin(admin.ModelAdmin):
	model = Employee
	list_display = ('employee_name','team')


class BookIssueAdminInline(admin.TabularInline):
	model = Book_Issue_Details
	# fk_name = 'Book'
	readonly_fields = ('book','book_issued_to','status','date_of_issue','date_of_return')
	list_display = ('book','book_issued_to','status','date_of_issue','date_of_return')
	actions = None
	extra = 0

	def has_delete_permission(self,request,obj=None):
		return False

class BookIssueAdmin(admin.ModelAdmin):
	list_display = ('book','book_issued_to','status','date_of_issue','date_of_return')

class BookAdmin(ImportExportModelAdmin):
	
	model = Book
	resource_class = BookResource
	list_display =  ('name','author','inventory_count','price')
	inlines = [BookIssueAdminInline]






admin.site.register(Book,BookAdmin)
admin.site.register(Book_Issue_Details, BookIssueAdmin)
admin.site.register(Employee, EmployeeAdmin)
