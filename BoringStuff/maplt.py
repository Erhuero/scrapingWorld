#! python3
#mapIt.py
import webbrowser, sys #ouvre un moteur de recherche sur une page specifique
#webbrowser.open('http://inventwithpython.com')#ouvre la page indiquee

if len(sys.argv)>1:#evalue si la ligne de commande à bien ete donnee
	address = ' '.join(sys.argv[1:])#sys.argv est une liste de string, on enleve aussi les premiers élèments de la rangee

