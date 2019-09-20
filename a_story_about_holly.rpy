label scenario_a_story_about_holly:
    "This is a basic draft"


$ config.developer = True


label diguedong:
    $ h_holly.name = "Holly"
    $ sandra.name = "Mom"
    $ cassie.name = "Cassie"
    $ scarlet.name = "Scarlet"

    outfit h_holly casual
    play music h_bgm_arms
    show h_holly a_5
    think "My name is Holly Davis, i live with my brother John and my mother Sandra. I'm currently attending collage"

    scene bg holly room dark
    play sound sfx_knock
    sandra "Honey, have you not awaken yet?"
    sandra "HONEY??"
    "..."
    play sound sfx_knock
    "..."
    sandra "I'm coming in!"
    accessory sandra bedhead
    show sandra a_3 at centerright, faceleft
    sandra "For goodness sake Holly, it's time to wake up. You're usually up by now..."
    think "what"
    outfit h_holly nude 
    show h_holly a_35 at centerleft, faceright
    holly "UuuuuhHHUU, good morning?"
    holly "Oh mom, I'm up.."
    sandra "Sure. Are you okay?"
    show h_holly a_8
    holly "Yeah... somewhat, we were out on a collage get-together yesterday and i must've drank an aweful lot ugh."
    think "Jesus christ i'm terribly nauseous. TOILET NOW"
    holly "Uh i think i need to puke..."
    show sandra a_8
    "Mom giggle slightly"
    sandra "Come down for breakfast once you're okay."
    hide sandra with easeoutright
    scene black with fade
    scene bg main bathroom day
    play sound sfx_door_open
    show h_holly a_7 at center:
        alpha 0.2
        ease 1.5 xpos 0.9 alpha 1.0
        xpos 0.9
        alpha 1.0
    "I ran towards the toilet with haste"
    play sound sfx_stomach_growling
    show h_holly a_0 at center:
        xpos 0.9
        alpha 1.0

    think "Yuck. I should really hold back on the drinking next time... My head... "
    "I washed up and headed for my room"
    hide h_holly with easeoutleft
    scene black with fade
    scene bg holly room day
    think "HOLY SHIT IT'S ALREADY 9"
    "I quickly throw yesterday's outfit on."
    outfit h_holly casual
    show h_holly a_1 at center
    think "What even happened yesterday? i recall after the last lecture heading towards {q}The Boar's Nest{/q} together with Cassie, Elizabeth and Scarlet."
    think "We were going to have a chat about this weeks classes, then head home quietly."
    show h_holly a_4
    play sound sfx_explosion
    think "Wait a fucking minute did that really happen?"
    show h_holly blush a_7
    think "Fractions of yesterday's memories are starting to flood back into my head. Images of me sitting in Cassie's lap, singing to the tunes of {q}Drunken Sailor{/q}. Oh god good what have i done."
    think "Oh my, i need to apologize to Cassie today. I hope she isn't mad at me.."
    hide h_holly with easeoutright
    scene bg main kitchen day
    show sandra a_0 at centerright
    show h_holly a_0 at centerleft with easeinleft
    "Mom was pouring a cup of black coffe and placing it on the table."
    think "It smells great, is that pancakes?"
    sandra "Hi sweetie, are you feeling better?"
    holly "My head is killing me. do we have any painkillers around?"
    "Mom starts rampaging through the upper cabinet, she finds a pack of Ibuprofen. She then reaches over to the other cabinet and takes out a glass and fills it with water."
    show sandra a_1
    sandra "Here sweetie"
    "She hands me the glass and a tablet"
    play sound h_sfx_swallow
    holly "gulp gulp, Haaahh..~ "
    holly "Thanks mom."
    sandra "You're welcome sweetie, your coffe is on the table. I'll come with a plate of pancakes in a bit"
    show sandra a_0 at Position(xpos = 0.35) with move
    show h_holly at Position(xpos = 0.75, ypos = 1.3) with move
    "Mom rummaging through the shelves for a plate, she grabs a few pancakes and put them on the platter"
    show sandra a_1 at Position(xpos = placement_of(h_holly).xpos) with move
    sandra "Here's your pancakes"
    show h_holly a_9 
    holly "Cheers mom."
    show sandra a_0 at Position(xpos = 0.35) with move
    sandra "I need to get to work now, clean up after me will you? And young lady you better hurry. Your lecture starts in 30 minutes!!"
    hide sandra with easeoutleft
    play sound h_sfx_eat loop
    show h_holly blush a_5
    think "Oh I'm finally starting to come back to life. I should probably text Cassie and make sure she came home safe, and apologize for my bold behavior yesterday"
    think "It's very unlike me to behave so boldly, she must have been quite flustered about the scene i was making.. oh well."
    "Holly and Cassie has known each other since they went to middle-school, at first Holly thought Cassie was a bit of a posh prick. But over the course of high-school they both took a liking to one another, Holly had a crush on Cassie, but didn't have the courage to admit her feelings."
    "And also Cassie was straighter than an arrow, she was basically beaming of heterosexuality"
    text start cassie
    text title "Hime-sama"
    stop sound
    msg holly "Hey Cassie.. How are you feeling?"
    play sound sfx_text
    msg cassie "Oh hi Holly, I'm still a bit hangover but it's nothing bad."
    msg holly "I had a good time yesterday, the little i can remember.. but i just want to apologize for my drunken self yesterday, i think i went overboard a bit."
    play sound sfx_text
    msg cassie "hahaha i had a good time as well, dw about it hun"
    show h_holly a_14
    text end
    think "Oh thank god she isn't angry with me. Okay! Time to get this mess sorted and get my ass to collage. What was my first lesson hmm.. today was Friday, so first lecture would be Math, yuck"
    show h_holly a_1 at Position(xpos = 0.35, ypos = 1.0) with move
    stop music fadeout 3.0
    "I cleaned up the dishes and headed out"
    hide h_holly with easeoutleft
    scene black with fade
    play sound h_sfx_walk loop
    scene bg main house day
    play music h_bgm_omae fadein 3.0
    #INSERT PSYCHO
    #maybe an option about carrie having a remote?? oh good christ..
    show h_holly a_1 at centerleft
    show h_holly a_1:
        easeout 4.5 offscreenright
    "Sun was shining without a cloud in sight, birds chirping and there was a slight smell of wet grass"
    think "I can't stop thinking about yesterday, i can't believe Cassie would just let me do all those things, I even kissed her on the cheek..."
    hide h_holly
    scene bg city walkway day
    show h_holly a_1 at left:
        easeout 4.5 ypos 0.5 offscreenright
    "Sun was shining without a cloud in sight, birds chirping and there was a slight smell of wet grass"
    think "I can't stop thinking about yesterday, i can't believe Cassie would just let me do all those things, I even kissed her on the cheek..."
    hide h_holly
    scene bg natschool day
    show h_holly a_0 at left
    "Coming into view ahead was Tina Koya Collage, a well respected academy for above average students."
    cassie "Hey Holly!"
    "I look around to spot her"
    cassie "Holllllyyyyy!!!!!"
    "There she is! Cassie and Scarlet is standing 50 meters away waving happily"
    show cassie a_0 at right
    show scarlet a_0 at Position(xpos = (placement_of(cassie).xpos - 0.15), ypos = 0.6)
    holly "Hey guys!"
    show cassie a_0 at centerright
    show scarlet a_0 at Position(xpos = (placement_of(cassie).xpos - 0.15), ypos = 0.6)
    show h_holly a_0 at centerleft
    with move
    stop sound
    scarlet "Hey Holly, yesterday was fun wasn't it"
    think "Shit don't blush, don't blush..."
    show h_holly blush a_6
    holly "Yeah.. I might've had a few many to drink. Did you get home safe yesterday?"
    "I should really try to change the subject.. "
    show scarlet a_11
    scarlet "O Holly you needn't be embarrassed, although you usually don't pounce on Cassie like a tiger hungering for meat"
    holly "uhhh i.. don-don't."
    cassie "Don't worry Holly she's only teasing you."
    think "I really need to calm down."
    holly ".. Shall we head to class perhaps?"
    scene black with fade
    scene bg natschool classroom day
    show h_holly b_0 at left
    show carla a_0 at center:
        zoom 0.4
        ypos 0.52 xpos 0.7
    "Math wasn't particularly difficult for me, I usually breeze through the math lectures pretty easily, the same couldn't be said about Cassie. I've been trying to help her study during the weekends to little avail."
    placeholder