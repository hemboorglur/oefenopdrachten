## NOAH ZEEMAN - 15494365
## NSP2 - ECPC - basisscript voor het experiment "ADC conversie"
## 30 Oct '26


# [voltage] = (max_volt / max_adc) * [ADC_waarde] = (3.3/1023) * [ADC_waarde]
# c_volt is de voltage conversie constante
raw_value = [0, 1023, 700]
c_volt = 3.3/1023
for value in raw_value:
    voltage = c_volt * value
    print(voltage)

#[ADC_waarde] = (max_adc / max_volt) * [ADC_waarde] = (1023/3.3) * [ADC_waarde]
# c_raw is de raw_value conversie constante
voltage = 2.28
c_raw = 1023/3.3
raw_value = c_raw * voltage
print(raw_value)
