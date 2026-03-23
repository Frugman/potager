# Architecture & Evolutions - Outil Potager 2026
*Dernière session : Consolidation Agronomique et Ergonomie avancée*

Ce document sert de "mémoire morte" pour reconstruire le contexte de développement si une IA doit reprendre le projet à l'avenir.

## 1. Ergonomie et Formulariation (UI/UX)
- **Consolidation "Gérer la Fiche"** : Le vieux fichier `ajout-semence.html` a été détruit au profit d'un système unique de création/modification sur `modifier-semence.html`. Utilisation de menus déroulants pour simplifier la saisie (Famille, Provenance "Kokopelli, Vilmorin...").
- **Action Express (Accueil)** : Les champs d'ajouts de notes (`index.html`) sont devenus ultras dynamiques. Remplacement de l'alerte sur la page Journal par une modalité fluide embarquée.
- **Historique Rendu Actif** : L'intégralité des encarts historiques affichant les anciennes notes (sur `fiche-semence.html` et l'accueil) disposent d'un déclencheur Javascript propre amenant directement sur l'éditeur (`modifier-journal.html?id=[id]`).
- **CSS** : Correction de l'ADN visuel. Ajout systématique de la classe manquante `.info-label` (vert majuscule), et bascule du texte des notes vers le blanc (`var(--text-primary)`) pour garantir la lisibilité sur mobile.
- **Tableau de Bord** : Hausse de l'affichage des futures actions (Agenda widget, passe de 5 à 10 items).
- **Problème Système (Favicon)** : L'Url cassée externe vers `favicon.png` sur les 11 fichiers a été remplacée par un appel relatif classique au fichier lourd `icon.png` (PWA).

## 2. Le Moteur "Associations & Amis/Ennemis" (Cross-Validation)
- **Refonte Base de Données** : Les associations uniques en texte libre du JSON (`associes`) ont été migrées vers deux arrays stricts : `bons_compagnons` et `mauvais_compagnons`.
- **UI de Saisie des Plantes Compagnes** : Abandon des sélecteurs `<select multiple>` (dangereux sur mobile). Création d'un système de badges verts/rouges alimenté par une balise `<datalist>` croisée en temps réel sur la liste complète des semences existantes.
- **Intercepteur d'Erreur Agronomique (Non-Bloquant)** : Ajout d'une IA locale dans l'Action Express. Lors de la saisie d'un plan dans un contenant défini ("Bac A"), la fonction Javascript `checkAssociations()` charge le `journal.json`, extrait la liste des plantes actives du bac sur l'année, puis boucle la comparaison des matrices `mauvais_compagnons` en **réciprocité absolue**. Si danger de culture, un bandeau rouge s'injecte délicatement sans stopper le bouton de soumission.

