class Hero:
    # Atribut / properto
    nama = ""
    damage = "0"
    hp = "0"
    defemse= "0"

    def __init__(self, nama, damage, hp, defemse):
        self.nama = nama
        self.damage = damage
        self.hp = hp
        self.defemse = defemse

    def info (self):
        print("="*20)
        print("name :" , self.nama)
        print("damage :" , self.damage)
        print("hp :", self.hp)
        print("defemse :", self.defemse)


hero = Hero ("Balmod","2300", "421", "90")
hero.info()