

INSERT INTO genre (name) 
VALUES ('rock'),('pop'),('jazz'),('chanson');

INSERT INTO artist (name) 
VALUES ('All american rejects'),('Harry Styles'),('Луи Армстронг'),('Лепс');

INSERT INTO album (name, year_release) 
VALUES ('Move Along', 2005),('Fine Line', 2019),('Our Monday Date', 1947),('Парус', 2004);

INSERT INTO track  (name, album_id, duration) 
VALUES ('Move Along', 1, 238),('Watermelon', 2, 195),('Bye and Bye', 3, 156),('Мой цыган', 4, 354);

INSERT INTO track  (name, album_id, duration) 
VALUES ('It ends tonight', 1, 245),('Falling', 2, 240),('Dallas blues', 3, 194),('Рюмка водки', 4, 246);

INSERT INTO collection  (name, year_release) 
VALUES ('Move', 2014),('Harry sugar', 2020),('Bye', 2010),('Цыган Гриша', 2013);

INSERT INTO trackcollection  (track_id, collection_id) 
VALUES (1,1),(2,2),(3,3),(4,4),(5,1),(6,2),(7,3),(8,4);

INSERT INTO artistgenre (artist_id, genre_id) 
VALUES (1,1),(2,2),(3,3),(4,4);

INSERT INTO artistalbum (artist_id, album_id) 
VALUES (1,1),(2,2),(3,3),(4,4);