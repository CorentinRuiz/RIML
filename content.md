---
layout: default
title : Projets open source bon candidat d'apprentissage
date:   2023-11
---

---

   **Date de rendu finale : fin février**
   - Respecter la structure pour que les chapitres soient bien indépendants
   - Remarques :
        - La structure proposée est là pour vous aider, mais peut-être adaptée à votre projet
        - Les titres peuvent être modifiés pour être en adéquation avec votre étude. 
        - Utiliser des références pour justifier votre argumentaire, vos choix, etc.
        - Vous avez le choix d'utiliser le français ou l'anglais.

    Dans l'article de Blog [Debret 2020], l'auteure donne les éléments principaux de la démarche d'une manière simple et très facile à lire, dans la partie [Quelles sont les étapes d’une bonne démarche scientifique ?](https://www.scribbr.fr/article-scientifique/demarche-scientifique/#:~:text=La%20d%C3%A9marche%20scientifique%20permet%20d,de%20nouvelles%20hypoth%C3%A8ses%20%C3%A0%20tester.)

---

---
# TODO: Supprimer ce bandeau avant le rendu

Critères d'évaluation :
- Présentation des résultats
- Analyse des résultats et commentaires
- Lien avec les hypothèses
- Si nécessaires, préciser les limites
- Recul et Pertinence des remarques
- Retour sur vos contributions
- Perspectives
- Format : Structure, forme, ...
- Contexte dont la motivation
- Question générale : Formulation, intérêt, limites éventuelles.
- Quelle est votre base d'information
- Quelles sous-questions et hypothèses
- Quelles expérimentations, démarches choisies pour vérifier ou non vos hypothèses, justifications.
- Quels outils sont utilisés ?
- Justification des choix
- Résultats
- Conclusion
---

**_février 2024_**

## Authors

We are four students in final year of Polytech Nice-Sophia specialized in Software Architecture :

* Thomas GUIOT &lt;thomas.guiot@etu.unice.fr&gt;
* Antony MARTIN &lt;antony.martin@etu.unice.fr&gt;
* Christophe RUIZ &lt;christophe.ruiz@etu.unice.fr&gt;
* Corentin RUIZ &lt;corentin.ruiz@etu.unice.fr&gt;
* Cyril VROUSOS &lt;cyril.vrousos@etu.unice.fr&gt;

## I. Research context /Project

Les architectures microservices ont récemment émergé comme une approche dans le domaine du développement logiciel, offrant une alternative décentralisée aux structures monolithiques. Cette transition vers les microservices est motivée par le désir d'accroître la modularité, la flexibilité et la scalabilité des applications. Les projets open source embrassent de plus en plus ces architectures distribuées, reconnaissant leur potentiel à répondre aux exigences croissantes de systèmes logiciels complexes.

L'un des pattern les plus populaires intégrées aux architectures microservices est l'event-sourcing. Cette pratique de conception propose un modèle où chaque modification de l'état d'une application est enregistrée sous forme d'événement immuable. L'event-sourcing offre une traçabilité granulaire des changements, facilitant la reconstitution de l'état d'une application à n'importe quel moment. Dans le contexte des microservices, cette approche peut renforcer la cohérence des données dans des environnements distribués, améliorant ainsi la résilience et la gestion des transactions.

Une intégration réussie de l'event-sourcing dans les architectures microservices nécessite une bonne compréhension des échanges entre les services. L'adoption croissante de l'event-sourcing dans des projets open source souligne l'importance de cette intégration et pose des questions cruciales sur sa pertinence et son efficacité dans ce contexte spécifique.

En analysant les caractéristiques de l'intégration de l'event-sourcing, il devient possible d'identifier la complexité d'apprentissage associée à chaque projet. Cette évaluation permettra de catégoriser les projets en fonction de leurs approches et visions spécifiques de l'event-sourcing, contribuant ainsi à définir des modèles d'implémentation et à se renseigner sur les meilleures pratiques.

Par ailleurs, l'évaluation de la pertinence de l'implémentation de l'event-sourcing dans les projets open source en microservices offre une opportunité significative d'identification de cas d'utilisation exemplaires et d'approches novatrices. Ces exemples pourraient servir de références inspirantes pour d'autres développeurs et équipes de projet, favorisant ainsi la diffusion de bonnes pratiques et contribuant à l'amélioration continue de la qualité logicielle au sein de la communauté open source.

## II. Observations/General question

Notre sujet est motivé par la question suivante.

> Les projets open-source implémentés en micro-services sont-ils de bons candidats pour apprendre les principes des architectures micro-services ?

