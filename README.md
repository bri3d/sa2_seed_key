# SA2 Seed Key

SA2 Seed/Key authentication is a mechanism for authorizing test / tool clients with Volkswagen Auto Group control units, usually used to unlock a Programming session to re-flash the control units.

The SA2 Seed/Key "script" is contained in the FRF or ODX flash container, and consists of a small bytecode machine in which simple opcodes are applied to the "seed" provided by the ECU to generate the "Key".

# Usage:

```
vs = Sa2SeedKey([0x68, 0x02, 0x81, 0x49, 0x93, 0xa5, 0x5a, 0x55, 0xaa, 0x4a, 0x05, 0x87, 0x81, 0x05, 0x95, 0x26, 0x68, 0x05, 0x82, 0x49, 0x84, 0x5a, 0xa5, 0xaa, 0x55, 0x87, 0x03, 0xf7, 0x80, 0x6a, 0x4c], 0x1a1b1c1d)
result = vs.execute() # 0x6a37f02e
```
