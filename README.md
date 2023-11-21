## 野球の部屋

このサイトは、データを用いて、野球の見方を変える。

## ER図
``` mermaid
erDiagram
user{
    int id
    char name
    char address
}

senshu{
    char name
    char teamename
    char information
    int seiseki
}

teame_information{
    char teamename
    int jyuni
    int winner
    int lose
    int draw
    int shouritu 
    int teamdaritu
    int teamebougyorit
    int teamesenepatubougyoritu
    int teamenakatugibougyoritu
    int senshu_name
    int senshu_seiseki
}


title{
    int senshu_name
    int senshu_teamename
    int senshu_seiseki
}

teame_jyuni{
    int teame_information_jyuni
    char teame_information_teamename
    int teame_information_winner
    int teame_information_lose
    int teame_information_draw
    int teame_information_teamdaritu
    int teame_information_teamebougyorit
    int teame_information_shouritu
}

senshu |o --o{ teame_information : ""
senshu |o --o{ title : ""
teame_information |o --o{ teame_jyuni : ""

```