from django.test import TestCase

# Create your tests here.

from .models import Location,Category,Image

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Location(location_name="nyungwe")
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nyungwe,Location))
    # Testing Save Method
    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)