

default sus = 0


#FIRST GROUP
define pm = Character("Praying Mantis", color="#43AC3D", what_color="#43AC3D")
define z = Character("Zombie", color="#D78AC2", what_color="#D78AC2")
define t = Character("Tentacle", color="#EBAADA", what_color="#EBAADA")


#SECOND GROUP
define g = Character("Ghost", color="#DFDAAF", what_color="#DFDAAF")
define d = Character("Dinosaur", color="#4D8C49", what_color="#4D8C49")
define v = Character("Vampire", color="#A3BBE3", what_color="#A3BBE3")

image dino:
    # zoom 0.9
    "dino.png"

image vampire:
    zoom 0.8
    "vampire.png"

image witchK:
    zoom 1.4
    "Kseniawitch.png"

image witchR:
    zoom 1.4
    "Ruxiwitch.png"

#THIRD GROUP
define bw = Character("Black Widow", color="#D04C4C", what_color="#D04C4C")
define s = Character("Sphinx", color="#E3B92A", what_color="#E3B92A")
define m = Character("Merperson", color="#45C688", what_color="#45C688")


#WITCHES
define wr = Character("Witch 1", color="#A3BBE3", what_color="#A3BBE3")
define wk = Character("Witch 2", color="#E3B92A", what_color="#E3B92A")

#IMAGES

image tentacle:
    zoom 0.5
    "tentacle.png"

image widow:
    zoom 0.8
    "widow.png"

image sphinx:

    "sphinx.png"

image zombie:
    zoom 0.9
    "zombie.png"

image mermaid:
    zoom 0.9
    "mermaid.png"

image ghost:
    zoom 0.7
    "ghost.png"

image mantis:
    zoom 0.9
    "mantis.png"


image snow:
    zoom 0.8
    "snow.png"

image bar1 = im.Scale("barBG.jpg", 1280, 720)
image barCrowded = im.Scale("bgWitches.jpg", 1280, 720)
image barLux = im.Scale("bgHoodie.jpg", 1280, 720)

image heart = "heart.png"
image heartBreak = "heartBreak.png"
image introSkip = "Intro/skipIntro.png"

#HAPPY ENDINGS

image tentacleEnding:
    zoom 0.7
    "he/tentacleEnding.png"

image zombieEnding:
    zoom 0.7
    "he/zombieEnding.png"

image vampireEnding:
    zoom 0.7
    "he/vampireEnding.png"

image mermaidEnding:
    zoom 0.7
    "he/mermaidEnding.png"

image sphinxEnding:
    zoom 0.7
    "he/sphinxEnding.png"

image dinoEnding:
    zoom 0.7
    "he/dinoEnding.png"


#GAME OVERS

image over:
    zoom 0.7
    "go/over.png"

image overGhost:
    zoom 0.7
    "go/overGhost.png"

image overMantis:
    zoom 0.7
    "go/overMantis.png"

image overWidow:
    zoom 0.7
    "go/overWidow.png"


label start:

#INTRO
    play music "audio/windIntro.mp3"
    scene introSkip

    menu introSkip:
        "Watch the intro":
            jump intro

        "Skip intro":
            jump firstDate

label intro:
    play music "audio/windIntro.mp3"

    scene snow
    pause

    play sound "audio/introNar/intro1.mp3"
    "It's a frosty winter's night"
    play sound "audio/introNar/intro2.mp3"
    "Your feet are cold."
    play sound "audio/introNar/intro3.mp3"
    "Your ears are cold."
    play sound "audio/introNar/intro4.mp3"
    "You can't remember the last time you felt your hands."
    play sound "audio/introNar/intro5.mp3"
    "A sultry light at the end of the street catches your eye."
    play sound "audio/introNar/intro6.mp3"
    "You follow it."
    play sound "audio/introNar/intro7.mp3"
    "It's a pub."
    play sound "audio/introNar/intro8.mp3"
    "Craving warmth, you enter."

    jump introPub


