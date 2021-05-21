from django.db.models import Count, Max

def removeDuplicates(MyObject):

    unique_fields = ['district_name', 'district_id', 'name', 'vaccine','vaccine_date', 'available_capacity','status']
    
    duplicates = (
        MyObject.objects.values(*unique_fields)
        .order_by()
        .annotate(max_id=Max('id'), count_id=Count('id'))
        .filter(count_id__gt=1)
    )

    for duplicate in duplicates:
        (MyObject.objects.filter(**{x: duplicate[x] for x in unique_fields}).exclude(id=duplicate['max_id']).delete())
