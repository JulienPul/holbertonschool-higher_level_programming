| ✅ **Commande SQL**               | 🎯 **Utilisation**                                                   | 🧱 **Agit sur**       | 💡 **Remarques**                                      |
| -------------------------------- | -------------------------------------------------------------------- | --------------------- | ----------------------------------------------------- |
| `CREATE DATABASE`                | Crée une base de données                                             | base                  | Utilise `IF NOT EXISTS` pour éviter les erreurs       |
| `CREATE TABLE`                   | Crée une table dans une base                                         | table                 | Doit être exécutée après `USE nom_de_la_base`         |
| `INSERT INTO`                    | Ajoute une ou plusieurs lignes                                       | données (lignes)      | Peut insérer plusieurs lignes en une commande         |
| `SELECT`                         | Récupère des données                                                 | données               | Ne modifie rien                                       |
| `UPDATE`                         | Modifie des valeurs dans des lignes existantes                       | données (lignes)      | Peut être combiné avec `WHERE` pour cibler            |
| `DELETE FROM`                    | Supprime des lignes d’une table                                      | données (lignes)      | Utilise `WHERE` pour éviter de tout effacer           |
| `TRUNCATE TABLE`                 | Supprime **toutes** les lignes d’une table, plus rapide que `DELETE` | données               | Ne peut pas être annulé, plus radical                 |
| `DROP TABLE`                     | Supprime une table (et toutes ses données)                           | structure (table)     | Utilise `IF EXISTS` pour ne pas provoquer d’erreur    |
| `DROP DATABASE`                  | Supprime une base de données entière                                 | structure (base)      | Supprime toutes les tables dedans                     |
| `ALTER TABLE`                    | Modifie la structure d’une table (ajout colonne, clé, etc.)          | structure (table)     | Très utile pour évoluer sans supprimer                |
| `USE nom_de_la_base`             | Active une base pour y exécuter des commandes                        | environnement courant | À exécuter avant toute création de table ou insertion |
| `SHOW TABLES` / `SHOW DATABASES` | Affiche les bases/tables existantes                                  | information           | ❗ Interdit dans certains exos Holberton               |
| `DESCRIBE table_name`            | Affiche la structure d’une table                                     | information           | Pour voir les colonnes, types, clés                   |
