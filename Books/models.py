from django.db import models
from django.db.models import Sum

class AuthorManager(models.Manager):
    def with_copies_sold(self):
        return self.annotate(copies_sold=Sum('book__copies_sold'))

class Author(models.Model):
    name = models.CharField(max_length=200)    

    objects = AuthorManager()  # Use the custom manager
    
    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copies_sold = models.PositiveIntegerField()
    def __str__(self):
        return self.title


#In the views part or wherever you wish to run your query set
authors_with_copies_sold = Author.objects.annotate(total_copies_sold=Sum('book__copies_sold'))
for author in authors_with_copies_sold:
    print(f"Author: {author.name}, Copies Sold: {author.total_copies_sold}")
