from django.contrib import admin
from .models import Trainers, Abonements, Clubs, Partners, Equipments, grouptraining
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin


@admin.register(Trainers)
class trainsxls(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    pass
@admin.register( Abonements)
class abonexls(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    pass
@admin.register(Clubs)
class clubsxls(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    pass
@admin.register(Partners)
class prtnersxls(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    pass
@admin.register(Equipments)
class eqipmsxls(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    pass
@admin.register(grouptraining )
class grouptrsxls(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    pass
