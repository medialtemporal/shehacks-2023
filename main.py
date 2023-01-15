from classify import Question
from keywords import extract_keyword
from generate import generate_symptoms, generate_safe, generate_mystic
import requests
import cohere
from time import sleep


def main():
    query = str(input("What questions do you have for MySTIc today?\n"))

    prompt = Question(query)

    prompt.question_classify()

    classification = prompt.get_classification()

    print()

    try:
        if classification == 'clinic':
            clinics = clinic_questions()

            print("Here are a list of clinics in your area that may be able to provide you with more information on "
                  "sexually-transmitted infections:\n")
            for clinic in clinics:
                sleep(1)
                print(f'{clinic[0]}\n{clinic[1]}\n')

        elif classification == 'symptom':
            print(symptom_questions(prompt.get_question()))

        elif classification == 'mystic':
            print(mystic_questions(prompt.get_question()))

        else:
            print(safe_sex_questions(prompt.get_question()))

    except cohere.error.CohereError:
        print('Please adjust your prompt and try again, as this generation may be a potential violation of Co:here\'s '
              'Usage Guidelines.')


def clinic_questions():
    """
    A function for questions classified by co:here as being about finding clinics to get tested for STIs.
    :return: A list of possible clinics in the user's vicinity and their addresses.
    """
    api_key = "AIzaSyC_O6EW91JhE_B1FR6rKmdM7WMQ_F4Relg"
    location = "43.02,-81.28"  # currently hardcoded, should change in mobile app or based on area code of phone #
    radius = 10000  # in metres, so 10 kilometres
    keyword = 'std testing'  # change to be more dynamic
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}" \
          f"&keyword={keyword}&key={api_key} "
    response = requests.get(url)
    data = response.json()
    clinics = []
    for location in data["results"]:
        if 'men' not in location["name"].lower() and\
                'covid-19' not in location["name"].lower() and\
                'higi' not in location["name"].lower() and\
                'travel' not in location['name'].lower() and\
                'surehire' not in location['name'].lower():  # hard coded instead of making better search result filter
            clinics.append((location["name"], location["vicinity"]))
    return clinics


def symptom_questions(question):
    """
    A function for questions classified by co:here as being about STI symptoms.
    :return:
    """
    keys = extract_keyword(question)
    response = generate_symptoms(question, keys)
    return response


def safe_sex_questions(question):
    response = generate_safe(question)
    return response


def mystic_questions(question):
    response = generate_mystic(question)
    return response


if __name__ == '__main__':
    main()



