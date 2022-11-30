-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_genres.name = "Comedy" AND tv_show_genres.genre_id = tv_genres.id AND tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC;