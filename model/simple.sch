v 20110115 2
C 40000 40000 0 0 0 title-B.sym
C 42000 49400 1 270 0 voltage-1.sym
{
T 42500 49300 5 10 0 0 270 0 1
device=VOLTAGE_SOURCE
T 42500 49200 5 10 0 1 270 0 1
refdes=Acell
T 42500 49500 5 10 1 1 270 0 1
value=cell_potential
}
C 43000 49600 1 90 0 resistor-2.sym
{
T 42650 50000 5 10 0 0 90 0 1
device=CPE
T 42700 49800 5 10 0 1 90 0 1
refdes=Xintracpe
T 43200 49700 5 10 1 0 90 0 1
file=intracellular_cpe.cir
}
C 43300 49400 1 0 0 resistor-1.sym
{
T 43600 49800 5 10 0 0 0 0 1
device=RESISTOR
T 43500 49700 5 10 1 1 0 0 1
refdes=R_pene
}
N 42900 50600 42900 50500 4
C 40900 48000 1 90 0 resistor-1.sym
{
T 40500 48300 5 10 0 0 90 0 1
device=RESISTOR
T 40600 48000 5 10 1 1 90 0 1
refdes=Rwholecell
}
C 41700 48000 1 90 0 capacitor-1.sym
{
T 41000 48200 5 10 0 0 90 0 1
device=CAPACITOR
T 41200 48000 5 10 1 1 90 0 1
refdes=Cwholecell
T 40800 48200 5 10 0 0 90 0 1
symversion=0.1
}
N 42900 47800 42900 49600 4
C 44700 49600 1 90 0 resistor-2.sym
{
T 44350 50000 5 10 0 0 90 0 1
device=CPE
T 44400 49800 5 10 0 1 90 0 1
refdes=Xsheathedcpe_i
T 44900 49700 5 10 1 0 90 0 1
file=sheathed_cpe_i.cir
T 45100 49700 5 10 0 0 90 0 1
pinseq=1,2
}
N 44600 50500 44600 50600 4
N 44600 49100 44600 49600 4
C 45000 49400 1 0 0 resistor-1.sym
{
T 45300 49800 5 10 0 0 0 0 1
device=RESISTOR
T 45200 49700 5 10 1 1 0 0 1
refdes=R_seal_i
}
C 46400 49600 1 90 0 resistor-2.sym
{
T 46050 50000 5 10 0 0 90 0 1
device=CPE
T 46100 49800 5 10 0 1 90 0 1
refdes=Xextracpe
T 46600 49700 5 10 1 0 90 0 1
file=extracellular_cpe.cir
}
N 46300 50600 46300 50500 4
N 45000 49500 44600 49500 4
N 46300 49500 45900 49500 4
C 40900 46100 1 90 0 resistor-1.sym
{
T 40500 46400 5 10 0 0 90 0 1
device=RESISTOR
T 40600 46300 5 10 1 1 90 0 1
refdes=Rbath
}
N 40800 45900 40800 46100 4
C 40700 45600 1 0 0 gnd-1.sym
N 46300 47400 46300 49600 4
N 40800 47400 46300 47400 4
{
T 42500 47200 5 10 1 1 0 0 1
netname=solution_bus
}
N 42900 47800 44600 47800 4
{
T 43000 47900 5 10 1 1 0 0 1
netname=cell_bus
}
C 45200 48200 1 90 0 capacitor-1.sym
{
T 44500 48400 5 10 0 0 90 0 1
device=CAPACITOR
T 44700 48400 5 10 1 1 90 0 1
refdes=Cmembrane_i
T 44300 48400 5 10 0 0 90 0 1
symversion=0.1
}
C 44300 48200 1 90 0 resistor-1.sym
{
T 43900 48500 5 10 0 0 90 0 1
device=RESISTOR
T 44000 48400 5 10 1 1 90 0 1
refdes=Rmembrane_i
}
N 44200 49100 45000 49100 4
N 44200 48200 45000 48200 4
N 44600 47800 44600 48200 4
N 44600 49500 44200 49500 4
{
T 44000 49500 5 10 1 1 0 0 1
netname=Rpene_bus
}
C 47300 49500 1 90 0 resistor-1.sym
{
T 46900 49800 5 10 0 0 90 0 1
device=RESISTOR
T 47000 49700 5 10 1 1 90 0 1
refdes=RStray
}
C 48200 49500 1 90 0 capacitor-1.sym
{
T 47500 49700 5 10 0 0 90 0 1
device=CAPACITOR
T 47700 49700 5 10 1 1 90 0 1
refdes=CStray
T 47300 49700 5 10 0 0 90 0 1
symversion=0.1
}
N 47200 50400 48000 50400 4
N 48000 49500 47200 49500 4
C 47500 49000 1 0 0 gnd-1.sym
N 47600 49300 47600 49500 4
N 47600 50400 47600 50600 4
N 42900 50600 47600 50600 4
{
T 43400 50700 5 10 1 1 0 0 1
netname=electrode_bus
}
N 40800 48000 40800 47000 4
N 41500 48000 41500 47400 4
N 42900 49500 40800 49500 4
N 40800 49500 40800 48900 4
N 41500 48900 41500 49500 4
N 42200 49400 42200 49500 4
N 43300 49500 42900 49500 4
C 42100 48200 1 0 0 gnd-1.sym
