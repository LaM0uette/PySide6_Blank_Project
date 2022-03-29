# MyApp
## Courte présentation

MyApp est une sorte d'application "Modèle" qui a pour but de faciliter la création de multiples   
applications facilement et rapidement en customisant les différents Widgets de manière simple et efficace.

## Fonctions

- Comprend tout ce dont une application de base a besoin.
- Des Widgets 100% personnalisables.
- Des fenêtre de dialogue 100% personnalisables.
- Un menu d'option déjà pré fait.
- Des fonctions élémentaires préconstruite.
- Les images SVG se régénères selon le thème choisit.

## Charte
> ## Couleur :
> th1 = Primaire  
> th2 = Secondaire  
> th3 = Tertiaire   
> bn1 = Bonus 1   
> bn2 = Bonus 2   
> 
> <br>
> 
> ## Fonctions :
> Pas d'espaces entre des fonctions de même usage.   
> Placer les fonctions entre des balises de commentaires.   
> Séparer les groupes de fonctions come ceci :
> ```
> def groupe_1():
>   pass
> 
> #####
> 
> def groupe_2():
>   pass
> ```
> 
> ### Nomenclature du nom des fonctions :
> ***Fonctions :*** f_nom_de_la_fonction   
> ***Fonctions "Masqué" :*** _f_nom_de_la_fonction   
> 
> ***Événement :*** e_nom_de_la_fonction   
> ***Événement "Masqué" :*** _e_nom_de_la_fonction   
> 
> ***Actions :*** a_nom_de_la_fonction   
> ***Actions "Masqué" :*** _a_nom_de_la_fonction   
> 
> ***Fonctions externes :*** NOM_DE_LA_FONCTION   
> ***Fonctions externes "Masqué" :*** _nom_de_la_fonction   
> 
> ## Classes :
> Pas d'espaces entre des fonctions de même usage.   
> Mettre des arguments explicits.   
> 
> ### Nomenclature du nom des classes :
> ***Classe principal :*** NomDeLaClasse   
> ***Classe diverse :*** nomDeLaClasse

<br>

## Fonctionnement
> ### Initialisation :
> 
> Il s'agit d'un groupe de liste avec une fonction ainsi qu'une brève description.   
> Toutes les fonctions mise à l'intérieur seront exécuté au début du programme.
> 
> ``` py
> self.INIT(
>     [self.IN_BASE, "Configuration des éléments principaux"],
>     [self.IN_SETUP_UI, "Setup de l'interface graphique"],
>     [self.IN_CLASSE, "Initialisation des Widgets"],
>     [self.IN_WG, "Configuration de base des Widgets"],
>     [self.IN_CONNECTIONS, "Ajout des connexions"],
>     [self.IN_ACT, "Fonctions de base"],
>     [self.IN_WG_BASE, "Etat de base des Widgets"],
>     [self.IN_TRAY, "Finalisation de la configuration"]
> )
> ```
> 
> ***self.IN_BASE :*** Permet les configurations de base de l'application.   
> ***self.IN_SETUP_UI :*** Configure l'interface graphique.   
> ***self.IN_CLASSE :*** Initialise les classes de chaque widget.   
> ***self.IN_WG :*** Initialise les Widgets (texte, img, dimension, ...).   
> ***self.IN_CONNECTIONS :*** Créer les connections des Widgets.   
> ***self.IN_ACT :*** Lance des fonctions au démarage.   
> ***self.IN_WG_BASE :*** Initialise des états de base (CheckBox, CurrentItem, ...).   
> ***self.IN_TRAY :*** Créer le trayIcon.
> 
> Fichier de configuration : src > config > config.json
> 
> <br>
> 
> ### Imports :
> Pour importer de manière globale tous les modules, il suffit de faire :
> ```py
> from src import *
> ```
> Cependant, il faut faire attention à ne pas importer un module en boucle.   
> Si vous importer le module ```Rgb``` dans le fichier Rgb le programme ne pourras pas se lancer.
> 
> <br>
> 
> ### Palettes :
> Il y a des palettes mises à disposition et utilisable partout.
> Pour importer le module il suffit de faire :
> ```py
> from src.lib.palettes import *
> ```
> 
> Ensuite, il suffit d'écrire : nomPalette.VALEUR 
>    
> Voici un exemple pour chaque palette :
> - ***PaAlign :*** PaAlign.TOP
> - ***PaArrowType :*** PaArrowType.NO
> - ***PaAutoFormating :*** PaAutoFormating.NONE
> - ***PaButtonSymbols :*** PaButtonSymbols.NO
> - ***PaCur :*** PaCur.CRAYON
> - ***PaDim :*** PaDim.H4
> - ***PaDragDropMode :*** PaDragDropMode.DRAG_AND_DROP
> - ***PaDropAction :*** PaDropAction.MOVE
> - ***PaEchoMode :*** PaEchoMode.NORMAL
> - ***PaFlow :*** PaFlow.LEFT_TO_RIGHT
> - ***PaFocusPolicy :*** PaFocusPolicy.NO
> - ***PaFont :*** PaFont.TEXTE
> - ***PaFrameShadow :*** PaFrameShadow.PLAIN
> - ***PaFrameShape :*** PaFrameShape.NO
> - ***PaImg :*** PaImg.ALERTE
> - ***PaInputMask :*** PaInputMask.NO
> - ***PaInsertPolicy :*** PaInsertPolicy.NO
> - ***PaKeys :*** PaKeys.F1
> - ***PaLayoutDirection :*** PaLayoutDirection.LEFT_TO_RIGHT
> - ***PaPopupMode :*** PaPopupMode.DELAYED
> - ***PaProgressFormat :*** PaProgressFormat.PERCENTAGE
> - ***PaRgb :*** PaRgb.TH2
> - ***PaScroll :*** PaScroll.ON
> - ***PaSelectionBehavior :*** PaSelectionBehavior.ROW
> - ***PaSelectionMode :*** PaSelectionMode.NO
> - ***PaShadow :*** PaShadow.OMBRE_PORTEE(wg)
> - ***PaSizePolicy :*** PaSizePolicy.FIXED
> - ***PaStyleBase :*** PaStyleBase.BORDER
> - ***PaTextFormat :*** PaTextFormat.PLAIN
> - ***PaTickPosition :*** PaTickPosition.NO
> - ***PaToolButtonStyle :*** PaToolButtonStyle.ICON_ONLY
> 
> ### Widgets :
> Chaque widget possède sa propre classe (src/widgets/"nomDuWidget"/"nomDuWidget")   
> Pour créer une nouvelle ```class``` pour le widget choisit, il suffit de l'ajouter dans le fichier au nom du widget.   
> Vous pouvez ensuite appeler ces ```class``` dans les fichiers d'ui.  
> Dans la doc, %.. Signifie qu'il faut remplacer le texte par votre valeur. # ex: Rgb().%nomCouleur() == Rgb().th3()   
> 
> ### Dialogues :
> Des fenêtres de dialogues sont déjàs préconstruites.
> Pour importer le module il suffit de faire :
> ```py
> from src.gui import *
> ```
> 
> Ensuite, il suffit d'écrire : nomDlg().typeDlg()   
>    
> Voici un exemple pour chaque dialogue :
> - ***Saisie de texte :*** InputBox.TXT(*arguments)
> - ***Message :*** MsgBox.INFO(*arguments)
> - ***Menu d'option :*** OptionBox.MAIN(*arguments)
> - ***Demande de validation :*** ResponseBox.INFO(*arguments)
> - ***Choix d'une couleur :*** RgbBox.GET(*arguments)
> 