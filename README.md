# 🚗 ft_linear_regression  
**Apprendre le Machine Learning à partir de zéro en prédisant le prix des voitures**

Une implémentation simple et claire d’un **modèle de Machine Learning construit from scratch** pour prédire le prix d’une voiture à partir de son kilométrage.

Ce projet met l’accent sur la **compréhension du fonctionnement de l’apprentissage**, et non sur l’utilisation de bibliothèques « boîte noire ».

---

## ✨ Ce que fait ce projet

Ce projet apprend à un ordinateur à :
- observer des ventes de voitures passées  
- comprendre la relation entre le kilométrage et le prix  
- prédire le prix d’une nouvelle voiture jamais vue auparavant  

Il utilise l’une des techniques les plus fondamentales du machine learning : **la régression linéaire**.

---

## 🧠 Qu’est-ce que le Machine Learning ?

Le machine learning consiste à **ne pas donner de règles fixes à l’ordinateur**.

Au lieu d’écrire :
> « Si le kilométrage est élevé, le prix est bas »

on donne à l’ordinateur beaucoup d’exemples et on le laisse **découvrir la règle par lui-même**.

Plus il voit d’exemples, meilleur il devient.

---

## 📈 Qu’est-ce que la régression linéaire ?

La régression linéaire est une manière pour une machine d’apprendre une **tendance**.

Dans ce projet, la tendance est :
> comment le prix d’une voiture change quand le kilométrage augmente.

Le modèle trouve une droite qui représente le mieux cette relation et l’utilise pour faire des prédictions.

---

## ❌ Comment le modèle sait qu’il se trompe ?

Chaque prédiction est comparée au vrai prix.

Si la prédiction est loin de la réalité, le modèle sait qu’il a fait une erreur.

L’entraînement consiste simplement à :
> réduire ces erreurs petit à petit.

---

## 🔁 Comment l’apprentissage fonctionne-t-il ?

Le processus d’apprentissage se déroule ainsi :

1. Le modèle fait une prédiction  
2. Il mesure à quel point elle est fausse  
3. Il s’ajuste légèrement  
4. Il recommence  

En répétant cela de nombreuses fois, le modèle devient de plus en plus précis.

C’est ainsi que l’ordinateur apprend.

---

## 🧭 Qu’est-ce que le Gradient Descent ?

Le gradient descent est la méthode utilisée pour améliorer le modèle.

Cela signifie :
> faire de petits pas dans la direction qui réduit les erreurs.

Comme descendre une colline dans le brouillard :
on ne voit pas le bas, mais on avance toujours dans la direction qui descend.

À la fin, on atteint la meilleure solution possible.

---

## 📊 Pourquoi mettre les données à l’échelle ?

Les valeurs de kilométrage peuvent être très grandes (100 000 km, 200 000 km, etc).

De grands nombres rendent l’apprentissage instable et lent.

On met donc les données à l’échelle pour que le modèle apprenne :
- plus vite  
- plus régulièrement  
- plus efficacement  

C’est une pratique standard en machine learning.

---

## ⚙️ Comment ça marche

### 1. Entraînement
Le programme d’entraînement :
- lit le jeu de données  
- apprend la relation entre kilométrage et prix  
- sauvegarde ce qu’il a appris  

### 2. Prédiction
Le programme de prédiction :
- charge le modèle appris  
- demande un kilométrage  
- affiche un prix estimé  

On entraîne une fois, puis on peut prédire autant de fois qu’on veut.

---

## 🎯 Pourquoi ce projet est important

Ce projet enseigne les bases de :
- comment les machines apprennent  
- comment les données deviennent des prédictions  
- comment les erreurs guident l’amélioration  

Ces mêmes idées sont utilisées dans :
- les systèmes d’IA  
- les moteurs de recommandation  
- les voitures autonomes  
- et les modèles modernes de deep learning  

C’est ici que le machine learning commence.
