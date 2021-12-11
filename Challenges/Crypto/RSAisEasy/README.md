```text
HTB challenge -- Crypto[easy] <<RSAisEasy>>
Link: https://app.hackthebox.com/challenges/rsaiseasy
```

```text
CHALLENGE DESCRIPTION
I think this is safe... Right?
```

```python
#!/usr/bin/env python3
from Crypto.Util.number import bytes_to_long, getPrime
from secrets import flag1, flag2
from os import urandom

flag1 = bytes_to_long(flag1)
flag2 = bytes_to_long(flag2)

p, q, z = [getPrime(512) for i in range(3)]

e = 0x10001

n1 = p * q
n2 = q * z

c1 = pow(flag1, e, n1)
c2 = pow(flag2, e, n2)

E = bytes_to_long(urandom(69))

print(f'n1: {n1}')
print(f'c1: {c1}')
print(f'c2: {c2}')
print(f'(n1 * E) + n2: {n1 * E + n2}')
```

```text
n1: 101302608234750530215072272904674037076286246679691423280860345380727387460347553585319149306846617895151397345134725469568034944362725840889803514170441153452816738520513986621545456486260186057658467757935510362350710672577390455772286945685838373154626020209228183673388592030449624410459900543470481715269
c1: 92506893588979548794790672542461288412902813248116064711808481112865246689691740816363092933206841082369015763989265012104504500670878633324061404374817814507356553697459987468562146726510492528932139036063681327547916073034377647100888763559498314765496171327071015998871821569774481702484239056959316014064
c2: 46096854429474193473315622000700040188659289972305530955007054362815555622172000229584906225161285873027049199121215251038480738839915061587734141659589689176363962259066462128434796823277974789556411556028716349578708536050061871052948425521408788256153194537438422533790942307426802114531079426322801866673
(n1 * E) + n2: 601613204734044874510382122719388369424704454445440856955212747733856646787417730534645761871794607755794569926160226856377491672497901427125762773794612714954548970049734347216746397532291215057264241745928752782099454036635249993278807842576939476615587990343335792606509594080976599605315657632227121700808996847129758656266941422227113386647519604149159248887809688029519252391934671647670787874483702292498358573950359909165677642135389614863992438265717898239252246163

```