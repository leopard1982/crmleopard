from django.db import models

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=100,null=False,blank=False)
	last_name = models.CharField(max_length=100,null=False,blank=False)
	address = models.CharField(max_length=200,null=False,blank=False)
	city = models.CharField(max_length=100,null=False,blank=False)
	state = models.CharField(max_length=100,null=False,blank=False)
	province = models.CharField(max_length=100,null=False,blank=False) 
	kode_pos = models.CharField(max_length=100,null=False,blank=False)
	email = models.CharField(max_length=100,null=False,blank=False)
	phone = models.CharField(max_length=100,null=False,blank=False)
	created_by = models.CharField(max_length=100,default="")

	def __str__(self):
		return "%s %s"%(self.first_name,self.last_name)

	class Meta:
		ordering = ['first_name','last_name']
		unique_together=['first_name','last_name']