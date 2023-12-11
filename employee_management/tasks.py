from celery import shared_task
from django.shortcuts import get_object_or_404
from .models import Employee
from time import sleep
from django.core.exceptions import ObjectDoesNotExist
# def delete_employee_task(employee_id):
#     print('ssssssssssssssssssssssssssss')
#     try:
#         employee = Employee.objects.get(id=employee_id)
#         employee.delete()
#         return f"Employee {employee_id} deleted successfully."
#     except ObjectDoesNotExist:
#         return f"Employee {employee_id} does not exist."
print("FFFFFFFFFFFFFFFFFFFFFFFFFFFF")

@shared_task(bind=True)
def test_func(self):
    print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    for i in range(10):
        print(i)
    return "DONE"