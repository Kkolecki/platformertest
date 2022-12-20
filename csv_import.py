from csv import reader


def import_csv_layout(path):  # importing csv file into a list to read later for map generation
    terrain_map = []
    with open(path) as map:
        layout = reader(map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map