label introPub:
    play music "audio/Intro.mp3"
    $renpy.music.set_volume(0.4, delay=0, channel='music')

    scene barCrowded
    pause

    play sound "audio/introNar/intro9.mp3"
    "Ah. Warmth"
    play sound "audio/introNar/intro10.mp3"
    "Oh shit! What the hell is that smell?"
    play sound "audio/introNar/intro11.mp3"
    "It's a monster pub!"
    play sound "audio/introNar/intro12.mp3"
    "You need to get out...before the monsters realize that there is a human among them."
    play sound "audio/introNar/intro13.mp3"

    "Fortunately, your skin looks remarkably unhealthy from your lifestyle of gaming and staying indoors 24/7"
    play sound "audio/introNar/intro14.mp3"
    "You can fit in here. Maybe even pass as a zombie."
    play sound "audio/introNar/intro16.mp3"
    "That won't be easy. You need a plan. But...what is this?!"
    play sound "audio/introNar/intro17.mp3"
    "There is a flyer that says...TONIGHT: SPEED-DATING NIGHT!"
    play sound "audio/introNar/intro18.mp3"
    "This is your chance!"
    play sound "audio/introNar/intro19.mp3"
    "You will meet 3 random monsters during speed dating. Charm them to escape the pub in their company."
    play sound "audio/introNar/intro20.mp3"
    "Don't let them know you're human. Watch the suspicion bar at the top right to see how suspicious of you the monsters are. "
    play sound "audio/introNar/intro21.mp3"
    "Replay to unlock more monster characters & endings."
    play sound "audio/introNar/intro22.mp3"
    "Good luck."


    show screen bars
    $ sus += 10




    menu startGame:
        "START DATING":
            jump firstDate




label firstDate:

    #play music "audio/Intro.mp3"
    scene barCrowded
    $ sus +=20

    #pause

    $ char1 = renpy.random.randint(1, 3)

    if char1 == 1 :
        jump mantis
    elif char1 == 2:
        jump zombie
    else:
        jump tentacle

label mantis:
    play music "audio/1Dialogue_Jazzy_Music.mp3"

    # $ susCount = 0
    scene barCrowded

    show mantis
    show screen bars
    pm "May God be with you on that beautiful, cold winter’s day."
    pm "My name dear is Mantis Theresa and I am, as thou might have noticed, a praying mantis."
    pm "Let’s praise all of God’s creations in this diverse, divine world and blessed may be the fruit of all."
    pm "Especially, when they have such an interesting appearance such as yours."
    pm "Stranger, praytell something of thine heart!"
    pm "What’s in thy soul, my dear?"

    menu manty1:

        "In my soul? Actually, I am not sure. Which God are you even talking about?":
            $ sus += 10
            # $ susCount += 1
            pm "An Atheist, I see."
            pm "As confusing as thy life might be without proper guidance of the divine force of God, I respect thy choice of not believing in anything..."
            pm "Even though thine soul is doomed to eternal damnation."

        "Lovely Mantis Theresa, blessed be thy day as well! My beliefs are certainly matching thine and I am sure it’s God’s will that our paths have crossed.":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            pm "A lovely response, from a lovely looking being."
            pm "I am sure it was God’s plan all along. I am delighted, my dear."

    hide mantis
    show witchR with easeinright
    wr "Hi there fellow speed-daters, is there anything I can bring you?"
    hide witchR
    show mantis


    menu manty2:

        "My dearest sister, would you be so kind and fetch me a glass of the sweet juice of our Lord and Savior Jesus Christ?":
            $ sus += 10
            # $ susCount += 1
            pm "BLASPHEMY! How dare thou drag the name of our saviour through the mire. Waitress? Fetch me a drink, I am boiling!"

        "May I have some of your finest tap-water please? I am thirsting for something cool and wet running down my throat.":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            pm "A person of health, I see. I am impressed by thy drinking choices. Keeping your flesh clean and pure. Thy body is a temple after all."

    pm "Anyhow, you seem to have a good head on thy shoulders."
    pm "What do thou seek to find in this crowded place?"
    pm "Is it pure and never-ending love? Most beings solely wish to indulge in their lustful urges."

    menu manty3:
        "Lustful urges? No, no and a thousand times no! My pure body should only be touched by the right being, The One if you will. My body is a temple and not a filthy one.":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            pm "My dearest that sounds amazing!"
            pm "Then let’s leave this dirty establishment and let’s enrich ourselves by praying together."
            pm "Come to me, my sweetheart."
            pm" Let’s hug it out, right here."
            jump mantyEnd

        "Ehm.. actually.. I didn’t even plan on going speed-dating, I’m not looking for a partner. I just came with a friend. I might not be the right person, I do not think it was meant to be, after all?":
            $ sus += 10
            pm "That’s alright my sweetest."
            pm "T’is a pity, however, I shall pray for thou salvation."
            pm "I am Mantis Theresa, after all."
            pause
            jump secondDateIntro


