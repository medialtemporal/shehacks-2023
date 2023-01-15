import cohere

co = cohere.Client('vgI94PHV5fb3ZYLBM2kb72gAvqByrai9YFYnQOyG')


def generate_symptoms(question, symptom_keywords):
    prompt = 'This program will generate a summarized informational response to a question about sexually transmitted ' \
             'infections, given the question, and keywords from the question.\n' \
             '--\n' \
             'Question: What is chlamydia?\n' \
             'Keywords: chlamydia\n' \
             'Response: Chlamydia is a sexually transmitted infection caused by bacteria that affects the cervix, ' \
             'penis, rectum, and throat. You can get chlamydia from having sex with someone who already has it. Many ' \
             'people with chlamydia do not have symptoms, but you can pass on chlamydia even if you don\'t have ' \
             'symptoms. If you do have symptoms, they usually occur 2 to 6 weeks after exposure. Symptoms include ' \
             'pain, swelling, or discharge from genitals. It\'s important to treat chlamydia, as it can lead to ' \
             'serious health problems if untreated. Chlamydia can be treated and cured with a single dose of ' \
             'antibiotics, and your sexual partners should also get tested and treated.\n' \
             '--\n' \
             'Question: What are symptoms of gonorrhea?\n' \
             'Keywords: gonorrhea symptoms\n' \
             'Response: Some common symptoms of gonorrhea include irritation when peeing, pain during sex, and ' \
             'unusual discharge from genitals. It\'s important to remember some people will not have any signs for ' \
             'months, and some people may not have any symptoms at all. Here is a list of symptoms of gonorrhea:\n' \
             '* Penis: Thick, yellow or green discharge, swelling or pain in testicles, itchiness.\n' \
             '* Bleeding, pain, or itching, mucus discharge from rectum.\n' \
             '* Vulva/Vagina: Bleeding after sex or between periods, pain during intercourse, discharge.\n ' \
             '* Pain in abdomen or lower back for those with ' 'vulvas/vaginas.\n' \
             '* Throat infection (if gonorrhea infection is in the throat).\n' \
             '* Redness, itching, or discharge in the eyes (if gonorrhea is in the eyes).\n' \
             '* Pain while urinating\n' \
             'If you suspect you have gonorrhea, you should get tested so you can get it treated before it causes ' \
             'complications.\n' \
             '--\n' \
             'Question: Do I have gonorrhea?\n' \
             'Keywords: gonorrhea\n' \
             'Response: You may have gonorrhea if you have symptoms including peeing, pain during sex, and unusual ' \
             'discharge from the genitals. However, many people with gonorrhea do not have any symptoms for months, ' \
             'or at all. As well, these symptoms are common to many other sexually transmitted infections. \n' \
             '--\n' \
             'Question:'

    response = co.generate(
        model='xlarge',
        prompt=prompt + " " + question + '\nKeywords:' + symptom_keywords + " " + '\nResponse:',
        max_tokens=300,
        temperature=0.3,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')

    return response.generations[0].text


def generate_safe(question):
    prompt = 'This program will generate a summarized informational response to a question about safe sex, given the ' \
             'question.\n' \
             '--\n' \
             'Question: What is safe sex?\n' \
             'Response: Sex can be fun and pleasurable but it can come with risks such as sexually transmitted ' \
             'infections (STIs) and/or unplanned pregnancy. Safer sex is about taking care of yourself and your ' \
             'partner(s). Safer sex includes talking to your partner(s) before having sex about safer sex tools ' \
             'like condoms. It also includes asking your partner(s) before having sex if they have an STI, and ' \
             'getting tested for STIs when you or your partner has a new sexual partner or has symptoms of an STI. ' \
             'Lastly, safer sex includes considering sexual activities that can’t lead to an unplanned pregnancy and ' \
             'put you at lower risk of an STI.' \
             '--\n' \
             'Question: How can I practice safe sex?\n' \
             'Response: Safer sex is about taking care of yourself and your partner(s). Safer sex includes talking to ' \
             'your partner(s) before having sex about safer sex tools like condoms. It also includes asking your ' \
             'partner(s) before having sex if they have an STI, and getting tested for STIs when you or your partner' \
             ' has a new sexual partner or has symptoms of an STI. Lastly, safer sex includes considering sexual ' \
             'activities that can’t lead to an unplanned pregnancy and put you at lower risk of an STI.\n' \
             '--\n' \
             'Question: Can I get an STD without having had penetrative sex?\n' \
             'Response: Yes, you can still get an STI without having had penetrative sex. STIs can be transmitted ' \
             'through semen, but there are a lot of other ways they can be spread, including contact with vaginal ' \
             'fluid, pre-cum, open cuts or sores, and skin-to-skin contact.  \n' \
             '--\n' \
             'Question:'

    response = co.generate(
        model='xlarge',
        prompt=prompt + " " + question + " " + '\nResponse:',
        max_tokens=200,
        temperature=0.3,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')

    return response.generations[0].text


def generate_mystic(question):
    prompt = 'This program will generate a summarized informational response to a question about an app called ' \
             'MySTIc, given the question and the following information: MySTIc (or my STI clinic) is a program that ' \
             'allows users to anonymously inform sexual partners if they test positive for an STD. It does this by ' \
             'maintaining a log of the user’s sexual partners. After every sexual encounter, the user can add their ' \
             'sexual partner’s name (optional) and phone number to the application, along with the date of the ' \
             'encounter. The next time the user is tested, they can input either their test results or have their ' \
             'doctor virtually confirm that they have an STI on the app. This will then automatically notify users ' \
             'through texts sent to the numbers stored in the log of partners. These texts will not tell the receiver ' \
             'the name of the person who tested positive, and it will only send the type of STI if the STI is HIV. ' \
             'This is because HIV that is caught early on can be treated completely with post-exposure prophylaxis (' \
             'PEP). Mystic also makes it easier for people to inform past sexual partners without having to confront ' \
             'them face to face. If the STI is not HIV, the text will simply say STI without explicitly saying which ' \
             'STI it is. The texts will resemble something like this: “Hi there! This is a message from Mystic (My ' \
             'STI Clinic). A recent sexual partner of yours has tested positive for HIV. We encourage you to get ' \
             'tested at your nearest clinic. More information about STIs, clinics, and next steps can be found at ' \
             'Mystic.ca.” Mystic will also allow users to find more information about STIs, STI symptoms, ' \
             'and safe sex. Mystic will also show users clinics near them that will allow them to get tested for STIs ' \
             'or can help with treatment.\n' \
             '--\n' \
             'Question: What is MySTIc?\n' \
             'Response: MySTIc (or my STI clinic) is an app that allows users to anonymously inform sexual partners if' \
             ' they test positive for an STI. Once partners are informed, the app also provides them with a chat bot ' \
             'to learn more about STIs and find clinics near them to get tested.\n--\nQuestion: Why doesn\'t the app' \
             ' tell me what STI I have?\nResponse: These texts will only include the type of STI the sender has if ' \
             'the STI is HIV. This is because HIV that is caught early on can be treated completely, so it\'s important' \
             ' to know right away. If the STI is not HIV, the text will simply say STI without explicitly saying which' \
             ' STI it is, and encourage the receiver to\n' \
             '--\n' \
             'Question: Can I ask MySTIc for information about STIs?\n' \
             'Response: Yes, Mystic allows users to find more information about STIs, STI symptoms, and safe sex. It ' \
             'can also show users clinics near them that will allow them to get tested for STIs or can help with ' \
             'treatment.\n' \
             '--\n' \
             'Question: Can MySTIc tell me about clinics?\n' \
             'Response:',

    response = co.generate(
        model='xlarge',
        prompt='prompt' + " " + question + " " + '\nResponse:',
        max_tokens=200,
        temperature=0.6,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')

    return response.generations[0].text

