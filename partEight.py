inventory = []
tasksdone = []
def main():

    currentinput = ""
    timeleft = 5
    tempinput = ""


    print("You awaken in your bed and look at the clock. There are a few things that you need to do before you leave for another day.")
    currentinput = validateinput(input("You notice that your ID card is on your desk. Do you pick it up? y/n ").lower(), ["y","n"])
    if (currentinput == "y"):
        print("You picked up your ID card and put it into your coat pocket. You can't believe that you left it on your desk last night.")
        inventory.append("id card")
    else:
        print("You decided that you could do it later, after all, you have to get ready before even worrying about the ID card.")

    while timeleft > 0:
        thingstoputinbag = ["notebook", "plush", "book", "keyring", ""]
        tasksleft = ["breakfast", "getting dressed", "washing", "packing bag", "tidying", ""]
        currentinput = validateinput(input("You have some other things that you need to do before leaving. breakfast/getting dressed/washing/packing bag/tidying ").lower(), tasksleft)
        match (currentinput):
            case currentinput if currentinput == "breakfast" and "breakfast" not in tasksdone:
                print("You have to eat something today, after all you'll need it for the long day ahead.")
                tempinput = validateinput(input("You head into your kitchen and see some fruit and some cereal that you could eat. Which do you choose? fruit/cereal ").lower, ["fruit", "cereal"])
                if (tempinput == "fruit"):
                    print("You pick up some of the fruit laying in the bowl and realise that most of what you have decided on would be able to go into your bag.")
                    tempinput = validateinput(input("Do you plan to put the fruit in your bag for later? y/n ").lower(), ["y", "n"])
                    if (tempinput == "y"):
                        print("You pick up the fruit and head back to your bedroom.")
                        inventory.append("assorted fruits")
                    else:
                        print("You would rather just eat it now anyway, otherwise you may forget about eating it later and it ends up wasted. \nIt tasted nice, and you feel a bit more refreshed as you return to your room.")
                else:
                    print("You eat some of the cereal that is in the cupboard. You don't look forward to having to wash that bowl when you get home, but it's better than being hungry. You return to your room after placing your bowl besides your other washing up.")
                tasksdone.append("breakfast")
            case "breakfast":
                print("You have already eaten, but you take another look around the kitchen and spot your cat eating from her bowl.")
                tempinput = validateinput(input("Do you pet her? y/n").lower(), ["y","n"])
                if (tempinput == "y"):
                    print("You gently stroke her as she is still absorbed in her food. How adorable. \nWhile you wish that you could stay there longer, you have other things to do.")
                else:
                    print("You decide to leave her to her own devices for now, because you have things to do.")
            case currentinput if currentinput == "getting dressed" and "getting dressed" not in tasksdone:
                print("You pull on the clothes that you already have left out. You feel quite confident in your outfit for the day.")
                tasksdone.append("getting dressed")
            case "getting dressed":
                print("You already have your clothes ready but you are starting to second guess yourself.")
                tempinput = validateinput(input("Do you want to change? y/n").lower(), ["y","n"])
                if (tempinput == "y"):
                    print("You take off your clothes and hang them back up, you haven't worn them long after all. You put on another set of clothes, ones that you are more confident in wearing.")
                else:
                    print("You elect not to change, that would just be a waste of your time.")
            case currentinput if currentinput == "washing" and "washing" not in tasksdone:
                print("You go into your bathroom and brush your teeth and wash yourself quickly. You feel better afterwards, more energised.")
                tempinput = validateinput(input("You notice your mouthwash sitting on the side of the sink. Do you use it? y/n ").lower(), ["y", "n"])
                if (tempinput == "y"):
                    print("You have the time to use it, and so you do- spitting it into the sink once you are finished.")
                else:
                    print("You haven't had enough time to use it recently anyway, so you leave your bathroom without using your mouthwash.")
                tasksdone.append("washing")
            case "washing":
                print("You have already washed yourself, so it wouldn't be the best idea to coe back here. You do not even notice anything out of place.")
            case "packing bag":
                print("You look in your bag after you have placed your lunch and a drink in there to see if you have everything. Fortunately you have everything you need.")
                if ("assorted fruits" in inventory and "packing bag" not in tasksdone):
                    print("Before you forget, you also decide to put those fruits from earlier in there.")
                print("You also notice some other things in your room that, while not necessary per say, would be nice to have for you. In your room you notice: ")
                for _ in thingstoputinbag.count:
                    print(thingstoputinbag[_])
                tempinput = validateinput(input("What do you put in your bag?").lower(), thingstoputinbag)
                match tempinput:
                    case "notebook":
                        print("You like having a notebook with you to note down the things that you have seen or any ideas you may get while outside. You slip it into your bag.")
                        inventory.append("notebook")
                    case "plush":
                        print("Sometimes when you have an extremely long day, you turn to this pluch for comfort in your exhaustion. It could also help you resolve certain problems you had by acting like a rubber duck. You decide to put it into your bag.")
                        inventory.append("plush")
                    case "keyring":
                        print("Your bag has never felt right without a keyring and you had one that you had been meaning to put on your bag. Now you have the perfect excuse to put it on.")
                    case "book":
                        print("You have a lot of long breaks today, and so the book you have been reading currently might make for a productive use of your time.")
                        inventory.append("book")
                    case _:
                        print("You decide to not put anything else into your bag, you already have everything that you need.")
                if ("packing bag" not in tasksdone):
                    tasksdone.append("packing bag")
            case currentinput if currentinput == "tidying" and "tidying" not in tasksdone:
                print("You decide to tidy your room while you had the time, moving everything to its rightful place before you left. You notice something on the floor as everything has been moved, some cash loose. You count the change and it totals to approximately £10.")
                tempinput = validateinput(input("Do you take it? y/n ").lower(), ["y", "n"])
                if tempinput == "y":
                    print("It could be useful, If nothing else, it is absolutely good as emergency money.")
                    inventory.append("money")
                else:
                    print("You decide to leave it in your room. It could be more useful another time.")

    print("You have run out of time to do anything else before you leave. After all, if you didn't leave now, you would be late.")
    tasksleft.remove("")
    if (tasksdone.count == tasksleft.count):
        print("You feel confident that you have done everything that you can do for now before leaving.")
        bus()
    elif (tasksdone.count != 0):
        print("You think that there is more to do, but that can wait for later.")
        bus()
    else:
        print("You feel so lethargic today and feel as though you cannot do anything but stare at the wall. So you elect to return to the warmth of your bed, at least you will be comfortable there. It is a waste of time to leave this house if you won't be able to focus on anything for the rest of the day.")
        print("You have lost.")
    


