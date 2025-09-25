from biotime import BIOT



bio = BIOT("http://185.203.239.37:8089", "admin", "C@rdinar@2025")
# print(bio.get_all_area())
# print(bio.get_all_employee())
print(bio.get_work_report(emp_id=337))
