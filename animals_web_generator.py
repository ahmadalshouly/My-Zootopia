from data_fetcher import serialize_animals

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
