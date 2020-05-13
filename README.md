# Récapitulatif

Master 1

## Description projet

Réseaux de neurone de type DCGAN pour générer des cards Magic [https://magic.wizards.com/fr](https://magic.wizards.com/fr)


## Search Informations

 API:
 - [https://scryfall.com/docs/api](https://scryfall.com/docs/api) le récupérateur est situer a /scriptDB/dlDB.py
        
 DataSet:
  - [https://www.quora.com/How-do-I-create-a-dataset-like-MNIST-for-recognizing-another-language-characters-I-have-dataset-as-a-folder-of-images-How-do-I-use-that-in-Tensorflow](https://www.quora.com/How-do-I-create-a-dataset-like-MNIST-for-recognizing-another-language-characters-I-have-dataset-as-a-folder-of-images-How-do-I-use-that-in-Tensorflow)
  - [https://keras.io/preprocessing/image/](https://keras.io/preprocessing/image/) exemple dans le fichier /scriptDB/createDataSet.py
        
 DCGAN:
  - [https://towardsdatascience.com/implementing-a-generative-adversarial-network-gan-dcgan-to-draw-human-faces-8291616904a](https://towardsdatascience.com/implementing-a-generative-adversarial-network-gan-dcgan-to-draw-human-faces-8291616904a)
  - [https://www.tensorflow.org/tutorials/generative/dcgan](https://www.tensorflow.org/tutorials/generative/dcgan)
  - [https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html]( https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html)

 Model/Base:
  - [https://github.com/jacobgil/keras-dcgan](https://github.com/jacobgil/keras-dcgan) premier trouvé modification non fonctionel a /sriptDB/GANMagicOLD.py
  - [https://github.com/Goldesel23/DCGAN-for-Bird-Generation](https://github.com/Goldesel23/DCGAN-for-Bird-Generation) trouvé après recherche contient les model et la fonction d'entrainement modification fonctionnel a /scriptDB/GANMagic
 
 ## Réalisation
 
 Les model et le train du model sont en grande partie tiré du DCGAN-Bird-Generation, très efficace mais lourd, le discriminator allant de 64 à 512 pour les conv2D, de meme que les Déconvolution du générateur startant a 256.
 
 L'utilisation de pyplot pour la création du graph pourait etre remplacer par TensorBoard.
 
 Pour une amélioration du rendu (impliquant une hausse du temps d'apprentissage) utiliser les dimmention original des image.
 
 Mais temps insuffisant car pour un resultat non optimal 11h de calcul pour 50 epoch avec calcul sur le GPU, un apprentissage de au moin 100 à 150 epoch serais plus indiquées.
 
 Pour reduire la loss du generator revoir à modifier la taille du filtre et du kernel_size.
 
 ## Usage

 ```python GANMagic --mode gen```

 Les images créé arriverons dans le dossier final_cards

 ```python GANMagic --mode train```

 Pour entrainé les réseaux mais au préalable lancé le script scriptDB/dlDB.py /!\ Opération longue et couteuse en réseaux/mémoire (~32000 images)
 
