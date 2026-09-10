with open("portal-overrides.js", "r", encoding="utf-8") as f:
    po = f.read()

names = ["Halfpenny's Cafe", "Johnny Burrito", "Nirvana II", "The Sandwich Club", "Crunch Bistro", "Luce Ristorante", "Hasaki Grill & Sushi", "French Quarter Restaurant", "Pie in the Sky Pizza", "Basil Thai Cuisine"]

for n in names:
    print(n, "in overrides:", n in po)
