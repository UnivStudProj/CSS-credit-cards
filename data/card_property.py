import random
import names
import json

cards_dict = {}
# adding cards to the dictionary 
for i in range(100):
    # random choise between images
    image = (lambda rn: "images/visa.png" if rn >= 0.5 else "images/mc.png")(random.random())
    # random card number
    num_list = []
    # creating 4 random digits
    for rn in range(4):
        rn_num = str(random.randint(0, 9999))
        # adding 0 at the beginning of the number if it not 4-digit
        while len(rn_num) != 4:
            rn_num = "0" + rn_num[:len(rn_num)]
        num_list.append(rn_num)
    # getting name for a carc
    card_holder = names.get_full_name()
    # generating random card date
    card_date = str(random.randint(1, 12)) + ' / ' + str(random.randint(22, 32))
    # hexadecimal color
    r = lambda: random.randint(0,255)
    gradient = ['#%02X%02X%02X' % (r(),r(),r()), '#%02X%02X%02X' % (r(),r(),r())]
    cards_dict[f"card{i}"] = {
        "image" : image,
        "num_list" : str(num_list).replace("'", ""),
        "card_holder" : card_holder,
        "card_date" : card_date,
        "gradient" : str(gradient).replace("'", "")
    }
# creating json file
with open('data/cards.json', 'w') as f:
    json.dump(cards_dict, f, indent=2)