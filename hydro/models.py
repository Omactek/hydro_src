# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AntyglPritok(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)
    wt_wl_degc = models.FloatField(db_column='WT_WL_degC', blank=True, null=True) 
    ec_lin_micros_cm = models.FloatField(db_column='EC_lin_microS/cm', blank=True, null=True)
    ec_nonlin_micros_cm = models.FloatField(db_column='EC_nonlin_microS/cm', blank=True, null=True)
    ec_uncomp_micros_cm = models.FloatField(db_column='EC_uncomp_microS/cm', blank=True, null=True)
    wt_degc = models.FloatField(db_column='WT_degC', blank=True, null=True)
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'antygl_pritok'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BreznickyPotok(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    gr_w_m2 = models.FloatField(db_column='GR_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    at_degc = models.FloatField(db_column='AT_degC', blank=True, null=True)  # Field name made lowercase.
    rh_pct = models.FloatField(db_column='RH_pct', blank=True, null=True)  # Field name made lowercase.
    ws_m_s = models.FloatField(db_column='WS_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wd_deg = models.FloatField(db_column='WD_deg', blank=True, null=True)  # Field name made lowercase.
    rx_mv = models.FloatField(db_column='RX_mV', blank=True, null=True)  # Field name made lowercase.
    wt_rx_degc = models.FloatField(db_column='WT_RX_degC', blank=True, null=True)  # Field name made lowercase.
    p_mm = models.FloatField(db_column='P_mm', blank=True, null=True)  # Field name made lowercase.
    ph = models.FloatField(db_column='pH_-', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ec_lin_micros_cm = models.FloatField(db_column='EC_lin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_nonlin_micros_cm = models.FloatField(db_column='EC_nonlin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_uncomp_micros_cm = models.FloatField(db_column='EC_uncomp_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wt_ec_degc = models.FloatField(db_column='WT_EC_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'breznicky_potok'


class CernyPotok(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    rx_mv = models.FloatField(db_column='RX_mV', blank=True, null=True)  # Field name made lowercase.
    wt_red_degc = models.FloatField(db_column='WT_red_degC', blank=True, null=True)  # Field name made lowercase.
    ph = models.FloatField(db_column='pH_-', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wt_ph_degc = models.FloatField(db_column='WT_pH_degC', blank=True, null=True)  # Field name made lowercase.
    wt_degc = models.FloatField(db_column='WT_degC', blank=True, null=True)  # Field name made lowercase.
    ec_lin_micros_cm = models.FloatField(db_column='EC_lin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_nonlin_micros_cm = models.FloatField(db_column='EC_nonlin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_uncomp_micros_cm = models.FloatField(db_column='EC_uncomp_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    p_mm = models.FloatField(db_column='P_mm', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cerny_potok'


class CikanskyPotok(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    ph = models.FloatField(db_column='pH_-', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wt_degc = models.FloatField(db_column='WT_degC', blank=True, null=True)  # Field name made lowercase.
    ec_lin_micros_cm = models.FloatField(db_column='EC_lin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_nonlin_micros_cm = models.FloatField(db_column='EC_nonlin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_uncomp_micros_cm = models.FloatField(db_column='EC_uncomp_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wt_ec_degc = models.FloatField(db_column='WT_EC_degC', blank=True, null=True)  # Field name made lowercase.
    wt_ph_degc = models.FloatField(db_column='WT_pH_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cikansky_potok'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Filipohutsky(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    wt_degc = models.FloatField(db_column='WT_degC', blank=True, null=True)  # Field name made lowercase.
    ec_lin_micros_cm = models.FloatField(db_column='EC_lin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_nonlin_micros_cm = models.FloatField(db_column='EC_nonlin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_uncomp_micros_cm = models.FloatField(db_column='EC_uncomp_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wt_ec_degc = models.FloatField(db_column='WT_EC_degC', blank=True, null=True)  # Field name made lowercase.
    ph = models.FloatField(db_column='pH_-', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'filipohutsky'


class HrabeciCesta(models.Model):
    at20_degc = models.FloatField(db_column='AT20_degC', blank=True, null=True)  # Field name made lowercase.
    rh20_pct = models.FloatField(db_column='RH20_pct', blank=True, null=True)  # Field name made lowercase.
    at_degc = models.FloatField(db_column='AT_degC', blank=True, null=True)  # Field name made lowercase.
    rh_pct = models.FloatField(db_column='RH_pct', blank=True, null=True)  # Field name made lowercase.
    ws_m_s = models.FloatField(db_column='WS_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hs_cm = models.FloatField(db_column='HS_cm', blank=True, null=True)  # Field name made lowercase.
    p_mm = models.FloatField(db_column='P_mm', blank=True, null=True)  # Field name made lowercase.
    ws_2_m_s = models.FloatField(db_column='WS_2_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sm10_pct = models.FloatField(db_column='SM10_pct', blank=True, null=True)  # Field name made lowercase.
    st10_degc = models.FloatField(db_column='ST10_degC', blank=True, null=True)  # Field name made lowercase.
    sm25_pct = models.FloatField(db_column='SM25_pct', blank=True, null=True)  # Field name made lowercase.
    st25_degc = models.FloatField(db_column='ST25_degC', blank=True, null=True)  # Field name made lowercase.
    sm60_pct = models.FloatField(db_column='SM60_pct', blank=True, null=True)  # Field name made lowercase.
    st60_degc = models.FloatField(db_column='ST60_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'hrabeci_cesta'


class HrebecnaMeteo(models.Model):
    p_mm = models.FloatField(db_column='P_mm', blank=True, null=True)  # Field name made lowercase.
    at_degc = models.FloatField(db_column='AT_degC', blank=True, null=True)  # Field name made lowercase.
    rh_pct = models.FloatField(db_column='RH_pct', blank=True, null=True)  # Field name made lowercase.
    hs_mm = models.FloatField(db_column='HS_mm', blank=True, null=True)  # Field name made lowercase.
    gr_w_m2 = models.FloatField(db_column='GR_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ws_m_s = models.FloatField(db_column='WS_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wd_deg = models.FloatField(db_column='WD_deg', blank=True, null=True)  # Field name made lowercase.
    gt05_degc = models.FloatField(db_column='GT05_degC', blank=True, null=True)  # Field name made lowercase.
    at50_degc = models.FloatField(db_column='AT50_degC', blank=True, null=True)  # Field name made lowercase.
    at20_degc = models.FloatField(db_column='AT20_degC', blank=True, null=True)  # Field name made lowercase.
    sm_neg60_pct = models.FloatField(db_column='SM60_pct', blank=True, null=True)  # Field name made lowercase.
    sm30_pct = models.FloatField(db_column='SM30_pct', blank=True, null=True)  # Field name made lowercase.
    sm15_pct = models.FloatField(db_column='SM15_pct', blank=True, null=True)  # Field name made lowercase.
    st_neg60_degc = models.FloatField(db_column='ST60_degC', blank=True, null=True)  # Field name made lowercase.
    st30_degc = models.FloatField(db_column='ST30_degC', blank=True, null=True)  # Field name made lowercase.
    st15_degc = models.FloatField(db_column='ST15_degC', blank=True, null=True)  # Field name made lowercase.
    at25_degc = models.FloatField(db_column='AT25_degC', blank=True, null=True)  # Field name made lowercase.
    at75_degc = models.FloatField(db_column='AT75_degC', blank=True, null=True)  # Field name made lowercase.
    at100_degc = models.FloatField(db_column='AT100_degC', blank=True, null=True)  # Field name made lowercase.
    grout_w_m2 = models.FloatField(db_column='GRout_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ws_2_m_s = models.FloatField(db_column='WS_2_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wd_2_deg = models.FloatField(db_column='WD_2_deg', blank=True, null=True)  # Field name made lowercase.
    wsmax_m_s = models.FloatField(db_column='WSmax_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wsmin_m_s = models.FloatField(db_column='WSmin_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'hrebecna_meteo'


class Javori(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    q_m3_s = models.FloatField(db_column='Q_m3/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_lin_micros_cm = models.FloatField(db_column='EC_lin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_nonlin_micros_cm = models.FloatField(db_column='EC_nonlin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wt_degc = models.FloatField(db_column='WT_degC', blank=True, null=True)  # Field name made lowercase.
    p_mm = models.FloatField(db_column='P_mm', blank=True, null=True)  # Field name made lowercase.
    at_degc = models.FloatField(db_column='AT_degC', blank=True, null=True)  # Field name made lowercase.
    sm_41_pct = models.FloatField(db_column='SM_41_pct', blank=True, null=True)  # Field name made lowercase.
    st_42_degc = models.FloatField(db_column='ST_42_degC', blank=True, null=True)  # Field name made lowercase.
    sm_43_pct = models.FloatField(db_column='SM_43_pct', blank=True, null=True)  # Field name made lowercase.
    st_44_degc = models.FloatField(db_column='ST_44_degC', blank=True, null=True)  # Field name made lowercase.
    sm_45_pct = models.FloatField(db_column='SM_45_pct', blank=True, null=True)  # Field name made lowercase.
    st_46_degc = models.FloatField(db_column='ST_46_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'javori'


class JavoriPila(models.Model):
    hs_cm = models.FloatField(db_column='HS_cm', blank=True, null=True)  # Field name made lowercase.
    swe_mm = models.BigIntegerField(db_column='SWE_mm', blank=True, null=True)  # Field name made lowercase.
    at_degc = models.FloatField(db_column='AT_degC', blank=True, null=True)  # Field name made lowercase.
    rh_pct = models.FloatField(db_column='RH_pct', blank=True, null=True)  # Field name made lowercase.
    hs_laser_cm = models.FloatField(db_column='HS_laser_cm', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'javori_pila'


class Kremelna(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'kremelna'


class LoseniceRejstejn(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'losenice_rejstejn'


class ModravaMeteoH7(models.Model):
    p_mm = models.FloatField(db_column='P_mm', blank=True, null=True)  # Field name made lowercase.
    at_degc = models.FloatField(db_column='AT_degC', blank=True, null=True)  # Field name made lowercase.
    rh_pct = models.FloatField(db_column='RH_pct', blank=True, null=True)  # Field name made lowercase.
    hs_cm = models.FloatField(db_column='HS_cm', blank=True, null=True)  # Field name made lowercase.
    gr_w_m2 = models.FloatField(db_column='GR_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grout_w_m2 = models.FloatField(db_column='GRout_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    swe_mm = models.FloatField(db_column='SWE_mm', blank=True, null=True)  # Field name made lowercase.
    ws_m_s = models.FloatField(db_column='WS_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wd_deg = models.FloatField(db_column='WD_deg', blank=True, null=True)  # Field name made lowercase.
    ws_2_m_s = models.FloatField(db_column='WS_2_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wd_2_deg = models.FloatField(db_column='WD_2_deg', blank=True, null=True)  # Field name made lowercase.
    wsmax_m_s = models.FloatField(db_column='WSmax_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wsmin_m_s = models.FloatField(db_column='WSmin_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rh_2_pct = models.FloatField(db_column='RH_2_pct', blank=True, null=True)  # Field name made lowercase.
    at_2_degc = models.FloatField(db_column='AT_2_degC', blank=True, null=True)  # Field name made lowercase.
    atmin_2_degc = models.FloatField(db_column='ATmin_2_degC', blank=True, null=True)  # Field name made lowercase.
    atmax_2_degc = models.FloatField(db_column='ATmax_2_degC', blank=True, null=True)  # Field name made lowercase.
    sm10_pct = models.FloatField(db_column='SM10_pct', blank=True, null=True)  # Field name made lowercase.
    st10_degc = models.FloatField(db_column='ST10_degC', blank=True, null=True)  # Field name made lowercase.
    sm25_pct = models.FloatField(db_column='SM25_pct', blank=True, null=True)  # Field name made lowercase.
    st25_degc = models.FloatField(db_column='ST25_degC', blank=True, null=True)  # Field name made lowercase.
    sm60_pct = models.FloatField(db_column='SM60_pct', blank=True, null=True)  # Field name made lowercase.
    st60_degc = models.FloatField(db_column='ST60_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'modrava_meteo_h7'


class Modravsky(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    wt_degc = models.FloatField(db_column='WT_degC', blank=True, null=True)  # Field name made lowercase.
    ec_lin_micros_cm = models.FloatField(db_column='EC_lin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_nonlin_micros_cm = models.FloatField(db_column='EC_nonlin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_uncomp_micros_cm = models.FloatField(db_column='EC_uncomp_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wt_ec_degc = models.FloatField(db_column='WT_EC_degC', blank=True, null=True)  # Field name made lowercase.
    ph = models.FloatField(db_column='pH_-', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'modravsky'


class Netradio1(models.Model):
    gr_w_m2 = models.FloatField(db_column='GR_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grout_w_m2 = models.FloatField(db_column='GRout_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lwin_w_m2 = models.FloatField(db_column='LWin_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lwout_w_m2 = models.FloatField(db_column='LWout_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    at_degc = models.FloatField(db_column='AT_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'netradio_1'


class Netradio2(models.Model):
    gr_w_m2 = models.FloatField(db_column='GR_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grout_w_m2 = models.FloatField(db_column='GRout_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lwin_w_m2 = models.FloatField(db_column='LWin_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lwout_w_m2 = models.FloatField(db_column='LWout_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hs_mm = models.FloatField(db_column='HS_mm', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'netradio_2'


class Netradio3(models.Model):
    gr_w_m2 = models.FloatField(db_column='GR_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grout_w_m2 = models.FloatField(db_column='GRout_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lwin_w_m2 = models.FloatField(db_column='LWin_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lwout_w_m2 = models.FloatField(db_column='LWout_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hs_mm = models.FloatField(db_column='HS_mm', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'netradio_3'


class PrasilskyPot(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'prasilsky_pot'


class Ptaci(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    q_m3_s = models.FloatField(db_column='Q_m3/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    p_mm = models.FloatField(db_column='P_mm', blank=True, null=True)  # Field name made lowercase.
    hs_cm = models.FloatField(db_column='HS_cm', blank=True, null=True)  # Field name made lowercase.
    st_neg10_degc = models.FloatField(db_column='ST10_degC', blank=True, null=True)  # Field name made lowercase.
    gt05_degc = models.FloatField(db_column='GT05_degC', blank=True, null=True)  # Field name made lowercase.
    at40_degc = models.FloatField(db_column='AT40_degC', blank=True, null=True)  # Field name made lowercase.
    at80_degc = models.FloatField(db_column='AT80_degC', blank=True, null=True)  # Field name made lowercase.
    at120_degc = models.FloatField(db_column='AT120_degC', blank=True, null=True)  # Field name made lowercase.
    at_degc = models.FloatField(db_column='AT_degC', blank=True, null=True)  # Field name made lowercase.
    wl_2_mm = models.FloatField(db_column='WL_2_mm', blank=True, null=True)  # Field name made lowercase.
    wt_degc = models.FloatField(db_column='WT_degC', blank=True, null=True)  # Field name made lowercase.
    ph = models.FloatField(db_column='pH_-', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wt_ph_degc = models.FloatField(db_column='WT_pH_degC', blank=True, null=True)  # Field name made lowercase.
    ec_lin_micros_cm = models.FloatField(db_column='EC_lin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_nonlin_micros_cm = models.FloatField(db_column='EC_nonlin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_uncomp_micros_cm = models.FloatField(db_column='EC_uncomp_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ptaci'


class PtaciSpa(models.Model):
    hs_cm = models.BigIntegerField(db_column='HS_cm', blank=True, null=True)  # Field name made lowercase.
    at120_degc = models.FloatField(db_column='AT120_degC', blank=True, null=True)  # Field name made lowercase.
    at90_degc = models.FloatField(db_column='AT90_degC', blank=True, null=True)  # Field name made lowercase.
    at60_degc = models.FloatField(db_column='AT60_degC', blank=True, null=True)  # Field name made lowercase.
    at30_degc = models.FloatField(db_column='AT30_degC', blank=True, null=True)  # Field name made lowercase.
    gt05_degc = models.FloatField(db_column='GT05_degC', blank=True, null=True)  # Field name made lowercase.
    st10_degc = models.FloatField(db_column='ST10_degC', blank=True, null=True)  # Field name made lowercase.
    swe_mm = models.FloatField(db_column='SWE_mm', blank=True, null=True)  # Field name made lowercase.
    rh_pct = models.FloatField(db_column='RH_pct', blank=True, null=True)  # Field name made lowercase.
    at_degc = models.FloatField(db_column='AT_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ptaci_spa'


class PtaiPotokIsco(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    wt_degc = models.FloatField(db_column='WT_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ptaci_potok_isco'


class RanklovskyPotok(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    ph = models.FloatField(db_column='pH_-', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wt_ph_degc = models.FloatField(db_column='WT_pH_degC', blank=True, null=True)  # Field name made lowercase.
    do_mg_l = models.FloatField(db_column='DO_mg/l', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wt_do_degc = models.FloatField(db_column='WT_DO_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ranklovsky_potok'

class RoklanskyHajenka(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    ec_lin_micros_cm = models.FloatField(db_column='EC_lin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_nonlin_micros_cm = models.FloatField(db_column='EC_nonlin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_uncomp_micros_cm = models.FloatField(db_column='EC_uncomp_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wt_degc = models.FloatField(db_column='WT_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'roklansky_hajenka'

class RoklanskyPot(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    q_m3_s = models.FloatField(db_column='Q_m3/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_3_micros_cm = models.FloatField(db_column='EC_3_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_4_micros_cm = models.FloatField(db_column='EC_4_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_5_micros_cm = models.FloatField(db_column='EC_5_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wt_degc = models.FloatField(db_column='WT_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'roklansky_pot'


class Rokytka(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    q_m3_s = models.FloatField(db_column='Q_m3/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hs_cm = models.FloatField(db_column='HS_cm', blank=True, null=True)  # Field name made lowercase.
    p_mm = models.FloatField(db_column='P_mm', blank=True, null=True)  # Field name made lowercase.
    swe_mm = models.FloatField(db_column='SWE_mm', blank=True, null=True)  # Field name made lowercase.
    ph = models.FloatField(db_column='pH_-', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wt_ph_degc = models.FloatField(db_column='WT_pH_degC', blank=True, null=True)  # Field name made lowercase.
    rx_mv = models.FloatField(db_column='RX_mV', blank=True, null=True)  # Field name made lowercase.
    wt_ecdegc = models.FloatField(db_column='WT_ECdegC', blank=True, null=True)  # Field name made lowercase.
    ec_lin_micros_cm = models.FloatField(db_column='EC_lin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_nonlin_micros_cm = models.FloatField(db_column='EC_nonlin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_uncomp_micros_cm = models.FloatField(db_column='EC_uncomp_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    at_degc = models.FloatField(db_column='AT_degC', blank=True, null=True)  # Field name made lowercase.
    rh_pct = models.FloatField(db_column='RH_pct', blank=True, null=True)  # Field name made lowercase.
    ws_m_s = models.FloatField(db_column='WS_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wd_deg = models.FloatField(db_column='WD_deg', blank=True, null=True)  # Field name made lowercase.
    ws_2_m_s = models.FloatField(db_column='WS_2_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wd_2_deg = models.FloatField(db_column='WD_2_deg', blank=True, null=True)  # Field name made lowercase.
    wsmax_m_s = models.FloatField(db_column='WSmax_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wsmin_m_s = models.FloatField(db_column='WSmin_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'rokytka'


class SebestianMeteo(models.Model):
    ws_m_s = models.FloatField(db_column='WS_m/s', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wd_deg = models.FloatField(db_column='WD_deg', blank=True, null=True)  # Field name made lowercase.
    p_mm = models.FloatField(db_column='P_mm', blank=True, null=True)  # Field name made lowercase.
    rh_pct = models.FloatField(db_column='RH_pct', blank=True, null=True)  # Field name made lowercase.
    at_degc = models.FloatField(db_column='AT_degC', blank=True, null=True)  # Field name made lowercase.
    gr_w_m2 = models.FloatField(db_column='GR_W/m2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    st10_degc = models.FloatField(db_column='ST10_degC', blank=True, null=True)  # Field name made lowercase.
    gt05_degc = models.FloatField(db_column='GT05_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'sebestian_meteo'


class SlatinnyKh(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    wl_2_mm = models.FloatField(db_column='WL_2_mm', blank=True, null=True)  # Field name made lowercase.
    wt_degc = models.FloatField(db_column='WT_degC', blank=True, null=True)  # Field name made lowercase.
    ec_lin_micros_cm = models.FloatField(db_column='EC_lin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_nonlin_micros_cm = models.FloatField(db_column='EC_nonlin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_uncomp_micros_cm = models.FloatField(db_column='EC_uncomp_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ph = models.FloatField(db_column='pH_-', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    wt_ph_degc = models.FloatField(db_column='WT_pH_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'slatinny_kh'


class SlatinnyPotok(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'slatinny_potok'


class StationMetadata(models.Model):
    st_name = models.TextField(blank=True, primary_key=True) #added primary key
    st_label = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    masl_m_field = models.BigIntegerField(db_column='masl (m)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station_metadata'


class Tmavy(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    ec_lin_micros_cm = models.FloatField(db_column='EC_lin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ec_nonlin_micros_cm = models.FloatField(db_column='EC_nonlin_microS/cm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wt_ec_degc = models.FloatField(db_column='WT_EC_degC', blank=True, null=True)  # Field name made lowercase.
    wt_degc = models.FloatField(db_column='WT_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tmavy'


class ValuesMetadata(models.Model):
    parameter = models.TextField(db_column='Parameter', primary_key=True)  # Field name made lowercase.
    parameter_abreviation_in_data_file = models.TextField(db_column='Parameter abreviation in data file')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unit = models.TextField(db_column='Unit', blank=True, null=True)  # Field name made lowercase.
    django_field_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'values_metadata'
        unique_together = (('parameter', 'parameter_abreviation_in_data_file'),)


class VolynkaMalenice(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'volynka_malenice'


class VolynkaVimperk(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'volynka_vimperk'


class ZhureckyPot(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    p_mm = models.FloatField(db_column='P_mm', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'zhurecky_pot'


class ZlatyHubertky(models.Model):
    swe_1_mm = models.FloatField(db_column='SWE_1_mm', blank=True, null=True)  # Field name made lowercase.
    swe_mm = models.FloatField(db_column='SWE_mm', blank=True, null=True)  # Field name made lowercase.
    hs_mm = models.FloatField(db_column='HS_mm', blank=True, null=True)  # Field name made lowercase.
    at_degc = models.FloatField(db_column='AT_degC', blank=True, null=True)  # Field name made lowercase.
    p_mm = models.FloatField(db_column='P_mm', blank=True, null=True)  # Field name made lowercase.
    hs_2_mm = models.FloatField(db_column='HS_2_mm', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'zlaty_hubertky'


class ZlatyMeteoHlad(models.Model):
    wl_mm = models.FloatField(db_column='WL_mm', blank=True, null=True)  # Field name made lowercase.
    p_mm = models.FloatField(db_column='P_mm', blank=True, null=True)  # Field name made lowercase.
    hs_cm = models.FloatField(db_column='HS_cm', blank=True, null=True)  # Field name made lowercase.
    at_degc = models.FloatField(db_column='AT_degC', blank=True, null=True)  # Field name made lowercase.
    rh_pct = models.FloatField(db_column='RH_pct', blank=True, null=True)  # Field name made lowercase.
    wt_degc = models.FloatField(db_column='WT_degC', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'zlaty_meteo_hlad'
