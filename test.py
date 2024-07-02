import math

def Rr_step_size():
    # Computing the number of x values for Isc_20mA and Turn_off_80mA
    len_Rr = math.floor((19 - 11) / 0.4)
    
    # Isc_20mA
    preVal = 10
    val = 10 + 0.4
    for i in range(len_Rr):
        Rr_data['x_Rr'].append(f'{preVal}~{val}')
        preVal = val
        val += Rr_data['step_size_Rr']
        val = round(val, 2)
    # Rr_data['x_Rr'][len_Rr - 1] = f'> {preVal}'
    # Rr_data['x_Rr'][0] = f'< {Rr_data["data_lLimit_Rr"]}'
