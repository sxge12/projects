f = open("discoveries.txt")
z = open("processedDiscoveries.txt", "w")
aspect_count = 0
#aspects = 3
for i in range(5):
 discoveries = f.readline()
 x = discoveries.split(sep=',')
 impact_level = int(x[1])
 discovery_name = x[0]
 description = ", ".join(x[2:])
 if impact_level >= 8:
    prefix = "revolutionary: "
    aspect_count += 1
 elif impact_level >= 5:
    prefix = "significant: "
    aspect_count += 1
 else :
    prefix = "minor: "
    aspect_count += 1

 aspects = description.split(",")
 aspectscounter = len(aspects)
 aspectsstring = ",".join(aspects)

 processedlines = f"{prefix} {discovery_name}, {impact_level}, {aspectscounter}: {aspectsstring}"

 z.write(processedlines)
z.close()



















