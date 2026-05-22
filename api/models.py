from django.db import models

# Create your models here.

class Log(models.Model):
    """
    Abstract model containing common operational metadata fields.
    Provides tracking attributes to all inheriting database subclasses.
    """
    created_by = models.BigIntegerField(
        db_column='CreatedBy', null=True, blank=True, default=0
    )
    created_on = models.DateTimeField(
        db_column='CreatedOn', auto_now_add=True
    )
    modified_by = models.BigIntegerField(
        db_column='ModifiedBy', default=0, null=True, blank=True
    )
    modified_on = models.DateTimeField(
        db_column='ModifiedOn', auto_now=True
    )
    is_active = models.BooleanField(
        db_column="IsActive", default=True
    )
    is_deleted = models.BooleanField(
        db_column="IsDeleted", default=False
    )

    class Meta:
        abstract = True  # 🚨 Prevents Django from creating a standalone physical database table
        
class AccessLevel:
    """Access levels and system role identification codes for the platform."""
    CUSTOMER = 400
    DRIVER = 700
    HOSTESS = 500
    ADMIN = 800
    SUPER_ADMIN = 900

    CUSTOMER_CODE = 'customer'
    DRIVER_CODE = 'driver'
    HOSTESS_CODE = 'hostess'
    ADMIN_CODE = 'admin'
    SUPER_ADMIN_CODE = 'super-admin'

    CHOICES = (
        (DRIVER, "Driver"),
        (CUSTOMER, "Customer"),
        (SUPER_ADMIN, 'Super Admin'),
        (ADMIN, 'Admin'),
        (HOSTESS, 'Hostess'),
    )
    DICT = dict(CHOICES)
    
class Role(Log):
    """Role classification table mapping permission scopes to internal access hierarchies."""
    name = models.CharField(db_column='Name', max_length=255, unique=True)
    code = models.SlugField(db_column='Code', default='')
    description = models.TextField(db_column='Description', null=True, blank=True)
    access_level = models.IntegerField(
        db_column='AccessLevel', 
        choices=AccessLevel.CHOICES,
        default=AccessLevel.CUSTOMER
    )
    
    class Meta:
        db_table = 'Roles'
        
# 