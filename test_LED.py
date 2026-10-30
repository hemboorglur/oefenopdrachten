## NOAH ZEEMAN - 15494365
## NSP2 "LED laten branden"
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
for i in range(1024):
    light = device.query(f"OUT:CH0 {i}")

final_value = device.query("OUT:CH0?")
print(final_value)