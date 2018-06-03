drop table if exists Users;
create table Users (
    id integer primary key autoincrement,
    name varchar(16) not null,
    password varchar(16) not null,
    access_key varchar(32) not null
);

drop table if exists Statuses;
create table Statuses (
    user_id integer primary key,
    name varchar(16) not null,
    obesity integer not null,
    serious integer not null,
    hot integer not null,
    strong integer not null,
    kind integer not null,
    foreign key (user_id)
        references Users(id)
);

