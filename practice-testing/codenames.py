import random
import pickle



def main():
    print(len(BOYS_NAMES))
    print(f'{len(GIRLS_NAMES)}')
    boys = BOYS_NAMES
    girls = GIRLS_NAMES
    select_boys = random_codenames(BOYS_NAMES)
    select_girls = random_codenames(GIRLS_NAMES)
    print(len(select_boys))
    print(len(select_girls))
    all_names = select_girls + select_boys
    print(len(all_names))
    random.shuffle(all_names)
    print_names(all_names)



def first_letter(code):
    return code[:1]

def random_codenames(names):
    selected_names = []
    while len(names) > 0:
        name = names.pop(random.randrange(len(names)))
        sum = 0
        for chosen in selected_names:
            if chosen[:1] == name[:1]:
                sum += 1
        if sum < 5:
            selected_names.append(name)
    return selected_names
 
    
        

def print_names(list):
    for name in list:
        print(f"{name}")


BOYS_NAMES = [
    "Abel", "Abie", "Acey", "Acie", "Adam", "Adan", "Aden", "Adin", "Ajay",
    "Alan", "Alba", "Alby", "Aldo", "Alec", "Alek", "Alex", "Alma", "Alta",
    "Alto", "Alva", "Alvy", "Amil", "Amin", "Amir", "Amit", "Amon", "Amos",
    "Andy", "Anna", "Arba", "Arch", "Ares", "Aric", "Arlo", "Arne", "Arno",
    "Aron", "Arvo", "Atha", "Audy", "Avon", "Axel", "Ayan", "Babe", "Baby",
    "Bart", "Bear", "Beau", "Bell", "Bert", "Bill", "Bird", "Birt", "Blas",
    "Bode", "Bose", "Boss", "Boyd", "Brad", "Bret", "Buck", "Budd", "Buel",
    "Bunk", "Burk", "Burl", "Burr", "Burt", "Bush", "Byrd", "Cade", "Cael", 
    "Cain", "Cale", "Carl", "Cary", "Case", "Cash", "Cass", "Cato", "Chad", 
    "Chas", "Chaz", "Chet", "Chin", "Chip", "Clay", "Clem", "Cleo", "Coby", 
    "Codi", "Cody", "Coen", "Cole", "Colt", "Cora", "Cory", "Coty", "Crew", 
    "Cris", "Cruz", "Curt", "Dale", "Dana", "Dane", "Dann", "Darl", "Dash",
    "Dave", "Davy", "Dean", "Dell", "Deon", "Derl", "Desi", "Dick", "Dink",
    "Dino", "Dion", "Dior", "Dirk", "Dock", "Doll", "Donn", "Dora", "Dorr",
    "Doss", "Doug", "Drew", "Duff", "Duke", "Earl", "Eben", "Eber", "Eddy",
    "Eden", "Edie", "Edna", "Eino", "Elam", "Elby", "Elex", "Elie", "Elio",
    "Ella", "Elmo", "Elon", "Eloy", "Elva", "Elza", "Elzy", "Emil", "Emir",
    "Emit", "Emma", "Emry", "Enos", "Enzo", "Erby", "Eric", "Erie", "Erik",
    "Erin", "Erle", "Esau", "Esco", "Esta", "Eula", "Evan", "Ewin", "Ezra",
    "Fate", "Ferd", "Fern", "Finn", "Flem", "Floy", "Foch", "Ford", "Fred",
    "Gabe", "Gael", "Gage", "Gail", "Gale", "Gary", "Gene", "Geno", "Gian",
    "Gino", "Glen", "Gray", "Greg", "Grey", "Guss", "Gust", "Hale", "Hall",
    "Hamp", "Hank", "Hans", "Harl", "Harm", "Hart", "Hays", "Herb", "Hill",
    "Hoke", "Hope", "Hoyt", "Huey", "Hugh", "Hugo", "Hung", "Hunt", "Iker",
    "Isai", "Isam", "Isom", "Ivan", "Iver", "Ivey", "Ivor", "Jace", "Jack",
    "Jade", "Jael", "Jair", "Jake", "Jame", "Jase", "Jaxx", "Jean", "Jeff",
    "Jens", "Jere", "Jess", "Jett", "Joan", "Jobe", "Jody", "Joel", "Joey",
    "John", "Jory", "Jose", "Josh", "Juan", "Judd", "Jude", "Judy", "Jule",
    "June", "Kace", "Kade", "Kael", "Kale", "Kane", "Karl", "Kase", "Kash",
    "Kaye", "Kent", "Keon", "Khai", "Kian", "Kiel", "King", "Kipp", "Kirk",
    "Kirt", "Knox", "Kobe", "Koby", "Koda", "Kody", "Koen", "Kole", "Kory",
    "Krew", "Kris", "Kurt", "Kyan", "Kyle", "Kylo", "Kyng", "Kyro", "Lacy",
    "Lafe", "Lane", "Lark", "Lars", "Lary", "Leif", "Lena", "Leon", "Less",
    "Levi", "Levy", "Liam", "Lian", "Lige", "Link", "Linn", "Lisa", "Lish",
    "Lois", "Lola", "Lone", "Long", "Lora", "Lott", "Love", "Loyd", "Luca",
    "Lucy", "Luis", "Luka", "Luke", "Lula", "Lupe", "Lute", "Lyle", "Lynn",
    "Mace", "Mack", "Male", "Marc", "Mark", "Mart", "Mary", "Math", "Matt",
    "Maud", "Maxx", "Mayo", "Meir", "Mell", "Merl", "Mike", "Milo", "Mont",
    "Mose", "Murl", "Musa", "Myer", "Mylo", "Myrl", "Nash", "Neal", "Neil",
    "Nels", "Nery", "Newt", "Nick", "Nico", "Niko", "Nile", "Nils", "Noah",
    "Noel", "Nora", "Nova", "Obed", "Obie", "Ocie", "Odie", "Odin", "Odis",
    "Odus", "Okey", "Olaf", "Olan", "Olen", "Oley", "Olie", "Olin", "Olof",
    "Omar", "Omer", "Onyx", "Opal", "Oral", "Oran", "Oren", "Orie", "Orin",
    "Oris", "Orla", "Orlo", "Osie", "Otha", "Otho", "Otis", "Otto", "Ovid",
    "Owen", "Ozie", "Ozzy", "Page", "Park", "Pate", "Paul", "Pete", "Phil",
    "Pink", "Ples", "Polk", "Purl", "Rafe", "Rahn", "Rand", "Raul", "Reed",
    "Reid", "Remi", "Remy", "Rene", "Reno", "Rhys", "Rian", "Rice", "Rich",
    "Rick", "Rico", "Robb", "Robt", "Roby", "Rock", "Roel", "Rolf", "Roll",
    "Roma", "Rome", "Rory", "Rosa", "Rose", "Ross", "Rube", "Ruby", "Rudy",
    "Ruel", "Rush", "Russ", "Ruth", "Ryan", "Ryne", "Sage", "Saul", "Scot",
    "Sean", "Seth", "Shad", "Shan", "Shay", "Shea", "Shep", "Shon", "Sing",
    "Skip", "Stan", "Syed", "Taft", "Tahj", "Tate", "Thad", "Theo", "Thor",
    "Thos", "Tina", "Tito", "Tobe", "Toby", "Todd", "Toma", "Tony", "Tory",
    "Trae", "Trey", "Troy", "TRUE", "Tuan", "Vera", "Vere", "Verl", "Vern",
    "Vick", "Vito", "Wade", "Walt", "Ward", "Wash", "Watt", "Webb", "Wess",
    "West", "Whit", "Will", "Wing", "Wirt", "Wong", "Wood", "Xavi", "Yael",
    "Yair", "Yoel", "York", "Zack", "Zaid", "Zain", "Zane", "Zayd", "Zayn",
    "Zeke", "Zeno", "Zion", "Zyon",
]

