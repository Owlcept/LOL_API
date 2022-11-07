create table if not exists games(
    player text,
    champ text,
    role text,
    vs text,
    kills int,
    deaths int,
    assists int,
    gold int,
    cs int,
    champdmg int,
    win int,
);
create table if not exists players(
    username text,
    wlr real,
)