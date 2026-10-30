## NOAH ZEEMAN - 15494365
## NSP2 "flashingLED"
## 27 Oct '26

# importeren van benodigde packages
import pyvisa

# zoeken naar verbonden arduinos
rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
print(ports)

# specifieke device aanwijzen
device = rm.open_resource(
    "ASRL/dev/ttyACM0::INSTR", read_termination="\r\n", write_termination="\n"
)
for x in range(10):
    for i in range(1023):
        light = device.query(f"OUT:CH0 {i}")

# laatste licht-waarde uitlezen
final_value = device.query("OUT:CH0?")
print(final_value)