# from django.db import models

# Create your models here.
# from django.db import models
from django.contrib.gis.db import models
from custom_rest_framework_mvt.managers import MVTManager


class Rangeli(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid_1 = models.BigIntegerField(blank=True, null=True)
    dcode = models.BigIntegerField(blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    dan = models.CharField(max_length=50, blank=True, null=True)
    das = models.BigIntegerField(blank=True, null=True)
    gapa_napa = models.CharField(max_length=50, blank=True, null=True)
    type_gn = models.CharField(max_length=50, blank=True, null=True)
    gn_code = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    new_ward_n = models.BigIntegerField(blank=True, null=True)
    ddgnww = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    center = models.CharField(max_length=50, blank=True, null=True)
    state_code = models.BigIntegerField(blank=True, null=True)
    ddgn = models.BigIntegerField(blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    ddgn_code = models.BigIntegerField(blank=True, null=True)
    wardnumber = models.BigIntegerField(blank=True, null=True)
    zone = models.CharField(max_length=50, blank=True, null=True)
    area_sq_km = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    studyarea = models.CharField(max_length=1, blank=True, null=True)
    remarks = models.CharField(max_length=50, blank=True, null=True)
    total_popu = models.BigIntegerField(blank=True, null=True)
    male_popu = models.BigIntegerField(blank=True, null=True)
    female_pop = models.BigIntegerField(blank=True, null=True)
    vcode = models.BigIntegerField(blank=True, null=True)
    total_abse = models.BigIntegerField(blank=True, null=True)
    male_abse = models.BigIntegerField(blank=True, null=True)
    female_abs = models.BigIntegerField(blank=True, null=True)
    orig_fid = models.BigIntegerField(blank=True, null=True)
    house = models.BigIntegerField(blank=True, null=True)
    household = models.BigIntegerField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = False
        db_table = 'rangeli'

class Bridge(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    submission = models.DateField(blank=True, null=True)
    munucipali = models.CharField(max_length=254, blank=True, null=True)
    ward = models.BigIntegerField(blank=True, null=True)
    chowk = models.CharField(max_length=254, blank=True, null=True)
    service = models.CharField(max_length=254, blank=True, null=True)
    service_ot = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    remark = models.CharField(max_length=254, blank=True, null=True)
    geometry_l = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    geometry_1 = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    geometry_a = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    geometry_2 = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    photo = models.CharField(max_length=254, blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    today = models.CharField(max_length=254, blank=True, null=True)
    username = models.CharField(max_length=254, blank=True, null=True)
    audit = models.CharField(max_length=254, blank=True, null=True)
    instanceid = models.CharField(max_length=254, blank=True, null=True)
    key = models.CharField(max_length=254, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = False
        db_table = 'bridge'

class Contour(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    length = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    contour = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    index = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = False
        db_table = 'contour'

class Landuse(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    level1 = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=50, blank=True, null=True)
    area_h = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    luclass = models.CharField(max_length=50, blank=True, null=True)
    subclass = models.CharField(max_length=50, blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = False
        db_table = 'landuse'


class MunicipalService(models.Model):
    gid = models.IntegerField(primary_key=True)
    municipality = models.CharField(max_length=254, blank=True, null=True)
    ward = models.BigIntegerField(blank=True, null=True)
    chowk = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    remark = models.CharField(max_length=254, blank=True, null=True)
    photo = models.CharField(max_length=254, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    service = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    service_id = models.CharField(max_length=200, blank=True, null=True)

    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = False
        db_table = 'municipal_services'

class Places(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    area = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    perimeter = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    # vil81_1_field = models.DecimalField(db_column='vil81_1_', max_digits=100, decimal_places=100, blank=True, null=True)  # Field renamed because it ended with '_'.
    # vil81_1_id = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    label = models.CharField(max_length=30, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = True
        db_table = 'places'

class River(models.Model):
    gid = models.AutoField(primary_key=True)
    # objectid_1 = models.BigIntegerField(blank=True, null=True)
    # objectid = models.BigIntegerField(blank=True, null=True)
    # join_count = models.BigIntegerField(blank=True, null=True)
    target_fid = models.BigIntegerField(blank=True, null=True)
    riv_name = models.CharField(max_length=50, blank=True, null=True)
    fcode = models.BigIntegerField(blank=True, null=True)
    level = models.BigIntegerField(blank=True, null=True)
    basin_no = models.BigIntegerField(blank=True, null=True)
    gridcode = models.BigIntegerField(blank=True, null=True)
    num_spp = models.BigIntegerField(blank=True, null=True)
    fish_spp = models.CharField(max_length=254, blank=True, null=True)
    riv_name_l = models.CharField(max_length=50, blank=True, null=True)
    # migration = models.CharField(max_length=1, blank=True, null=True)
    # migration_field = models.CharField(db_column='migration_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    # migrate_lo = models.CharField(max_length=1, blank=True, null=True)
    # migrate_me = models.CharField(max_length=1, blank=True, null=True)
    # migrate_sh = models.CharField(max_length=1, blank=True, null=True)
    # antecedant = models.CharField(max_length=1, blank=True, null=True)
    # migration1 = models.BigIntegerField(blank=True, null=True)
    # migratio_1 = models.BigIntegerField(blank=True, null=True)
    resident = models.BigIntegerField(blank=True, null=True)
    not_rec = models.BigIntegerField(blank=True, null=True)
    endemic = models.BigIntegerField(blank=True, null=True)
    con_depend = models.BigIntegerField(blank=True, null=True)
    common = models.BigIntegerField(blank=True, null=True)
    con_depe_1 = models.BigIntegerField(blank=True, null=True)
    endangered = models.BigIntegerField(blank=True, null=True)
    vulnerable = models.BigIntegerField(blank=True, null=True)
    rare_threa = models.BigIntegerField(blank=True, null=True)
    pristine_r = models.BigIntegerField(blank=True, null=True)
    exotic_com = models.BigIntegerField(blank=True, null=True)
    exotic_unc = models.BigIntegerField(blank=True, null=True)
    wshed_num = models.BigIntegerField(blank=True, null=True)
    # shape_leng = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    # shape_le_1 = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = True
        db_table = 'river'

class RoadPolygon(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    level1 = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=50, blank=True, null=True)
    area_h = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    luclass = models.CharField(max_length=50, blank=True, null=True)
    subclass = models.CharField(max_length=50, blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=100, decimal_places=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = False
        db_table = 'road_polygon'