### Sous-question
Nous avons choisi de restreindre ce sujet à la question suivante.

> Comment les projets open source, adoptant l'architecture microservices et intégrant l'event-sourcing, parviennent-ils à garantir la cohérence des données dans des environnements distribués ?
    
TODO: Parler de la question CQRS et son lien avec le sujet
### Justification

Cette question découle de l'utilisation conjointe des architectures microservices et de l'event-sourcing dans les projets open source. L'intérêt réside dans le besoin de comprendre comment ces deux concepts interagissent pour assurer la cohérence des données dans des systèmes distribués. Cette compréhension est importante pour les développeurs, car elle permettra d'identifier des bonnes pratiques et de définir des modèles d'implémentation efficaces.

## III. Information gathering

---
1. **Scripts Python pour l'Exploration des Projets :**
   - Présentation du script de sélection des projets open source.
     - Critères de pertinence : Présence de Kafka dans un fichier Docker Compose.
   - Détails sur la taille de l'échantillon de projets sélectionnés.
   - Justification des critères de sélection pour garantir la représentativité.
   - Explication du processus de récupération des projets via l'API GitHub.
2. **Script d'Analyse des Communications avec Kafka :**
   - Description du script d'exploration des fichiers des projets sélectionnés.
     - Méthodologie : Recherche des lignes pertinentes en Java indiquant la production ou la consommation d'événements dans le bus (Kafka).
   - Présentation des choix techniques et des bibliothèques Python utilisées.
3. **Limites et Considérations :**
   - Mise en évidence des limites potentielles liées à la méthodologie d'échantillonnage et aux choix technologiques.
   - Discussion sur la représentativité des résultats obtenus.
---
### Exploration des projets
La première tâche est de constituer une base de projets sur lesquels effectuer nos expériences. Pour cela, nous avons
rédigé des scripts Python utilisant l'API GitHub afin d'identifier des projets qui pourraient nous correspondre. Un
projet éligible est un projet dont les services sont renseignés dans un fichier Docker Compose. Pour pouvoir répondre à
la sous-question, nous souhaitons aussi que Kafka soit présent dans le projet et donc rescencé dans le Docker Compose.

En appliquant ces critères, nous avons trouvé XXXXXXXXXX projets principalement écrits en Java et Python.

Par la suite, nous nous sommes concentrés sur un sous-ensemble de l'échantillon initial. Nous avons ainsi éliminé les
projets trop simples. Un projet trop simple est un projet XXXXXXXXXX.
 
## IV. Hypothesis & Experiences

---
1. Il s'agit ici d'**énoncer sous forme d'hypothèses** ce que vous allez chercher à démontrer. Vous devez définir vos hypothèses de façon à pouvoir les _mesurer/vérifier facilement._ Bien sûr, votre hypothèse devrait être construite de manière à _vous aider à répondre à votre question initiale_. Explicitez ces différents points.
2. Vous **explicitez les expérimentations que vous allez mener** pour vérifier si vos hypothèses sont vraies ou fausses. Il y a forcément des choix, des limites, explicitez-les.

:bulb: Structurez cette partie à votre convenance:  
Par exemples :  
- Pour Hypothèse 1 => Nous ferons les Expériences suivantes pour la démontrer  
- Pour Hypothèse 2 => Expériences ou Vous présentez l'ensemble des hypothèses puis vous expliquer comment les expériences prévues permettront de démontrer vos hypothèses.
---

Nous avons choisi de catégoriser les projets afin de mettre

## V. Result Analysis and Conclusion

1. Présentation des résultats
2. Interprétation/Analyse des résultats en fonction de vos hypothèses
3. Construction d’une conclusion 

     :bulb:  Vos résultats et donc votre analyse sont nécessairement limités. Préciser bien ces limites : par exemple, jeux de données insuffisants, analyse réduite à quelques critères, dépendance aux projets analysés, ...
4. On peut dire que certaines metriques sont pas forcément intéressantes

## VI. Tools \(facultatif\)

Précisez votre utilisation des outils ou les développements \(e.g. scripts\) réalisés pour atteindre vos objectifs. Ce chapitre doit viser à \(1\) pouvoir reproduire vos expérimentations, \(2\) partager/expliquer à d'autres l'usage des outils.

![Figure 1: Logo UCA, exemple, vous pouvez l'enlever](file://assets/images/logo_uca.png) {:height="12px"}


## VI. References

[Debret 2020] Debret, J. (2020) La démarche scientifique : tout ce que vous devez savoir ! Available at: https://www.scribbr.fr/article-scientifique/demarche-scientifique/ (Accessed: 18 November 2022).


