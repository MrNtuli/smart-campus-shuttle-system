# List of locations
locations = [
    "Admin Building", "Engineering Block", "Science Labs", "Library", "ICT Department",
    "Residence A", "Residence B", "Cafeteria", "Sports Complex", "Main Entrance"
]

# Define connections (edges) as a directed graph
edges = [
    ("Admin Building", "Library"),
    ("Library", "ICT Department"),
    ("ICT Department", "Engineering Block"),
    ("Engineering Block", "Science Labs"),
    ("Science Labs", "Cafeteria"),
    ("Cafeteria", "Residence A"),
    ("Residence A", "Residence B"),
    ("Residence B", "Main Entrance"),
    ("Residence B", "Admin Building"),  # Loop back
    ("Library", "Sports Complex")
]

# Create Adjacency Matrix
adj_matrix = [[0]*len(locations) for _ in range(len(locations))]

for start, end in edges:
    i = locations.index(start)
    j = locations.index(end)
    adj_matrix[i][j] = 1

# Print Adjacency Matrix
print("Adjacency Matrix:")
print("   " + " | ".join(loc[:4] for loc in locations))
for i, row in enumerate(adj_matrix):
    print(f"{locations[i][:4]} | " + " | ".join(str(val) for val in row))

# Create Adjacency List (Dictionary)
adj_list = {loc: [] for loc in locations}

for start, end in edges:
    adj_list[start].append(end)

# Print Adjacency List
print("\nAdjacency List:")
for key in adj_list:
    print(f"{key} -> {', '.join(adj_list[key])}")
