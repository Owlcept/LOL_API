create table if not exists games(
    player text,
    champ text,
    lane text,
    vs text,
    kills int,
    deaths int,
    assists int,
    win int,
    matchid text
);
create table if not exists players(
    username text,
    wlr real
);