from django.contrib.admin.apps import AdminConfig

class BookrAdminConfig(AdminConfig):
    default_site = "bookr.admin.BookrAdminSite"
