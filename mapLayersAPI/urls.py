from django.urls import path

from custom_rest_framework_mvt.views import mvt_view_factory

from mapLayersAPI.models import *
from dataAPI.models import HouseholdData

urlpatterns = [
    path("municipality.mvt/", mvt_view_factory(Rangeli)),
    path("river.mvt/", mvt_view_factory(River)),
    path("road.mvt/", mvt_view_factory(RoadPolygon)),
    path("places.mvt/", mvt_view_factory(Places)),
    path("bridge.mvt/", mvt_view_factory(Bridge)),
    path("landuse.mvt/", mvt_view_factory(Landuse)),
    path("institution.mvt/", mvt_view_factory(MunicipalService)),

    path("house.mvt/", mvt_view_factory(HouseholdData)),

]
