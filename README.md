## 野球の部屋

このサイトは、データを用いて、野球の見方を変える。

## ER図
``` mermaid
erDiagram
user{
    int id
    char name
    char text
    char email
    char password
}

tokusetu{
    int id
    int game_number
    int hanshin_tigers_score
    int orix_buffaloes_score
}

```

