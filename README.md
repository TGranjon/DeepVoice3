# DeepVoice3

Dans ce dépôt se trouvent tout le contenu du projet Deep Voice 3 sur lequel j'ai travaillé le long de mon stage au sein du LIUM du 21/01/2019 au 05/07/2019.

Note : Les corpus utilisés sont LJ Speech (en anglais) et SynPaFlex (en français) et ils ne sont pas inclus dans ce dépôt.

Chaque répertoire possède son propre README pour donner plus de détails sur le fonctionnement et les modifications apportées.

## Contenu

On y trouve les différents répertoires :
  - deepvoice3_by_tg : le synthétiseur Deep Voice 3 fonctionnel en français avec Griffin-Lim ou WaveNet
  - deepvoice3_world : une tentative de mêler Deep Voice 3 et WORLD
  - evaluation : des fichiers pré et post évaluation
  - merlin : une tentative de faire fonctionner le synthétiseur Merlin sur du français
  - scripts : différents scripts bash ou python pour faire fonctionner tous les programmes
  - tacotron : une version très peu modifiée de Tacotron pour le comparer à Deep Voice 3
  - wavenet_vocoder : le vocodeur WaveNet, fonctionnel sur du français
  - world_vocoder : le vocodeur WORLD, très peu modifié
  
## Crédits

_Je rends à César ce qui appartient à César._ Je ne suis pas le créateur de tous ces logiciels, voici leur origine :
  - deepvoice3_by_tg : https://github.com/r9y9/deepvoice3_pytorch
  - deepvoice3_world : https://github.com/geneing/deepvoice3_pytorch
  - merlin : https://github.com/CSTR-Edinburgh/merlin
  - tacotron : https://github.com/r9y9/tacotron_pytorch
  - wavenet_vocoder : https://github.com/r9y9/wavenet_vocoder
  - world_vocoder : https://github.com/JeremyCCHsu/Python-Wrapper-for-World-Vocoder
