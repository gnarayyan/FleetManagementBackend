from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=50)

class District(models.Model):
    name = models.CharField(max_length=50)
    province =  models.ForeignKey(Province, on_delete=models.CASCADE)
    

class Municipality(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=[('R', 'Rural Municipality (गाउँपालिका)'), ('m', 'Municipality (नगरपालिका)'), (
        'M', 'Metropolitan City (महानगरपालिका)'), ('S', 'Sub - Metropolitan City (उप-महानगरपालिका)')], default='m')
    district = models.ForeignKey(District, on_delete=models.CASCADE)




