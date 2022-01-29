from django.db import models

# Create your models here.
class APP(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    detail = models.TextField(max_length=1000, default='')
    image = models.ImageField(upload_to="images/")
    # suggested that all models have by default a create and update date capture for filtering or sorting
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.summary
#
#     def detail_summary(self):
#         return self.detail[:100]
#
#     class Meta:
#         ordering = ['-updated_date']
#
# class JobAdmin(admin.ModelAdmin):
#     readonly_fields = ('id',)
#     list_display = ('id', 'title', 'summary', 'created_date', 'updated_date')
#     fields = ('id', 'title', 'summary', 'detail', 'created_date', 'updated_date', 'image')