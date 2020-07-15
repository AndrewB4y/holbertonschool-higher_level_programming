-- 15-comedy_only lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title AS title
FROM tv_shows, tv_show_genres, tv_genres
WHERE tv_genres.name="Comedy"
AND tv_genres.id=tv_show_genres.genre_id
AND tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title;
