use myDB
show dbs
show tables
db.myCol.insert({"Person":[{"id":"201511116","이름":"손희수"},{"id":"201511108", "이름":"김요나"}]})
db.myCol.find({"Person.이름":"손희수"})