label mantyEnd:
    play music "audio/Intro.mp3"
    hide screen bars
    scene introSkip
    show overMantis
    pause
    return

label zombie:
    play music "audio/1Dialogue_Jazzy_Music.mp3"
    scene barCrowded
    show zombie
    show screen bars
    z "Shall I compare thee to a summer's day, stranger?"
    z "Thou art more lovely and more…"
    z "Wait thou smell peculiar…"
    z "What type of monster are thou exactly?"


    menu zomby1:

        "Uhh… You couldn’t have heard of me. I don't go out much. I’m kind of a cryptid.":
            $ sus += 10
            z "Ah. How disappointing. But oh well… To each their own"

        "Good sir, how surprised I am that your senses have not picked up on my appearance. I am most often burdened with my fame, but this one time I can present myself to you without any prior judgement, and for that I am honored":
            $ sus -= 5
            show heart
            pause 0.5
            hide heart
            z "Oh good sir, what a pleasure it is to encounter someone of such eloquence."
            z "I’m sure we’ll have plenty of stimulating... discussions"

    z "So… Mysterious stranger"
    z "Would you consider warming this cold undead heart and reciting me a poem of your choosing?"

    menu zomby2:

        "Okaay… Roses are red… Violets are blue… You’re a dead guy... Sucks to be you":
            $ sus += 10
            z "How very crude… Your manners, sir, are almost as upsetting as your poetic abilities"

        "Your heart is cold, it doesn’t beat… My heart is warm, but it’s in pain… For I have seen a corpse so neat… And you’re driving me insane.":
            $ sus += 10
            z "Oh… How very forward of you..."
            z "But your sensitive soul is shining through…"
            z "I am impressed, stranger"

    z "Answer me this last question, stranger…"
    z "Assuming we leave this lowly bar a unit..."
    z "What type of journey shall we embark upon together?"

    menu zomby3:

        "Well I for one can’t wait to take you to the Wörthersee lake and spend the whole day stand up paddling and reciting Shakespeare to each other":
            $ sus += 5
            z "How cruel of you, stranger..."
            z "I thought we might share a special connection, but you mock me with your suggestion."
            z "Do you not see my decaying state?"
            z "How foolish of you to assume that I might go… What is it?"
            z "Stand up paddling you said?"
            z "Bother me no longer. Farewell."
            jump secondDateIntro

        "Dude I don’t even need to think about it. You. Me. Lil Nas X concert.":
            $ sus -= 5
            show heart
            pause 0.5
            hide heart
            z "Say no more, stranger."
            z "You have said all the right words."
            z "Let’s leave at once."
            jump zombyEnd


    return


label zombyEnd:
    play music "audio/GoodEnding.mp3"
    hide screen bars
    scene introSkip
    show zombieEnding
    pause
    return

