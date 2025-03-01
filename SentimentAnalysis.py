from transformers import pipeline

# Load pre-trained sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

# Run sentiment analysis
text = "I love this product! It's amazing."
result = sentiment_pipeline(text)
print(result)  # Example output: [{'label': 'POSITIVE', 'score': 0.999}]

sentiment_pipeline = pipeline("text-classification", model="yiyanghkust/finbert-tone")

# Famous Haribo Amazon Review
text = """
It was my last class of the semester, and the final exam was worth 30% of our grade.
After a late night study session I felt confident, but I had to decide between sleeping in or cooking breakfast. My eyelids chose sleep.
My stomach later regretted this decision, and after several uncomfortable stomach growls, I finally decided to make a quick stop by the campus bookstore and grab a snack before my test. Since the semester was ending and everyone was going home for the summer, a lot of items were on sale, including the snacks and candy that they kept up front. Being in the hungry state that I was in, it felt only logical to pick the largest, yet least expensive candy in order to get more bang for my buck.
And there they sat: two bags of Haribo Sugar-Free Gummi Bears, buy one get one free.
"What a deal!" I thought naïvely. I would eat one bag before my test, and one bag afterwards.
As I walked to class, I gleefully chewed on those abominable little bastards, unaware of the utter mayhem that they would soon unleash upon my poor, poor anus.
I sat down at my desk as the professor informed us that, due to issues with cheating in the past, restroom breaks would be prohibited until the completion of the exam.
"I'll give you 10 minutes to use the restroom now; this will be your last chance. Any takers?"
The demon bears hadn't released their unholy necromancy upon my stomach yet, so in my moment of ignorant foolishness, I remained seated, still munching on those miniature bear-shaped bombs.
After the students wise enough to take the professor's offer had returned, the professor handed out the test. I was six questions in when it happened.
It started subtly at first, almost like a slight tingly sensation in my lower abdomen. I thought nothing of it, assuming my intestines were just doing their thang. Little did I know that my intestines were trying desperately to warn me of the horror that was on the horizon.
By question 9 it happened again, but this time it was followed by a sharp pain, as if those infernal hellions had orchestrated an attack upon my colon. I fought to contain the groan that tried escaping my lips. It was at this point I began to panic; something was going horribly long, and I needed to get through this test before it got any worse.
By question 14 my worst fear was upon me; the Satan bears' burning, hot, liquidy dark magic crashed against my anal sphincter like a tidal wave. I was able to close the hatch just in time, but those relentless, toxic bears beat against it like Orcs breaking down the doors of Helm's Deep. I knew I wouldn't be able to so much as shift in my seat without risking a breach.
I kept fighting through my exam, clenching my cheeks with all my might. Beads of sweat began rolling down my neck. Suddenly, a loud, gurgling war cry came from my belly, and the entire class lifted their heads.
At this point, nothing mattered except expelling this ungodly presence from my bowels. With 15 questions left, I promptly wrote C for every answer and ran out of the classroom. My professor yelled something, but I was too preoccupied with the volcanic eruption that needed to take place before I could find sweet, sweet relief.
I burst into the restroom like the Kool-Aid man and, behold, the handicap stall was empty. Sun rays from the adjacent window shone upon it, as if it were a gift from God himself. It took me less than .5 seconds to undo my belt buckle, pull down my pants, and finally relax my weary buttocks upon the toilet seat.
It took absolutely no effort to expel this demon. Almost immediately, the floodgates of hell were opened and the damned, liquified souls of an entire bag's worth of gummi bears cried as they burned through my sphincter and into the watery abyss below. I had never felt such simultaneous relief and anguish in my life.
After 30 more minutes of this, I immediately went home, dug a hole in my backyard, and burned the remaining bag of gummi bears.
I leave with this; do not, I repeat do NOT eat these spawns of Satan. Not only did they cause me to fail my final test, but the anguish I experienced is something I wouldn't wish upon anyone, not even my worst enemy. The only place these god forsaken hell bears belong are buried deep below the Earth's surface."""

result = sentiment_pipeline(text[:512])
print(result)

result = sentiment_pipeline(text[-512:])
print(result)