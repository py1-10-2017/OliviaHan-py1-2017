


def generator(my_dict):
    for key,data in my_dict.iteritems():
        return (key,data)



my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

print generator(my_dict)
