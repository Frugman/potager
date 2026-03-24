# 🌱 Outil Potager 2026 - Solarpunk PWA

L'**Outil Potager 2026** est une application web progressive (PWA), "Low-Tech" et un peu *Solarpunk*, conçue pour gérer un potager de permaculture. 
Elle fonctionne entièrement dans votre navigateur mobile ou PC, sans aucun serveur complexe ni base de données coûteuse. Tout repose sur deux simples fichiers JSON hébergés sur GitHub qui servent de mémoire à l'application.

---

## 🛠️ Philosophie et Architecture Globale

- **0% Backend, 100% Client :** Tout le code (HTML, CSS, JS) est statique. L'application interroge et modifie directement les fichiers de données via l'API REST de GitHub en utilisant un jeton personnel stocké dans le navigateur (`localStorage`).
- **Low-Tech et Frugal :** Poids total de l'application : ~400 Ko. Aucune dépendance externe (pas de framework lourd comme React ou Vue). Le tout est stylisé en CSS brut et Javascript Vanilla.
- **Cache Local & Mobile :** Conçu pour se lancer comme une application mobile via le fichier `manifest.json`.

---

## ⚙️ Les Fichiers de Données

Toute l'intelligence de l'outil repose sur deux fichiers textuels manipulés en direct :

1. **`semences.json` (Le Cœur Agronomique)** :
   - Contient l'encyclopédie des variétés (Tomates, Courges, Alliacées...).
   - Centralise les durées de germination, distances, profondeurs, températures de levée.
   - Liste les "Bons" et "Mauvais" compagnons.
   - Contient les "Tâches automatiques" sous forme matricielle et les recommandations ciblées par région (ex: Vendée).

2. **`journal.json` (L'Historique Réel)** :
   - Le journal de bord de l'utilisateur.
   - Enregistre chaque action (Semis, Repiquage, Plantation, Arrachage, Récolte, Note) avec le lieu (`bac` ou `emplacement`), la date, et les quantités.

---

## 🚀 Fonctionnalités Principales

### 1. 📅 **L'Agenda Intelligent (La "Loi du Samedi")**
L'outil s'occupe de la charge mentale. À chaque "Semis" ou "Plantation" enregistré dans le journal, l'application recalcule les dates prévisionnelles de Repiquage et de Récolte. 
- **Regroupement (Batching) :** Si une tâche de soin ou une plantation tombe un mercredi, elle est algorithmiquement décalée au **Samedi le plus proche** pour optimiser le temps au jardin (Batching agronomique).
- **Levées sous surveillance :** L'algorithme isole l'attente de germination dans un encart spécifique "Levées" visible 14 jours.

### 2. ⚠️ **Le Radar de Compagnonnage (Cross-Validation)**
Lors d'une action de Semis ou de Plantation dans un bac précis (via l'Action Express) :
- L'outil scanne en arrière-plan toutes les plantes biologiquement actives dans ce même contenant cette année.
- Il compare les *"Mauvais compagnons"* de la nouvelle graine avec les anciennes, **en réciprocité absolue** (Si A déteste B, ou si B déteste A).
- Une alerte rouge s'affiche dynamiquement pour vous prévenir du conflit (ex: Tomate vs Betterave), mais de façon non bloquante.

### 3. 📝 **Le Menu "Action Express"**
Basé sur une interface mobile fluide, il permet d'enregistrer des événements au potager en 3 secondes : Semis, Repiquage, Plantation, Récolte, Arrachage, Note. 
- Les champs du formulaire se transforment selon l'action (un "Semis" demande un "Contenant", une "Plantation" cible un "Bac").
- Des photos peuvent être associées directement aux entrées du journal en convertissant les images en de légers encodages hébergés directement sur le dépôt GitHub.

### 4. 🌤️ **Météo Agricole (Open-Meteo)**
Prévisions à 7 jours basées sur une API ouverte sans clé. L'outil récupère gratuitement les données de températures, précipitations et risques de gel ciblées sur la position géographique.

### 5. 🗺️ **Le Plan Interactif 2D (Mode Bureau)**
Une interface visuelle exclusive aux ordinateurs pour cartographier vos bacs en métal (`Bac A` à `Bac E`).
- **Drag & Drop de Jetons :** Glissez-déposez vos semences depuis votre bibliothèque vers vos bacs.
- **Icônes Personnalisées :** Système de rendu 1:1 utilisant les images de `img/seeds/` basées sur l'ID des semences.
- **Cloud-Sync & Multi-saves :** Vos plans ne sont plus locaux. Ils sont sauvegardés sur GitHub dans un dossier `/saves/`. L'application permet de sauvegarder plusieurs versions (datées) et de charger celle de votre choix à tout moment, garantissant une synchronisation parfaite sur tous vos appareils.
- **Mode Focus :** Navigation verticale par "scroll" pour passer d'un bac géant à l'autre et gérer précisément ses densités de plantation.

---

## 🖥️ Interface et Ergonomie (UX)

L'application s'adapte dynamiquement selon votre appareil :
- **Version Mobile :** Focus sur l'Action Express et le Journal pour une saisie rapide au jardin. 
- **Version Bureau :** Menu latéral fixe (Sidebar), affichage du Journal en deux colonnes (Saisie / Chronologie) et accès au Plan Interactif pour la phase de conception.
- **Navigation Premium :** Les icônes de la barre de menu ont été repensées pour être plus lisibles avec un indicateur visuel (liseré vert) sur la page active.
- **Filtres de Navigation :** Possibilité de filtrer le Journal et l'Agenda par **Mois (Saisonnier)** pour retrouver instantanément vos notes de l'année précédente ou vos semis du mois en cours.

---

## 🔧 Installation et Configuration

Pour faire tourner le projet vous-même :
1. **Hébergement :** Le code peut être placé sur n'importe quel hébergement statique (GitHub Pages est idéal).
2. **Accès API :** Depuis l'application web (Page *⚙️ Paramètres GitHub*), renseignez :
   - Votre nom d'utilisateur GitHub.
   - Le nom du dépôt.
   - Un `Token` ou **Jeton d'Accès Personnel (Classic)** ayant la permission `repo` (pour pouvoir écrire dans `journal.json` et `semences.json`).
3. L'application est prête à enregistrer vos premières récoltes !
