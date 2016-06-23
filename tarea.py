from db import query


def file_get_contents(filename):
    a = open(filename)
    b = a.read()
    a.close()
    return b


def get_sql():
    return file_get_contents("tarea.sql")


def fmt(tmpl, data, list_names):
    if len(list_names) == 0:
        return interpolate(tmpl, data)

    key = list_names[0]
    rest = list_names[1:]

    a = tmpl.split("<!--"+key+"_START-->")
    if len(a) != 2:
        return "ERROR: "+key+"_START is missing.[" + tmpl + "]"

    b = a[1].split("<!--"+key+"_END-->")
    if len(b) != 2:
        return "ERROR: "+key+"_END is missing.[" + tmpl + "]"

    start = a[0]
    body = b[0]
    end = b[1]

    ax = ""
    for row in data:
        current_body = body
        ax += fmt(current_body, row, rest)

    return start + ax + end


def interpolate(sql, parameters):
    out = sql
    for i in parameters:
        out = out.replace("[#"+i+"]", unicode(parameters[i]))
    return out


def get_distances_from(origin):
    tmpl = {'lat': origin["latitude"], 'lon': origin["longitude"]}
    d = get_sql()
    distance_sql = interpolate(d, tmpl)
    # print("*" * 60)
    # print(origin["location"])
    # print(distance_sql)
    return query(distance_sql)


def get_headers():
    tmpl = file_get_contents("headers.html")
    data = query("select location from city order by id")
    return fmt(tmpl, data, ["LOOP"])


def get_results(distances):
    tmpl = file_get_contents("template.html")
    tmpl = tmpl.replace("[#headers]", get_headers())

    data = []
    for group in distances:
        data.append([{"distance": "<b>"+group["location"]+"</b>"}] + group["distances"])  # noqa

    a = 0
    while a < len(data):
        b = 0
        while b < len(data[a]):
            if a+1 == b:
                data[a][b]["distance"] = "N/A"
            b += 1
        a += 1

    ad = (fmt(tmpl, data, ["LOOP", "DIS"]))
    return ad
    # fp = open("salida.html", "w")
    # fp.write(ad.encode("utf-8"))
    # fp.close()


def round_column(data, column, decimals):
    for row in data:
        if row[column] is not None:
            row[column] = round(float(row[column]), decimals)
    return data


def get_all_cities_html():
    cities = query("SELECT latitude,longitude,location from city")
    distances = []
    for city in cities:
        distance_list = get_distances_from(city)
        distance_list = round_column(distance_list, "distance", 3)
        distances.append({"location": city["location"],
                          "distances": distance_list})
    # pprint.pprint(distances)
    return(get_results(distances))


def main():
    print(get_all_cities_html().encode("utf-8"))

if __name__ == "__main__":
    main()
