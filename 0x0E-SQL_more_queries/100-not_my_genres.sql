-- 100-not_my_genres list all genres not linked to the show Dexter.
SELECT DISTINCT tv_genres.name AS name
FROM tv_shows, tv_genres, tv_show_genres
WHERE tv_genres.name NOT IN(
      SELECT tv_genres.name
      FROM tv_shows, tv_genres, tv_show_genres
      WHERE tv_shows.title="Dexter"
      AND tv_shows.id=tv_show_genres.show_id
      AND tv_show_genres.genre_id=tv_genres.id
      ORDER BY tv_genres.name ASC
);
