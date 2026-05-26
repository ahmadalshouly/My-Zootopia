import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)

def serialize_animals(animals):
    """ Serializes animals and their info """
    output = '<li class="cards__item">'

    if "name" in animals:
        output += f'<div class="card__title">{animals["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    if 'taxonomy' in animals and 'kingdom' in animals["taxonomy"]:
        kingdom = animals["taxonomy"]["kingdom"]
        output+= f'       <strong>Kingdom:</strong> {kingdom}<br/>\n'

    if 'taxonomy' in animals and 'scientific_name' in animals["taxonomy"]:
        scientific_name = animals["taxonomy"]["scientific_name"]
        output += f'      <strong>Scientific name:</strong> {scientific_name}<br/>\n'

    if "characteristics" in animals and"diet" in animals["characteristics"]:
        diet = animals["characteristics"]["diet"]
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'

    if "locations" in animals and len(animals["locations"])>0:
        output += f'      <strong>Location:</strong> {animals["locations"][0]}<br/>\n'

    if "characteristics" in animals and "type" in animals["characteristics"]:
        animal_type = animals["characteristics"]["type"]
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    output += '  </p>\n'
    output += "</li>\n"
    return output

def generate_animal_html(data, template_path, output_path):
    """ Generates HTML page for animals """
    output = ""
    for animal in data:
        output += serialize_animals(animal)
    with open(template_path, "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    # add encoding to head
    if '<meta charset="UTF-8">' not in template_content:
        template_content =template_content.replace(
            "<head>",
            "<head> \n<meta charset='UTF-8'>"
        )

    # replace the content with our output
    final_template = template_content.replace("__REPLACE_ANIMALS_INFO__",output)

    #create the animals.html file
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(final_template)
    print("Animals Web Generator has been successfully created")

def main():
    """ Main function """
    animals_data = load_data("animals_data.json")
    generate_animal_html(animals_data, "animals_template.html", "animals.html")

if __name__ == "__main__":
    main()