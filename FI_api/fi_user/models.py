from django.db import models

# Create your models here.
# class RegUser(models.Model):
#     id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     username = models.CharField(db_column='userName', max_length=100)  # Field name made lowercase.
#     at_created = models.TimeField(db_column='at_Created')  # Field name made lowercase.
#     at_modified = models.TimeField()
#     mobile_no = models.BigIntegerField()
#     password = models.CharField(max_length=256)
#
#     class Meta:
#         managed = False
#         db_table = 'reg_user'