label tentacle:
    play music "audio/1Dialogue_Jazzy_Music.mp3"

    $ susCount = 0
    scene barCrowded
    show tentacle
    show screen bars
    t "Oh god! I am all stiff from being crammed into this jar. It’s just a bit small for my girth..."
    t "Please tell me you are not just another one intimidated by my phallic shape?"
    t "This Freudian penis envy is so exhausting!"
    t "I just wanna have some casual conversation about contemporary psychoanalysis theory, but everyone here is just intimidated by me I guess."
    t " I am so hungry…"
    t "for intellectual conversation."



    menu tenti1:
        "I think Freud’s hypothesis of sexual envy projected towards the parent of the opposite sex is a widely  overestimated concept. It is overly simplistic in its understanding of gender, treating it as a simple binary that is entirely defined via one´s genitalia, and ignoring anything that doesn't fit within this rigid paradigm. It´s a laughable theory, in fact.":
            $ sus += 5
            $ susCount += 1
            t "...seems like you are quite familiar with the theory..."
            t "which is unusual for a fellow monster…."

        "To be honest I don’t feel intimidated at all...just turned on.":
            #$ sus += 10
            t "Back off...I am not looking for that sort of stimulation."
            t "Although fair enough, I was the one talking about genitals."


        "That is so fascinating! Please tell me more about those theories!":
            $ sus -= 10
            show heart
            pause 0.3
            hide heart
            t "Well, I don’t want to bore you, you don’t seem very….intellectual."
            t "But, oh, alright! What harm is there in enlightening the simpleminded!"
            t "I don’t mean to brag, but I was actually a professor at a very prestigious University..."
            t "Some even said I was the best professor that department had ever seen..."
            t "I wouldn’t know if that’s true of course..."


    #A witch comes over and asks you about drink orders

    hide tentacle
    show witchR with easeinright
    wr "Would you two like something to drink?"
    hide witchR
    show tentacle

    menu tenti2:
        "Pick a Margarita":
            $ sus += 10
            $ susCount += 1
            t "...does this….does this have SALT in it?"
            t "*pause*"
            t "I’m sorry, this is not gonna work out."

        "Pick a fine aged Whiskey":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            t "You really do have a fine taste, did anyone ever tell you that?"

        "Pick a Red Wine":
            t "Ah, what a fine drop..."
            t "Its flowery palette reminds me of the time I spent studying in Athens…."
            t "A young tentacle I was, and still untouched...ah, how time flies."
            t "I still remember it like it was only yesterday..."


    if susCount == 2:
        jump tentiEnd

    menu tenti3:
        "So...I really feel a connection here.Would you like to join me for a night at the opera? Dr. Faustus is playing tonight.":
            t "Uhhh... I feel like looking around some more..."
            t "Sorry..."
            jump secondDateIntro

        "Honestly, it seems like you just need to let loose for a night. How about we go back to my place? Release our suppressed desires together? In a Freudian sense, if you will...":
            $ sus += 10
            t "How dare you try and teach me about Freud! Good day!"
            jump secondDateIntro

        "How about we hit up a techno club right now? I could really use some smacking beats right now...just wanna let loose, you know?":

            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            pause
            #winning screen game over
            jump tentiWin




label tentiWin:
    play music "audio/GoodEnding.mp3"
    hide screen bars
    scene introSkip
    show tentacleEnding
    pause
    return


label secondDateIntro:

    $ sus += 20
    scene barLux
    show screen bars
    show witchR with easeinright
    wr "Don't you worry, sweetie!"
    wr "We'll help you find someone more suitable for you!"
    wr "You just make sure to keep your eye on that bar..."
    wr "By bar I mean 'The Four Witches of Klu Jam Bar', of course "
    wr "*winks*"
    wr "The next date we have lined up for you is quite something!"
    wr "Have fun, sweetie!"

    #jump vampire

    $ char2 = renpy.random.randint(1, 3)

    if char2 == 1 :
        jump ghost
    elif char2 == 2:
        jump dinosaur
    else:
        jump vampire


label vampire:
    play music "audio/2Dialogue_Jazzy_Monster_Default.mp3"
    # $ susCount = 0
    scene barLux
    show vampire
    show screen bars

    v " 'Sup? Name's Regis: Chaderick the first, but everyone calls me Regy."
    v "Imma be straight with you, literally (hehe)."
    v "I'm really into lifting and stuff... so..."
    v "Do you even lift bruh?"

    menu himbo1:
        "Check out my super ripped body. My guns poke through my shirt, bruh. *takes shirt off and flexes*":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            v "Yo daug, put them guns away, they’re fucking dangerous dude! *blushes* "

        "Are you trying to communicate? I can’t tell. Are those real words you’re saying?":
            $ sus += 10
            v "Bruuuuuuuuh! Fitness slang's not your strong suit, eh?"

    v "Whatever, I miss the sun bruh."
    v "My skin hasn’t seen sunlight in fucking centuries. This is not lit dude. I look so pale, man."
    v "Got any Vitamin D??"
    v "My body has been deprived of the D, bruh!"
    v "I NEED THE D! ......... no homo."

    menu himbo2:
        "Dude! I think I might have something even better for ya. Have you heard of spray tan? It’s super lit!":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            v "Whaat? You got something like that for me?"
            v "I'm starting to like you, brah."

        "Okay… I didn’t know vampires could get so undignified. What are you even wearing?":
            $ sus += 10
            v "Don't fucking tear down my wardrobe, bruh! I got that tank from my mum! She’s tha best, so fuckin’ step down!"


    v "Anyway, lately I’ve been really into protein shakes.."
    v "Ya know, eating healthy, strengthening my body."
    v "I mean YOLO right? Not literally because I live forever (hehe) but ya get the vibe, right?"

    menu himbo3:
        "Sure dude! Never skip leg day! I literally try to live long because YOLO, forreal. As my favorite sandwiches brand always says - Eat Fresh - right? (hehe)":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            "Dude! Sandwiches? I am starving! Let’s get out of here and fucking eat!"
            jump himboEnd

        "No, actually I don’t get the vibe. How old are you? 12? Talk like a grown-up or don’t talk at all!":
            $ sus += 10
            "No need to be rude bruh. I’m not talking about your weird-looking body so STFU!"
            jump thirdDate


