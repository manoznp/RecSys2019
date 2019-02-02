from django.db import models
from tinymce.models import HTMLField
from multiselectfield import MultiSelectField


class Destination(models.Model):
    title               = models.CharField(max_length=150, blank=False)
    slug                = models.CharField(max_length=100, blank=False)
    image               = models.FileField(upload_to="img", blank=False)
    content             = HTMLField(blank=False)
    temperature         = models.FloatField(blank=False, default="1")
    altitude            = models.FloatField(blank=False, default="1")
    difficulty          = models.FloatField(blank=False, default="1")
    security            = models.FloatField(blank=False, default="1")

    trekkingtype_choice = (
        ("Cycling","Cycling"),
        ("Walking", "Walking"),
        ("Biking", "Biking"),
        ("Peak Climbing", "Peak Climbing"),
        ("Others", "Others")
        )
    trekking_type=MultiSelectField(choices=trekkingtype_choice, default="Walking")

    destinationtype_choice = (
        ("Adventure","Adventure"),
        ("Pilgrims", "Pilgrims"),
        ("Waterbody", "Waterbody"),
        ("Himalayas", "Himalayas"),
        ("Nature Seeing", "Nature Seeing"),
        ("Others", "Others")
        )
    destinaton_type= MultiSelectField(choices=destinationtype_choice, default="Adventure")

    accomodationtype_choice = (
        ("Hotel","Hotel"),
        ("Teahouse", "Teahouse"),
        ("Motel", "Motel"),
        ("Himalayas", "Himalayas"),
        ("Tent", "Tent"),
        ("Homestay", "Homestay")
        )
    accomodation_type = MultiSelectField(choices=accomodationtype_choice, default="Hotel")
    latitude          = models.FloatField(blank=False, default="1")
    longitude         = models.FloatField(blank=False, default="1")
    act               = (("publish","Publish"),("draft", "Draft"))
    action            = models.CharField(max_length=50, choices=act, default="draft")

    def __str__(self):
        return self.title
