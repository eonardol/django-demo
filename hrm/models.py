from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AbsenceType(models.Model):
    code = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return "%s - %s" % (self.code,self.description)



class AbsenceRequest(models.Model):
    absence_type = models.ForeignKey(AbsenceType, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    ins_date = models.DateTimeField('data di inserimento')
    from_date = models.DateTimeField('data inizio')
    to_date = models.DateTimeField('data fine')
    total_days = models.IntegerField(default=0)
    total_hours = models.IntegerField(default=0)
    user_info = models.TextField()
    ABSENCE_REQUEST_STATUS = (
        ('TO_APPROVE', 'Da approvare'),
        ('CANCELED_BY_USER', 'Cancellata dal richiedente'),
        ('NOT_APPROVED', 'Non approvata'),
        ('APPROVED', 'Approvata'),
    )
    status = models.CharField(max_length=25, choices=ABSENCE_REQUEST_STATUS, default='TO_APPROVE')
    approver_info = models.TextField()
    def __str__(self):
        return "%s - in '%s' dal '%s' al '%s'" % (self.user,self.absence_type,self.from_date,self.to_date)
