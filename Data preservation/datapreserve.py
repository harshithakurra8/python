from logger import log
CONTACTS={
    "Dale":9876,
    "John":8689
}

def execute(cmd: list[str]):
    match cmd:
        case['ls']:print(CONTACTS)
    
        case['ls',name]:print(CONTACTS.get(
            name.capitalize(),"Not found!"
    ))
        case['add',name,info]:
            CONTACTS[name.capitalize()]=info

        case['del'|'rm',name]:
            name=name.capitalize()

            if name in CONTACTS:
                info=CONTACTS.pop(name)
                print(f"Removed{info}of {name}")
            else:
                print(f"{name}not found!")
        case["quit"|"exit"]: return "EXIT"
        case[*cmd]:
            print("Unknown Command",cmd)

#main loop
log("Phonebook",decor="#",padding=3)
while True:
    cmd = input("> ")
    exit_code=execute(cmd.split())
    if exit_code=="EXIT":break