def validateinput(vinput, validoptions):
    while (vinput not in validoptions):
        vinput = input("That is not a valid option, please try again: ").lower()
    return vinput

def bus():
    if ("id card" not in inventory and "money" not in inventory):
        print("As you move to get onto the bus, you realise that you cannot pay for the ticket you so desperately need- embarassing yourself in front of the expectant driver. You step off of the bus as quickly as you got on and watch helplessly as it leaves your stop- stranding you. Defeated, you resign yourself to missing today and return.")
        if (tasksdone.count != 5):
            print("You think that at least you can do those tasks that you left without doing, and spend more time with your cat, as dread mounts in you.")
        else:
            print("There is nothing that you can do except wander home as a sense of dread compounds inside of you.")
        print("You have lost.")
    elif ("money" in inventory):
        print("As your stomach plummets at the thought at you not having the ID necessary to validate your ticket, you search your bag and find the money that you had picked up earlier. It was fortunate that you had some on hand. You pay for a temporary bus ticket apologetically and seat yourself on the bus, secure in the knowledge that you will reach your destination on time if nothing else.")
        print("You have won.")
    else:
        print("You pull your ID card from your coat pocket and the bus driver nods after looking between it and the ticket on your phone. You smile and thank the driver before searching for a spare seat on the bus.")
        if ("assorted fruits" in inventory):
            print("You open your bag to find the fruit from earlier at the bottom and pull it out before closing your bag again. The fruit rests on your lap as it waits for you to eat.")
        print("You settle against the window, preparing for the long journey ahead to your destination- but everything is as it should be.")
        print("You have won.")