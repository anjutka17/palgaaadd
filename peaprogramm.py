from vitamiinid_module import *
def patsiendid():
    nimed, vitamiinid = loo_andmed()

    while True:
             print("\n--- MEN‹‹ ---")
             print("1 - N‰ita patsiente, kellel on D-vitamiini puudus (<30)")
             print("2 - Arvuta keskmine D-vitamiini n‰it")
             print("3 - Top K inimesed kırgeima D-vitamiiniga")
             print("4 - Otsi patsienti nime j‰rgi")
             print("5 - Oma valik (n‰ita patsientide arvu, kellel D > 80)")
             print("0 - V‰lju")

             valik = input("Sinu valik: ")

             if valik == "1":
                puuduj‰‰k(nimed, vitamiinid)
             elif valik == "2":
                keskmine(vitamiinid)
             elif valik == "3":
                 top_k(nimed, vitamiinid)
             elif valik == "4":
                 otsi_nime_jargi(nimed, vitamiinid)
             elif valik == "5":
                 oma_valik(nimed, vitamiinid)
             elif valik == "0":
                  print("Programmi lıpp.")
             break
    else:
        print("Vigane valik. Proovi uuesti.")
    