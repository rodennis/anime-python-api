BEGIN;

CREATE TABLE facts (
    fact_id text,
    fact text
);

COPY facts (show_name, fact) FROM stdin;
naruto Zabuzas name means never cut twice
naruto Sakura was supposed to die in episdoe 26
naruto Choujis dad was part of the group that wanted to kill Naruto in Chapter 1.
naruto Narutos favorite ramen shop Ichiraku exists in real life.
naruto Shikamarus IQ is above 200.
naruto Kakuzus techniques are named after the series Mobile Suit Gundam.
naruto Nejis forehead marks are different in the anime and manga.
naruto The tallest shinobi in Hidden Leaf is Ibiki Morino
naruto Sanji from One Piece was supposed to be named Naruto.
naruto Canonically, Naruto s RasenShuriken is a reddish-orange color.
naruto Naruto and Kurama s Bijuu Bomb is not the same color as the other bijuus.
naruto Sarutobi was supposed to be a monkey, but the creator of Naruto changed his mind and make him human like other Shinobis. Maybe that is why lord third was able to summon Enma.
\.

COMMIT;