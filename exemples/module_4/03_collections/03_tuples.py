"""Exemple de tuple : données ordonnées mais immuables."""

point = (45.5017, -73.5673)

# Déballage : chaque valeur du tuple est placée dans une variable.
lat, lon = point
print(f"Latitude : {lat}")
print(f"Longitude : {lon}")

# Un tuple est immuable : cette ligne causerait une TypeError.
# point[0] = 50.0