GIRLS_NAMES = [
    "Abby", "Adah", "Adda", "Adel", "Aida", "Aila", "Aili", "Alba", "Alda",
    "Alex", "Alia", "Alla", "Ally", "Alma", "Alta", "Alva", "Alys", "Amey",
    "Amia", "Amie", "Amma", "Amya", "Andi", "Anie", "Anna", "Anne", "Anya",
    "Arah", "Aria", "Arie", "Arla", "Arly", "Arra", "Arta", "Arya", "Asha",
    "Asia", "Ason", "Atha", "Aura", "Avah", "Avie", "Avis", "Ayla", "Ayva",
    "Azul", "Baby", "Bama", "Barb", "Bebe", "Beda", "Bell", "Bena", "Bert",
    "Bess", "Beth", "Bina", "Bird", "Brea", "Bree", "Bria", "Bryn", "Bula",
    "Buna", "Byrd", "Cali", "Cami", "Cara", "Cari", "Carl", "Caro", "Cary",
    "Ceil", "Cena", "Cher", "Ciji", "Clem", "Cleo", "Cloe", "Cody", "Cora",
    "Cori", "Cory", "Cruz", "Cuba", "Daja", "Dale", "Dana", "Dani", "Dara",
    "Dave", "Dawn", "Dean", "Debi", "Deja", "Dell", "Dema", "Demi", "Dena",
    "Dian", "Dicy", "Dina", "Dior", "Diya", "Dola", "Dona", "Dora", "Dori",
    "Dove", "Drew", "Dwan", "Dyan", "Earl", "Ebba", "Echo", "Eden", "Edie",
    "Edla", "Edna", "Edra", "Effa", "Elba", "Elda", "Elia", "Elin", "Ella",
    "Elle", "Elma", "Elna", "Elsa", "Else", "Elta", "Elva", "Elza", "Emma",
    "Emmy", "Enid", "Eola", "Eric", "Erie", "Erin", "Eris", "Erla", "Erma",
    "Erna", "Eryn", "Esme", "Essa", "Esta", "Etha", "Etna", "Etta", "Eula",
    "Euna", "Eura", "Ever", "Evia", "Evie", "Evon", "Exie", "Ezra", "Fawn",
    "Faye", "Fern", "Flor", "Floy", "Fran", "Fred", "Gail", "Gale", "Gary",
    "Gaye", "Gena", "Gene", "Geri", "Gigi", "Gina", "Gwen", "Gwyn", "Hali",
    "Halo", "Hana", "Hedy", "Hope", "Icey", "Icie", "Ilah", "Ilda", "Illa",
    "Ilma", "Ines", "Inez", "Inga", "Iola", "Iona", "Ione", "Iris", "Irma",
    "Irva", "Isis", "Isla", "Ivah", "Ivey", "Ivie", "Iyla", "Jack", "Jada",
    "Jade", "Jami", "Jana", "Jane", "Jann", "Jaye", "Jean", "Jena", "Jeri",
    "Jill", "Joan", "Jodi", "Jody", "Joey", "John", "Joni", "Joye", "Judi",
    "Judy", "Jule", "Juli", "June", "Kaci", "Kacy", "Kaia", "Kala", "Kali",
    "Kami", "Kara", "Kari", "Kate", "Kati", "Katy", "Kaya", "Kaye", "Keli",
    "Keri", "Kira", "Kiya", "Kloe", "Kora", "Kori", "Kris", "Kyla", "Kyle",
    "Kyra", "Laci", "Lacy", "Lady", "Lala", "Lana", "Lani", "Lara", "Leah",
    "Leda", "Leia", "Lela", "Lena", "Lera", "Lesa", "Leta", "Leva", "Lexi",
    "Lida", "Lila", "Lily", "Lina", "Lisa", "Lise", "Lita", "Liza", "Loda",
    "Lois", "Lola", "Loma", "Lona", "Loni", "Lora", "Lori", "Lota", "Love",
    "Lucy", "Luda", "Lula", "Lulu", "Luna", "Lupe", "Lura", "Lyda", "Lyla",
    "Lynn", "Lyra", "Maci", "Macy", "Maia", "Mame", "Mara", "Mari", "Mark",
    "Mary", "Maud", "Maya", "Maye", "Meda", "Mell", "Mena", "Meta", "Miah",
    "Mila", "Mima", "Mimi", "Mina", "Mira", "Miya", "Mona", "Mora", "Murl",
    "Myah", "Myla", "Myra", "Myrl", "Nada", "Nala", "Nana", "Navy", "Naya",
    "Neha", "Nell", "Nena", "Neta", "Neva", "Niki", "Nila", "Nina", "Nira",
    "Nita", "Noah", "Noel", "Nola", "Noma", "Nona", "Noor", "Nora", "Nova",
    "Nyah", "Nyla", "Nyra", "Ocie", "Octa", "Odie", "Olar", "Olga", "Olie",
    "Omie", "Oney", "Onie", "Opal", "Opha", "Orah", "Oral", "Orma", "Orra",
    "Osie", "Otha", "Ozie", "Paul", "Pink", "Raya", "Reba", "Remi", "Remy",
    "Rena", "Rene", "Reta", "Reva", "Rhea", "Risa", "Rita", "Riya", "Roma",
    "Rona", "Roni", "Rory", "Rosa", "Rose", "Rosy", "Roxy", "Rubi", "Ruby",
    "Ruie", "Ruth", "Ryan", "Sada", "Sade", "Sage", "Sara", "Sena", "Shae",
    "Shay", "Shea", "Sina", "Skye", "Star", "Sula", "Suzy", "Taja", "Tami",
    "Tana", "Tara", "Tari", "Taya", "Tena", "Tera", "Teri", "Tess", "Thea",
    "Theo", "Tina", "Tiny", "Tisa", "Tobi", "Toby", "Toni", "Tori", "Tory",
    "Toya", "Troy", "Tula", "Tyra", "Vada", "Vara", "Veda", "Vela", "Vena",
    "Vera", "Veta", "Veva", "Vicy", "Vida", "Vina", "Vira", "Vita", "Viva",
    "Wava", "Will", "Wren", "Xena", "Yara", "Zada", "Zana", "Zara", "Zela",
    "Zena", "Zeta", "Zina", "Zion", "Zita", "Zoey", "Zoie", "Zola", "Zona",
    "Zora", "Zoya", "Zula", "Zuri",
]




if __name__ == "__main__":
    main()

