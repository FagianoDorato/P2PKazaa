# coding=utf-8
import threading
from Client.Peer import Peer
from servers import multithread_server
from dbmodules.dbconnection import *
from helpers.helpers import *
import config

supernode_mode = False

# Avvio il server in ascolto sulle porte 80 e 6000
server = multithread_server.Server()
server.start()

db = MongoConnection()

out_lck = threading.Lock()

output(out_lck, "Are you a supernode?")
output(out_lck, "1: YES")
output(out_lck, "2: NO")

int_choice = None
while int_choice is None:
    try:
        option = raw_input()    # Input da tastiera
    except SyntaxError:
        option = None

    if option is None:
        output(out_lck, "Please select an option")
    else:
        try:
            int_choice = int(option)
        except ValueError:
            output(out_lck, "A choice is required")


if int_choice == 1:
    output(out_lck, "YOU ARE A SUPERNODE")
    supernode_mode = True
else:
    output(out_lck, "YOU ARE A PEER!")

p = Peer()

while True:
    print_menu_top(out_lck)
    output(out_lck, "## Select one of the following options ('e' to exit): ##")
    output(out_lck, "## 1: Search supernodes                               ##")
    print_menu_bottom(out_lck)

    int_option = None
    while int_option is None:
        try:
            option = raw_input()
        except SyntaxError:
            option = None

        if option is None:
            output(out_lck, "Please select an option")
        elif option == 'e':
            output(out_lck, "Bye bye")
            server.stop()
            sys.exit()  # Interrompo l'esecuzione
        else:
            try:
                int_option = int(option)
            except ValueError:
                output(out_lck, "A number is required")

    if int_option != 1:
        output(out_lck, "Option " + str(option) + " not available")
    else:
        # TODO: ricerca dei supernodi tramite i vicini nella tabella neighbor, i supernodi vanno salvati nella tabella neighbor con is_supernode = true


        # una volta trovato almeno un supernodo


        if supernode_mode:
            while True:
                print_menu_top(out_lck)
                output(out_lck, "## Select one of the following options ('e' to exit): ##")
                output(out_lck, "## 1: Search supernodes                               ##")
                output(out_lck, "## 2: Add file (to myself)                            ##")
                output(out_lck, "## 3: Delete file (from myself)                       ##")
                output(out_lck, "## 4: Search file                                     ##")
                print_menu_bottom(out_lck)

                int_option = None
                try:
                    option = raw_input()
                except SyntaxError:
                    option = None

                if option is None:
                    output(out_lck, "Please select an option")
                elif option == 'e':
                    output(out_lck, "Bye bye")
                    server.stop()
                    sys.exit()  # Interrompo l'esecuzione
                else:
                    try:
                        int_option = int(option)
                    except ValueError:
                        output(out_lck, "A number is required")
                    else:
                        if int_option == 1:
                            # ricerca supernodi e salvataggio nel db
                            print "ricerca supernodi"
                        elif int_option == 2:
                            # scelgo un file dalla cartella e lo aggiungo alla directory
                            print "aggiunta file"
                        elif int_option == 3:
                            # scelgo un file dalla directory (tra i miei) e lo rimuovo
                            print "rimozione file"
                        elif int_option == 4:
                            # creo una query e la invio agli altri supernodi
                            print "query file"
                            # aspetto i risultati
                            print "wait 20s"

                            not_done = True
                            while not_done:
                                output(out_lck, "Select one of the following options ('e' to exit):")
                                output(out_lck, "1: View query results")
                                output(out_lck, "2: Download")

                                int_option = None
                                try:
                                    option = raw_input()
                                except SyntaxError:
                                    option = None

                                if option is None:
                                    output(out_lck, "Please select an option")
                                elif option == 'e':
                                    output(out_lck, "Bye bye")
                                    server.stop()
                                    sys.exit()  # Interrompo l'esecuzione
                                else:
                                    try:
                                        int_option = int(option)
                                    except ValueError:
                                        output(out_lck, "A number is required")
                                    else:
                                        if int_option == 1:
                                            # stampo a video i risultati della ricerca
                                            print "risultati"
                                        elif int_option == 2:
                                            # stampo i risultati e faccio scegliere il file da scaricare
                                            print "risultati + download"

                                            # Torno al menu principale
                                            not_done = False

                                        else:
                                            output(out_lck, "Option " + str(int_option) + " not available")

                        else:
                            output(out_lck, "Option " + str(int_option) + " not available")



        else:
            # se trovo almeno un supernodo faccio scegliere quale utilizzare per fare il login
            output(out_lck, "Select a supernode to log in:")
            output(out_lck, "lista supernodi")

            int_option = None
            while int_option is None:
                try:
                    option = raw_input()
                except SyntaxError:
                    option = None

                if option is None:
                    output(out_lck, "Please select an option")
                else:
                    try:
                        int_option = int(option)
                    except ValueError:
                        output(out_lck, "A number is required")
                    else:
                        #TODO: impostare l'indirizzo del supernodo che fa da directory
                        p.dir_ipv4 = ""
                        p.dir_ipv6 = ""
                        p.dir_port = ""

                        # faccio il login
                        #p.login()
                        p.session_id = "269d4afsfdaf645as1"

                        while p.session_id is not None:
                            print_menu_top(out_lck)
                            output(out_lck, "## Select one of the following options:               ##")
                            output(out_lck, "## 1: Add file                                        ##")
                            output(out_lck, "## 2: Delete file                                     ##")
                            output(out_lck, "## 3: Search file                                     ##")
                            output(out_lck, "## 4: Log out and exit                                ##")
                            print_menu_bottom(out_lck)

                            int_option = None
                            try:
                                option = raw_input()
                            except SyntaxError:
                                option = None

                            if option is None:
                                output(out_lck, "Please select an option")
                            else:
                                try:
                                    int_option = int(option)
                                except ValueError:
                                    output(out_lck, "A number is required")
                                else:
                                    if int_option == 1:
                                        # scelgo un file dalla cartella e lo aggiungo alla directory
                                        print "aggiunta file"
                                        #p.share()
                                    elif int_option == 2:
                                        # scelgo un file dalla directory (tra i miei) e lo rimuovo
                                        print "rimozione file"
                                        #p.remove()
                                    elif int_option == 3:
                                        # creo una query e la invio agli altri supernodi
                                        print "query file"
                                        #p.search()


                                        not_done = True
                                        while not_done:
                                            output(out_lck, "Select one of the following options ('e' to exit):")
                                            output(out_lck, "1: View query results")
                                            output(out_lck, "2: Download")

                                            int_option = None
                                            try:
                                                option = raw_input()
                                            except SyntaxError:
                                                option = None

                                            if option is None:
                                                output(out_lck, "Please select an option")
                                            elif option == 'e':
                                                break
                                            else:
                                                try:
                                                    int_option = int(option)
                                                except ValueError:
                                                    output(out_lck, "A number is required")

                                                if int_option == 1:
                                                    # stampo a video i risultati della ricerca
                                                    print "risultati"
                                                elif int_option == 2:
                                                    # stampo i risultati e faccio scegliere il file da scaricare
                                                    print "risultati + download"

                                                    not_done = False
                                                else:
                                                    output(out_lck, "Option " + str(int_option) + " not available")
                                    elif int_option == 4:
                                        print "logging out"
                                        p.session_id = None

                                    else:
                                        output(out_lck, "Option " + str(int_option) + " not available")