label himboEnd:
    play music "audio/GoodEnding.mp3"
    hide screen bars
    scene introSkip
    show vampireEnding
    pause
    return

label dinosaur:
    play music "audio/2Dialogue_Jazzy_Monster_Default.mp3"
    $ susCount = 0
    scene barLux
    show dino
    show screen bars

    d "Hey buddy..."
    d "Sorry, I’m taking up so much room"
    d "It’s always the same with my body shape."
    d "I didn’t even wanna come here tonight..."
    d "But my Dad said I should go out and socialize some more..."
    d "He’s really worried about me, you know?"
    d "Says I should find love...but I don’t really fit in here..."
    d "I mean it’s not even the right age for me..."
    d "I belong in the late jurassic period!"
    d "But here I am now, the product of scientific experimentation with cloning..."

    menu dino1:
        "Sounds like you’re in a bit of an existential crisis there, buddy...":
            $ sus += 10
            $ susCount += 1
            d "I knew it was a mistake coming here! You see right through me!"

        "Well you found the right person, er…..I mean creature, then! I don’t belong here any more than you do.":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            d "I thought you looked a bit too human for this place..."
            d "Don’t worry though, I won’t eat you, I’m a convinced herbivore. It goes against my principles."


    d "Well, I guess we should get to know each other a bit then...what do you like to do in your spare time"

    menu dino2:
        "I'm a vegan":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            d "Oh how exciting!"
            d "Carnivore’s are so weird to me."
            d "The blood, the flesh, the taste of the dead..."
            d "I mean, how could you even think of eating a decaying body. It’s just gross to me."

        "I’m really into techno music.":
            $ susCount += 1
            $ sus += 10
            d "Oh, no, no no, techno music is so aggressive. I am more of a Jason Mraz fan, honestly."


    menu dino3:
        "I get the feeling that you would rather be someplace else, and I feel the same way. Should we go grab some vegan burgers?":
            d "Actually, I am starving myself and this bar doesn’t serve anything veggy. Let’s go eat plants."
            jump dinoEnd

        "You know, of all the creatures in here, you are the nicest one for sure. What do you say, should we take our relationship to the next level?":
            $ sus += 10
            d "That’s so flattering, but I really just wanna stay friends."
            jump thirdDate


label dinoEnd:
    play music "audio/GoodEnding.mp3"
    hide screen bars
    scene introSkip
    show dinoEnding
    pause
    return

