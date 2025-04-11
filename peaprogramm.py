from vitamiinid_module import *
def patsiendid():
    nimed, vitamiinid = loo_andmed()

    while True:
             print("\n--- MENÜÜ ---")
             print("1 - Näita patsiente, kellel on D-vitamiini puudus (<30)")
             print("2 - Arvuta keskmine D-vitamiini näit")
             print("3 - Top K inimesed kõrgeima D-vitamiiniga")
             print("4 - Otsi patsienti nime järgi")
             print("5 - Oma valik (näita patsientide arvu, kellel D > 80)")
             print("0 - Välju")

             valik = input("Sinu valik: ")

             if valik == "1":
                puudujääk(nimed, vitamiinid)
             elif valik == "2":
                keskmine(vitamiinid)
             elif valik == "3":
                 top_k(nimed, vitamiinid)
             elif valik == "4":
                 otsi_nime_jargi(nimed, vitamiinid)
             elif valik == "5":
                 oma_valik(nimed, vitamiinid)
             elif valik == "0":
                  print("Programmi lõpp.")
             break
    else:
        print("Vigane valik. Proovi uuesti.")
if __name__=="__main__":
    patsiendid()
    
