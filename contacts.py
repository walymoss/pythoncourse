contacts = {
    "number":4,
    "students":
    [
        {"name":"Sarah Holderness", "email":"sarah@example.com"},
        {"name":"Harry Potter", "email":"harry@example.com"},
        {"name":"Walter Estrada", "email":"walter@example.com"}
    ]
}

for contact in contacts["students"]:
    #print(contact)
    print(contact["email"])