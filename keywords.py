import cohere

co = cohere.Client('vgI94PHV5fb3ZYLBM2kb72gAvqByrai9YFYnQOyG')


def extract_keyword(question):
    prompt = 'This program generates keywords based off of a question about sexual health.' \
             '\n\nQuestion: What are genital warts a symptom of?\n' \
             'Keywords: genital warts symptom\n' \
             '--\n' \
             'Question: My vagina is itchy\n' \
             'Keywords: itchy vagina symptom\n' \
             '--\n' \
             'Question: Should it hurt to pee?\n' \
             'Keywords: hurt peeing\n' \
             '--\n' \
             'Question: I have weird vaginal discharge\n' \
             'Keywords: vaginal discharge\n' \
             '--\n' \
             'Question: large rash on penis\n' \
             'Keywords: penis rash\n' \
             '--\n' \
             'Question: what is chlamydia\n' \
             'Keywords: chlamydia\n' \
             '--\n' \
             'Question: what are symptoms of gonorrhea\n' \
             'Keywords: gonorrhea symptoms\n' \
             '--\n' \
             'Question: '

    prompt = prompt + " " + question + '\nKeywords:'
    response = co.generate(
        model='xlarge',
        prompt=prompt,
        max_tokens=15,
        temperature=0.3,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')

    answer = response.generations[0].text
    answer.rstrip("\n--").strip("")
    return answer