## 3. Base de Données Agronomique Experte (Update Massif Kokopelli)
La base `semences.json` (environ 60 plantes de permaculture pour la Vendée) a été modifiée par scripts Python successifs (Batch 1 à 7) :
- Les données comme les durées germinatives (ex: Alliacées limitées à 1-2 ans ; Boraginacées boostées à 8 ans), l'exposition, et le besoin en eau ont été remplies "à la dure".
- Ajustement des profondeurs et styles de semis avec précisions manuelles pointues (ex: graine de concombre "sur la tranche", courgette "pointe vers le bas" pour faciliter l'ancrage). 
- Annulation pure et simple des délais de "repiquage" pour les plantes à racine pivotante (Mâche, Pavot, Bourrache...).
- Avertissements climatiques inscrits au coeur du JSON (Thermo-dormances de l'Epinard formellement inscrites si terre > 20°C ; inverse pour la Fève qui a besoin de 5°C).

## 4. Révolution des "Dates Cibles de Semis"
- Abandon total du système vague des mois nominatifs (`["Mars", "Avril"]`) au profit de l'Objectif de Semis ciblé vendéen par le "Coach IA".
- Chaque fiche semence affiche une date fixe "Samedi X" avec un paragraphe technique adossé au fond de son JSON. Les modifications de `modifier-semence.html` ont été converties pour interagir avec `<input type="date">` et rendre ces alertes personnalisables à perpétuité.

## 5. Algorithmique Avancée du Calendrier & Agenda
- **Gestion du Semis Direct :** L'algorithme (`index.html` et `agenda.html`) détecte désormais les plantations sans caissettes. Si le `contenant` est déclaré comme `Pleine terre (sans contenant)` lors d'un "Semis", les futures tâches de "Repiquage" et de "Plantation" sont purement annulées et masquées car inutiles. La date estimée de récolte est alors recalculée pour devenir exacte.
- **Extraction des "Levées" :** L'attente d'une graine n'est pas une tâche physique. L'évènement "🌱 Levée attendue" a donc été extrait du flux principal de l'Agenda. Ces événements sont désormais captés et regroupés dans un nouvel encart dynamique sur l'Accueil : `👀 LEVÉES SOUS SURVEILLANCE`, qui n'apparaît que si des graines doivent germer dans les 14 jours.
- **Batching et Loi du Samedi :** Transformation radicale de la charge mentale de l'outil. Toute action physique (Repiquage, Semis, Plantation) bénéficie d'une méthode `getClosestSaturday()`. Si l'algorithme tombe sur un Mercredi, il reculera la tâche au Samedi, si c'est un Vendredi il poussera au Samedi d'après.
- **Interface Groupée (Clustering) :** L'affichage en liste brouillonne a été remplacé par une Interface unie regroupant toutes les missions agronomiques sous forme de listes à puces à l'intérieur de vastes cadres intitulés : *📆 Samedi [Date]* (Batch processing absolu).

## 6. Plan Interactif 2D et Ergonomie Desktop (V2.5)
- **Système de Navigation Latérale :** Introduction d'une sidebar fixe à gauche (`.nav-bar` en `position: fixed`) pour les résolutions > 1024px. Ajout de liens directs vers le **Journal** et la **Météo** pour optimiser l'espace écran.
- **Le Plan Visuel Interactif (`plan-visuel.html`) :** Création d'un module de conception 2D exclusif au format bureau.
    - **Architecture Verticale :** Abandon du plan fixe "une seule vue" au profit d'un défilement vertical (`overflow-y: auto`) permettant d'afficher des bacs géants (90% de largeur) pour une meilleure précision de placement.
    - **Moteur de Drag & Drop :** Implémentation d'un système de "glisser-déposer" avec gestion des coordonnées absolues lors du drop. Les plants sont clonés depuis une palette "sticky" qui suit l'utilisateur durant son scroll.
    - **Rendu Iconographique 1:1 :** Transition d'une spritesheet générique vers un système d'icônes individuelles haute définition (`img/seeds/[id].png`). Le code mappe automatiquement les semences à leurs illustrations via l'ID unique.
    - **Persistance LocalStorage :** Sauvegarde de l'état du plan (positions X/Y et IDs) dans le `localStorage` sous la clé `potager_plan2D` pour garantir la reprise du travail entre deux sessions sans alourdir le JSON distant.
    - **Alignement Magnétique (Snap-to-Grid) :** Mise en place d'une grille d'aimantation de 50px pour garantir un alignement parfait des pastilles de cultures. Ajout d'une option d'affichage de la grille visuelle (subtile) directement sur l'interface du plan pour faciliter la conception.
- **Filtres de Saisie Saisonnière :** Ajout de sélecteurs de mois dans le Journal et l'Agenda. Le filtrage s'exécute en local sur les données déjà chargées (`globalJournal` ou `allTasks`), permettant une navigation fluide et instantanée dans l'historique des cultures.
- **Optimisation Mobile/Desktop :** Utilisation des classes CSS `.desktop-only` et `.mobile-only` pour épurer l'interface selon le contexte d'usage (masquage du plan complexe sur smartphone avec message d'avertissement).