label ghost:
    play music "audio/2Dialogue_Jazzy_Monster_Default.mp3"
    scene barLux
    show ghost
    show screen bars

    g "WHAT THE FUCK, DUDE!?"
    g "Okay, don’t lose your shit but I am human too!"
    g "I know it’s a pretty good disguise, right?"
    g "Those monsters before didn’t even flinch at me. But forreal - how are you still alive?"
    g "You don’t even have a proper disguise?! OMFG do you wanna get both of us killed?"
    g "I AM NOT READY TO DIE! I just reached 1K Followers on Instagram! I am not ready to give that up!"

    menu ghosty1:

        "Phew! Another human, thank god! What do we do? Should we try to escape?":
            g "YES DUDE!"
            g "Let’s get out of here!"
            g "They can smell fear and... I hate to admit it but I just shat my pants."

        "Ehm.. actually I am here to find real love, but I’m not interested in humans.. Awkward..":
            g "Real love?!"
            g "At this place?!"
            g "WHAT THE FUCK IS WRONG WITH YOU??"
            g "Is this some kind of a kink? Am I on national TV?"
            g "Those dudes will eat us alive! Let’s plan an escape!"

        "Who even uses Instagram anymore? Everyone’s on TikTok nowadays.. Where do you live? In a cave?":
            g "Don’t fucking judge my social media preferences!"
            g "I am about to make it big!"
            g "But whatever, we need to get out of here!"

    g "So.."
    g "What do we do?"

    menu ghosty2:
        "How should I know? I am fucking losing my shit here!":
            g "Do you even think we could escape together?"
            g "Or should we stick to some of the monsters to get out of here?"
        "Ok, let’s think.. let’s splash ourselves with drinks so we reek of alcohol, produce some weird monster sounds to blend in and then fucking run to the exit?":
            g "Do you even think we could escape together?"
            g "Or should we stick to some of the monsters to get out of here?"

    g "I want to live! I AM NOT READY TO GO! NOT LIKE THIS!"


    menu ghosty3:
        "Ok, let’s fucking run!":
            jump ghostyEnd

        "I am not going down with you! I’m gonna seduce the next monster I see and try to get out of here with them! Good luck, loser!":
            jump thirdDate



label ghostyEnd:
    play music "audio/Intro.mp3"
    hide screen bars
    scene introSkip
    show overGhost
    pause
    return

'''
    "You try to escape with the weirdly looking ghost who shat its pants but you don’t make it to the door."
    "Your effort of splashing yourselves with alcohol while making monster sounds terribly fails."
    "The monsters catch you both and kill you in an instant."
    "People in the bar shortly bat an eye but soon return to their usual business. "
'''

label thirdDate:
    $ sus += 10

    play music "audio/3Dialogue_Jazzy_Music.mp3"
    scene bar1
    show screen bars
    show witchK with easeinleft

    if sus >= 90:
        wk "Oh, sorry, pumpkin, looks like everyone is looking at you a certain way..."
        jump gameOver

    wk "What are you still doing here exactly?"
    wk"You have a deathwish, pumpkin?"
    wk"Well... You know what they say..."
    wk"Third time's the charm!"
    wk"You're about to meet someone really...really interesting"
    wk"Take care, honeybun"



    $ char3 = renpy.random.randint(1, 3)

    if char3 == 1 :
        jump blackWidow
    elif char3 == 2:
        jump sphinx
    else:
        jump mermaid



label blackWidow:
    play music "audio/3Dialogue_Jazzy_Music.mp3"
    #$ susCount = 0
    scene bar1
    show widow
    show screen bars

    bw "You look delicious tonight. Does the curtain match the drapes?"

    menu bw1:
        "...excuse me?":
            $ sus += 10
            bw "One's lifestyle choices influence one’s health."
            bw "I am looking for a healthy partner, my apologies for being so blunt."
            bw "After all, it is a speed-dating night."

        "Care to find out?":
            $ sus -= 5
            show heart
            pause 0.5
            hide heart
            bw "Yes, and as soon as possible."
            bw "Before the night is over, we’ll know each other inside out."

    bw "So, tell me, do you like to engage in….unhealthy activities?"

    menu bw2:
        "Well, I have been a smoker for almost half a decade now...":
            $ sus += 10
            bw "Oh, how very unfortunate..."

        "No, no. I am as healthy as they get!":
            $ sus -= 5
            show heart
            pause 0.5
            hide heart
            bw "Mama likey!"

    bw "Well I’m gonna cut to the chase..."

    menu bw3:
        "I’m gonna stop you right there. Take me home.":
            bw "Don't mind if I do"
            pause
            jump overWidow

        "IHAVABOYFRIEND!!!!!!":
            bw "Okurrrrrrrr"
            pause
            jump gameOver


    return


label overWidow:
    play music "audio/Intro.mp3"
    hide screen bars
    scene over
    show overWidow
    pause
    return


