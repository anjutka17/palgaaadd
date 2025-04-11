import random
def loo_andmed():
    """
    Loob nime- ja vitamiinide nimekirja.
    :return: (nimed, vitamiinid) - kaks listi
    """
    nimed = []
    vitamiinid = []

    n = int(input("Mitu patsienti? "))
    for _ in range(n):
      nimi = input("Sisesta patsiendi nimi: ")
      nimed.append(nimi)
      vitamiinid.append(random.randint(10, 100)) 
      return nimed, vitamiinid


def puudujääk(nimed, vitamiinid):
    """Выводит список пациентов, у которых витамин D < 30"""
    print("\nPatsiendid, kellel on D-vitamiini puudus (<30):")
    for i in range(len(vitamiinid)):
        if vitamiinid[i] < 30:
             print(f"{nimed[i]} - {vitamiinid[i]}")


def keskmine(vitamiinid):
    """Выводит среднее значение витамина D"""
    if vitamiinid:

        avg = sum(vitamiinid) / len(vitamiinid)
        print(f"\nKeskmine D-vitamiini tase: {avg:.2f}")
    else:
        print("Vitamiinide nimekiri on tühi.")


def top_k(nimed, vitamiinid):
    """Выводит список K людей с самым высоким уровнем витамина D"""
    k = int(input("Mitu parimat inimest soovid näha? "))
    koos = list(zip(nimed, vitamiinid))
    koos.sort(key=lambda x: x[1], reverse=True)

    print(f"\nTop {k} inimest D-vitamiini sisaldusega:")
    for nimi, vitamiin in koos[:k]:
         print(f"{nimi} - {vitamiin}")


def otsi_nime_jargi(nimed, vitamiinid):
    """Поиск пациента по имени"""
    otsitav = input("Sisesta nimi, keda otsid: ")
    leitud = False
    for i in range(len(nimed)):
        if nimed[i].lower() == otsitav.lower():
            print(f"{nimed[i]} - {vitamiinid[i]}")
            leitud = True
            if not leitud:
                print("Patsient nimega ei leitud.")


def oma_valik(nimed, vitamiinid):
    """Пример: выводит количество пациентов с уровнем > 80"""
    count = sum(1 for v in vitamiinid if v > 80)
    print(f"\nPatsiente, kelle D-vitamiini tase > 80: {count}")
