
# Task 2

def get_cats_info(path):
    try:
        with open(path,'r',encoding="utf-8") as file:
            cats = file.readlines()

            catsList = []

            for cat in cats:
                id, name, age = cat.strip().split(',')
                catsList.append({"id":id,"name":name,'age':age})
                

            return catsList

    except Exception as e:
        return e



cats_info = get_cats_info("cat.txt")
print(cats_info)
