import cohere
from cohere.classify import Example


class Question:

    def __init__(self, question):
        self._question = question
        self._classification = None

    def question_classify(self):
        co = cohere.Client('vgI94PHV5fb3ZYLBM2kb72gAvqByrai9YFYnQOyG')
        model = 'large'

        examples = [
            # Symptoms
            Example("I have pain when urinating, do I have an STI?", "symptom"),
            Example("Is vaginal discharge normal", "symptom"),
            Example("What is chlamydia", "symptom"),
            Example("What are genital warts a sign of", "symptom"),
            # MySTIc
            Example("What is MySTIc?", "mystic"),
            Example("Does MySTIc cost money?", "mystic"),
            Example("What does MySTIc do?", "mystic"),
            Example("Who runs mystic", "mystic"),
            # Clinic
            Example("What should I do next?", "clinic"),
            Example("What doctors are near me?", "clinic"),
            Example("Where should I get tested?", "clinic"),
            # Safe Sex
            Example("Can I get an STI without doing penetrative sex?", "safe"),
            Example("I used a condom during sex, can I still have an STD", "safe"),
            Example("How do I practice safe sex?", "safe"),
            Example("How do lesbians practice safe sex?", "safe")
        ]

        inputs = [self._question]

        # classifies input based on model and examples
        response = co.classify(
            model=model,
            inputs=inputs,
            examples=examples)

        model_classification = str(response.classifications[0])

        self._classification = model_classification.split()[1].lstrip('"').rstrip('",')

    def get_classification(self):
        return self._classification

    def get_question(self):
        return self._question
