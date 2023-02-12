from ..models import Measurement
from variables.logic import variables_logic as vl
def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement

def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement.variable = vl.get_variable(new_var["variable"])
    measurement.value = new_var["value"]
    measurement.unit = new_var["unit"]
    measurement.place = new_var["place"]
    measurement.save()
    return measurement

def create_measurement(var):
    measurement = Measurement(variable = vl.get_variable(var["variable"]),
                              value = var["value"],
                              unit = var["unit"],
                              place = var["place"]
    )
    measurement.save()
    return measurement

def delete_measurement(var):
    measurement = Measurement.objects.get(pk=var)
    measurement.delete()
    return measurement

