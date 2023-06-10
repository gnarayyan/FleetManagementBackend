from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class District(models.Model):
    name = models.CharField(max_length=50)
    province =  models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    

class Municipality(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=[('R', 'Rural Municipality (गाउँपालिका)'), ('U', 'Urban Municipality (नगरपालिका)'), (
        'M', 'Metropolitan City (महानगरपालिका)'), ('S', 'Sub - Metropolitan City (उप-महानगरपालिका)')], default='R')
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name




