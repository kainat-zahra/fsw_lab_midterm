from django.shortcuts import render
import wikipedia,webbrowser

def getPage():
    wikipage = wikipedia.random(1)        
    wikiload = wikipedia.page(wikipage)

    userchoice = input("Would you like to read about {}?? (Y/N/Q)".format(wikipage)).lower().strip()

    if(userchoice == "y" or userchoice == "yes"):
        print("\nSummary:\n--------\n"  )
        print(wikiload.summary)
        wikiopen = input("\nDo you want to Open Wikipedia page in browser? (Y/N)").lower().strip()
        if(wikiopen == "yes" or wikiopen == "y"):
            webbrowser.open(wikiload.url,new=2)
        again = input("Do you Want to View Another Article (Y/N)??").lower()
        if (again == "y" or again == "yes"):
            getPage()
        else:
            print("\nThank You!!!\n")
            print("Regards:\n183159\n183173\n183183\n183205")
            exit(0)

    elif(userchoice == "n" or userchoice == "no"):
        getPage()
    elif(userchoice == "q" or userchoice == "quit"):
        print("\nThank You!!!\n")
        print("Regards:\n183159\n183173\n183183\n183205")
        exit(0)
    else:
        print("Invalid Input.\nWARNING: Another INVALID INPUT will generate a new random article.\n")

        userchoice = input("Would you like to read about {}?/(Y/N/Q)".format(wikipage)).lower().strip()

        if(userchoice == "y" or userchoice == "yes"):
            print("\nSummary:\n--------\n"  )
            print(wikiload.summary)
            wikiopen = input("\nDo you want to Open Wikipedia page in browser? (Y/N)").lower().strip()
            if(wikiopen == "yes" or wikiopen == "y"):
                webbrowser.open(wikiload.url,new=2)
            again = input("Do you Want to View Another Article??(Y/N)").lower()
            if (again == "y" or again == "yes"):
                getPage()
            else:
                print("\nThank You!!!\n")
            print("Regards:\n183159\n183173\n183183\n183205")
            exit(0)
        elif(userchoice == "n" or userchoice == "no"):
            getPage()
        elif(userchoice == "q" or userchoice == "quit"):
            print("\nThank You!!!\n")
            print("Regards:\n183159\n183173\n183183\n183205")
            exit(0)
        else:
            print("Invalid Input.\n(Article Changed)")
            getPage()
            


if __name__ == "__main__":
    getPage()

