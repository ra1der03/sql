select name,duration from track
where duration=(select max(duration) from track);

select name from track
where duration>209;

select name from collection
where year_release BETWEEN 2018 AND 2020;

select name from artist
where name not LIKE '% %';

select name from track
where upper(name) like 'МОЙ%' or upper(name) like 'MY%';

select genre_id, count(artist_id) from artistgenre
group by genre_id;

select count(*) from track 
where album_id = (select id from album 
where year_release between 2018 and 2020);

select a.name, avg(t.duration) from album as a
left join track as t on t.album_id = a.id
group by a.name 
order by avg(t.duration);

--2019 год вместо 2020, важен лишь факт выполнения задачи сортировки
select ar.name, al.year_release from artist as ar
left join album as al on al.id = ar.id
where al.year_release != 2019
order by al.year_release;

select a.name, c.name from collection as c
left join trackcollection as tc on tc.collection_id = c.id 
left join track as t on t.id = tc.track_id
left join album as al on al.id = t.album_id 
left join artistalbum as aa on aa.album_id = t.album_id 
left join artist as a on a.id = aa.artist_id 
where a.name = 'Harry Styles'
limit 1




