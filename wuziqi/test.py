import numpy
residual = {-3.4927642611365, 1.1709566609995, -5.7665154143868, 1.353236934182, 13.059821050372, 2.1424546968475, -6.1509611869629, -2.3162284799146}
reserve = 0
for i in residual:

    reserve += i * i
print(reserve)

print(numpy.sqrt(reserve/len(residual) - 2))
