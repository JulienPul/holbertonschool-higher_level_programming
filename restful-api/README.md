# 📡 Introduction aux API, HTTP/HTTPS et curl

Ce projet vise à comprendre le fonctionnement des **protocoles HTTP et HTTPS**, les **méthodes HTTP**, les **codes de statut**, et à savoir **interagir avec une API** depuis le terminal à l’aide de `curl`.

---

## 🔐 1. Différences entre HTTP et HTTPS

| Critère                           | HTTP                                           | HTTPS                                                     |
| --------------------------------- | ---------------------------------------------- | --------------------------------------------------------- |
| **Signification**                 | HyperText Transfer Protocol                    | HyperText Transfer Protocol **Secure**                    |
| **Port par défaut**               | `80`                                           | `443`                                                     |
| **Chiffrement**                   | ❌ Aucun                                        | ✅ Données **chiffrées** avec **SSL/TLS**                  |
| **Authentification**              | ❌ Non                                          | ✅ Via certificat SSL                                      |
| **Intégrité des données**         | ❌ Non                                          | ✅ Protège contre les modifications                        |
| **Vulnérabilité**                 | ✅ Très exposé                                  | ❌ Protégé contre le sniffing et MITM                      |
| **Indicateur navigateur**         | Non sécurisé                                   | 🔒 Cadenas + https://                                      |
| **Utilisation typique**           | Sites simples/test                             | Sites avec **données sensibles**                          |

---

## 📬 2. Méthodes HTTP courantes

| Méthode    | Description                                                | Exemple d’usage                                              |
| ---------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **GET**    | Lire une ressource                                         | Afficher un profil utilisateur                               |
| **POST**   | Créer une nouvelle ressource                              | Ajouter un nouveau post ou formulaire                        |
| **PUT**    | Modifier complètement une ressource                        | Remplacer un profil utilisateur                              |
| **DELETE** | Supprimer une ressource                                    | Supprimer un commentaire ou un utilisateur                   |

---

## 🧾 3. Codes de statut HTTP utiles

| Code    | Signification         | Description                                  | Exemple                                                      |
| ------- | ---------------------| -------------------------------------------- | ------------------------------------------------------------ |
| **200** | OK                    | Requête réussie                              | Une API renvoie les données demandées                        |
| **301** | Moved Permanently     | Redirection permanente                       | Ancien site redirige vers le nouveau                         |
| **400** | Bad Request           | Erreur de syntaxe dans la requête            | Champs manquants dans un formulaire                         |
| **401** | Unauthorized          | Authentification requise                     | Accès interdit sans token ou mot de passe                    |
| **404** | Not Found             | Ressource introuvable                        | Route ou utilisateur inexistant                             |

---

## ⚙️ 4. Structure d’une requête / réponse HTTP

### 📨 Requête (client → serveur)

```http
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
