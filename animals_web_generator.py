import data_fetcher

animal_name = input("Enter a name of an animal: ").strip()

animals = data_fetcher.fetch_data(animal_name)

if not animals:
    body = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
else:
    body = ""
    for animal in animals:
        name = animal.get("name", "Unknown")
        locations = animal.get("locations", [])
        locations_text = ", ".join(locations) if locations else "Unknown"

        body += f"""
        <div class="card">
          <h2>{name}</h2>
          <p><strong>Locations:</strong> {locations_text}</p>
        </div>
        """

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Zootopia With API</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 24px; }}
    .card {{ border: 1px solid #ddd; padding: 12px; border-radius: 8px; margin-bottom: 12px; }}
  </style>
</head>
<body>
  <h1>Zootopia With API</h1>
  {body}
</body>
</html>
"""

with open("animals.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Website was successfully generated to the file animals.html.")