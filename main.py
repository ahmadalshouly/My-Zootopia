from animals_web_generator import generate_animal_html
from data_fetcher import get_animals_from_api

def main():
    """ Main function """
    while True:
        animal_name = input("Please enter animal's name: ")

        if not animal_name:
            print("Please enter animal's name!!")
            continue

        if not animal_name.isalpha():
            print("Please enter animal's name!!")
            continue

        animals_data = get_animals_from_api(animal_name)

        if not animals_data:
            print (f"No data found for ({animal_name})")
            continue

        generate_animal_html(animals_data, "animals_template.html","animals.html")
        break

if __name__ == "__main__":
    main()