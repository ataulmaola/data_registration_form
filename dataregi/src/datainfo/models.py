from django.db import models
blood_choices=(('O+','O+'),('O-','O-'),('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'),)
batch_choices=(('1972','1972'),('1973','1973'),('1974','1974'),('1975','1975'),('1976','1976'),
              ('1977','1977'),('1978','1978'),('1979','1979'),('1980','1980'),('1981','1981'),
              ('1982','1982'),('1983','1983'),('1984','1984'),('1985','1985'),('1986','1986'),
              ('1987','1987'),('1988','1988'),('1989','1989'),('1990','1990'),('1991','1991'),
              ('1992','1992'),('1993','1993'),('1994','1994'),('1995','1995'),('1996','1997'),
              ('1998','1998'), ('1999','1999'), ('2000','2000'), ('2001','2001'), ('2002','2002'),
               ('2003','2003'), ('2004','2004'), ('2005','2005'), ('2006','2006'), ('2007','2007'), 
               ('2008','2008'), ('2009','2009'), ('2010','2010'), ('2011','2011'),('2012','2012'),
)
MALE='male'
FEMALE='female'
gender_choices=((MALE,"Male"),(FEMALE,'Female'),)
# Create your models here.
# This is for personal data
class DataRegistration(models.Model):
    first_name = models.CharField(max_length=30,help_text='Please Use Block Letter')
    last_name = models.CharField(max_length=30,help_text='Please Use Block Letter')
    birth_date = models.DateField()
    gender=models.CharField(max_length=7,choices=gender_choices,default=MALE)
    batch_number=models.CharField(max_length=5,choices=batch_choices,default='1972')
    email=models.EmailField()
    address=models.CharField(max_length=100,help_text='Please Use Block Letter')
    blood_gruoup=models.CharField(max_length=3,choices=blood_choices,default='O+')
    college=models.CharField(max_length=50,help_text='Please Use Block Letter')
    alma_mater=models.CharField(max_length=50,help_text='Please Use Block Letter')
    status=models.CharField(max_length=250,help_text='Please Use Block Letter')
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    def __str__(self):
        return ''.join([self.first_name,self.last_name])