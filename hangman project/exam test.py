def read_data(filename):
    with open(filename, "r") as f:
        parentdict = {}

        nextline = f.readline()

        for line in f:
            bits = line.split(",")

            assert len(bits) == 9, "bits greater than 9"

            country = bits[0]

            parentdict[country] = {}
            parentdict[country]['year'] = bits[1]
            parentdict[country]['Total water consumption(BCM)'] = float(bits[2])
            parentdict[country]['Per capita_water use(LPD)'] = float(bits[3])
            parentdict[country]['Agricultural water use(%)'] = float(bits[4])
            parentdict[country]['Industrial water use(%)'] = float(bits[5])
            parentdict[country]['Household water use(%)'] = float(bits[6])
            parentdict[country]['Rainfall impact(mm)'] = float(bits[7])
            parentdict[country]['Groundwater depletion rate(%)'] = float(bits[8])

    return parentdict

print(read_data("cleaned_global_water_consumption.csv"))





