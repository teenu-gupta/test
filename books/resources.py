from import_export import resources
from books.models import Book , Book_Issue_Details , Employee

class BookResource(resources.ModelResource):
	class Meta:
		model = Book
		fields = ('name','author','inventory','price')
