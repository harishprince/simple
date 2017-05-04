from django.db import models


class Details(models.Model):
	name = models.CharField(max_length=60)
	surname = models.CharField(max_length=40)
	address = models.CharField(max_length=50)
	phoneno = models.IntegerField()
	emailid = models.EmailField()
	
	
	

