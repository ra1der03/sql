create table if not exists Genre ( 
id SERIAL primary key,
name VARCHAR(30) not null unique
);

create table if not exists Artist ( 
id SERIAL primary key,
name VARCHAR(30) not null unique
);

create table if not exists Album ( 
id SERIAL primary key,
name VARCHAR(30) not null unique,
year_release INTEGER not null
);

create table if not exists Track ( 
id SERIAL primary key,
name VARCHAR(30) not null,
album_id INTEGER references Album(id),
duration integer not null
);

create table if not exists Collection ( 
id SERIAL primary key,
name VARCHAR(30) not null,
year_release INTEGER NOT null check (year_release > 0)
);

create table if not exists ArtistGenre ( 
artist_id INTEGER,
genre_id INTEGER,
CONSTRAINT uk 
	FOREIGN KEY (artist_id) references artist(id) on update cascade on delete cascade,
CONSTRAINT up 
	foreign KEY (genre_id) references genre(id) on update cascade on delete cascade
);

create table if not exists TrackCollection ( 
track_id INTEGER,
collection_id INTEGER,
CONSTRAINT rk 
	foreign KEY (track_id ) references track(id) on update cascade on delete cascade,
CONSTRAINT pk 
	foreign KEY (collection_id) references collection(id) on update cascade on delete cascade
);

create table if not exists ArtistAlbum ( 
artist_id INTEGER,
album_id INTEGER,
CONSTRAINT pr 
	foreign KEY (artist_id) references artist(id)  on update cascade on delete cascade,
CONSTRAINT pt
	foreign KEY (album_id) references album(id) on update cascade on delete cascade
);



