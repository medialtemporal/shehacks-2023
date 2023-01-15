# MySTIc
## My STI Clinic is an app to allow users to keep track of sexual partners, anonymously notify partners about STI results, learn more about STIs and safe sex, and find out what local clinics can help.

### Inspiration
STIs affect many people — over 150,000 Canadians in 2018. Because some can be asymptomatic, STIs can be transmitted without knowledge. It can also be hard to track who an STI came from, and even harder to inform sexual partners that you have an STI. MySTIc aims to combat lack of knowledge about STIs and safe sex, as well as the stigma that can prevent people from informing others that they have an STI.
<br><br>
The COVID-19 tracking app was an inspiration to us, because it allowed people to find out if they had been near someone who tested positive for COVID-19. Our app had to be different because while COVID-19 can be spread without any kind of physical contact, STIs are transmitted in a more intimate way. So, we decided to use the COVID app as inspiration but made many tweaks.

### What it does
MySTIc will allow users to:
* Inform sexual partners anonymously if they test positive for an STI by sending them a text message
* Inform the receiver if the STI is HIV, because HIV can potentially be prevented if treated within 72 hours using post-exposure prophylaxis
* Get notified if recent sexual partners have had an STI
* Get information on clinics near you and how to get tested
* Get information on different STIs

### How we built it
We first created a mockup and prototype using Figma. This prototype showed how the mobile app would work and how the chat bot would work in a browser. We then learned how to use the Co:here API using their documentation and tutorials, and we decided to use the Generate and Classify endpoints. We used Python, Co:here, Repl.it, and Github to collaborate in creating the backend software of the chat bot.

### Challenges we ran into
One challenge we ran into was using the Google Maps API and Co:here to find locations near the user where they could get tested for STIs. The problem was that some locations would show up in a Google Maps search that were related to sexual health, but did not offer testing for STIs.
<br><br>
Another challenge we ran into was using certain words with Co:here. Using words like ‘penis’ or ‘sex’ gave us a Co:here error that our prompts violated the User Agreement. While this makes sense to prevent Co:here users from using derogatory or harmful language, it posed a challenge for our use case. This was overcome by providing prompts that use different language, but it is not practical to expect users to use words not related to genitals or sex.

### Accomplishments that we're proud of
We are proud of the idea we had, since it's in line with our personal values of encouraging safety, health, and education, while also contributing to the destigmatization of sexual health. We are also proud of the steps we took to create prototypes of our mobile app and chat bot. Lastly, we're proud that we were able to actually write functional code for our chat bot's backend, especially since we quickly learned to use Co:here for our project from scratch.

### What we learned
We learned how Co:here works and how much we can do with it. We first learned to use Co:here when we were using the Classify portion of it to classify different types of questions that the chat bot could be asked. We later learned to use Co:here Generate to generate key words from a user’s inquiry and to generate text messages to users.

## What's next for MySTIc
* Flask will be used to create the front end of the application in a way that matches the Figma prototype.
* Use a service like Twilio to send messages from the app to users.
* Once MySTIc gains more traction and enough people start using it, notifications can be sent through the app itself rather than through text messages.

### Built with
* Python
* Co:here
* Figma
* Git/Github

View Figma designs here: https://www.figma.com/file/q8YYMDov5nQOfm0BWMvGya/MySTIc?node-id=0%3A1&t=ZkwwSbw5L2bhDhuh-0
