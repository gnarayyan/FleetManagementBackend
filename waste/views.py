from rest_framework import viewsets
from .models import Waste
from .serializers import WasteSerializer


class WasteViewSet(viewsets.ModelViewSet):
    '''
    This is an API endpoint for the Waste model with standard CRUD operations available at the following endpoints:

GET / api / wastes /  - Retrieves a list of all waste objects
GET / api / wastes / {id} / - Retrieves a specific waste object by ID
POST / api / wastes /  - Creates a new waste object
PUT / api / wastes / {id} / - Updates a specific waste object by ID
DELETE / api / wastes / {id} / - Deletes a specific waste object by ID
    '''
    queryset = Waste.objects.all()
    serializer_class = WasteSerializer