label sphinx:
    play music "audio/3Dialogue_Jazzy_Music.mp3"
    # $ susCount = 0
    scene bar1
    show sphinx
    show screen bars

    s "Finish the sentence. A sphinx walks into a bar looking for a cute date…"

    menu sphinxy1:
        "She stops looking as soon as she lays her eyes on me *winks*":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            s "*winks back*"
        "She leaves alone because no one likes riddles...":
            $ sus += 10
            s "Eh. How stereotypical…"
            s "Riddles are so 2500 BC."
            s "It’s all about standup with Sphinxes now, sweetie. Keep up."

    s "Knock..."
    s "..."
    s "...knock"

    menu sphinxy2:
        "Who’s there? *under your breath* …please kill me...":
            s "A classy and surprisingly attractive for her age mythical being"

    menu sphinxy3:
        " 'a classy and surprisingly attractive for her age mythical being' - who?":
            s "uh... I actually don’t have a punch line for that one, but..."

    s "Are you just window shopping, pretty thing, or are you here to make a... purchase?"

    menu sphinxy4:

        "I actually think I prefer my Sphinxes speaking in riddles…":
            $ sus += 10
            s "And I prefer dull strangers to keep their opinions to themselves."
            s "But I guess we both can’t get what we want, boo."

        "Hey there...Please take my credit card, no refunds, mam":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            s "Card approved, sweetheart"

    s "Here’s a final riddle for you, handsome."
    s "Who has two paws, a top notch sense of humor and is going to go home tonight with a dinner...?"
    s "um… DATE! I meant date!"

    menu sphinxy5:

        "That hot werewolf over there?":
            $ sus += 10
            s "Huh?"
            s "Who? Frank?"
            s "I'm afraid you’re not really his type, cutie pie, but go ahead, shoot your shot."
            s "See ya."
            jump gameOver

        "Hm… Well there is a huge PAWsibility, ‘tis might be you, mam":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            s "You better not be kitten around, then, pumpkin, let’s get out of here"
            jump sphinxEnd


label sphinxEnd:
    play music "audio/GoodEnding.mp3"
    hide screen bars
    scene introSkip
    show sphinxEnding
    pause
    return





label mermaid:
    play music "audio/3Dialogue_Jazzy_Music.mp3"
    $ susCount = 0
    scene bar1
    show mermaid
    show screen bars

    m "Wow, finally someone I can get on board with! Pun intended!"
    m "My scales were getting kind of dry with all these monsters around..."
    m "But you look ...almost human I have to say!"
    m "To be honest with you, I prefer human lovers..."
    m "But I kept finding them at the bottom of the ocean after a day or two, sadly."
    m "I thought I’d switch to dating monsters now, but wow, here you are"

    menu mermy1:
        "I guess you could say I have a human...quality. But other than that I am totally a monster, as well. Sorry to disappoint you here.":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            m "You’re not disappointing at all. I love your squishy, soft skin. And guppy, your legs just do it for me."

        "What? Ehm... human? I am sure you confuse me with someone else, because I have no human qualities. Look at my unhealthy pallor, do you think a human would look like this?.":
            $ sus += 10
            m "Mhmm.. okay, lol."


    m "Nonetheless, you apparent non-human being..."
    m "Please tell me, what do you like to do in your spare time, my friend?"

    menu mermy2:
        "My spare time? You know, the usual - taking a walk in the local park and shopping, basically. My wardrobe like always needs an update.":
            $ sus += 10
            m "Clothes and walks, huh? Not kinda my vibe.. because you know.. I cannot walk lol"

        "As a stereotypical monster. I really love music. Also, there’s this one band which comes to my mind while talking to you - 'The Long Johns'!":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            m "I really love music as well. Not to brag but I am quite the singer myself."


    m "Alright, I feel like I know you a little bit better now..."
    m "But my most important question would be what would our perfect date look like?"
    m "Give me something creative here.."
    m "Life is so boring anyway..."

    menu mermy3:
        "Uh yeah, we could just go out and wander around.. See what’s out there?":
            $ sus += 10
            m "Wander. Around. Town? *gestures meaningfully at herself* Ok lol."
            jump gameOver

        "You know…there’s a karaoke place nearby. Should we get over there and go nuts?":
            $ sus -= 10
            show heart
            pause 0.5
            hide heart
            m "Oh. My. God. You just get me! Le’t fucking go!"
            jump mermyEnd




label mermyEnd:
    play music "audio/GoodEnding.mp3"
    hide screen bars
    scene introSkip
    show mermaidEnding
    pause
    return


label gameOver:
    play music "audio/Intro.mp3"
    hide screen bars
    scene introSkip
    show over
    pause
    return




    #return
