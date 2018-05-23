drop table if exists statuses;
create table statuses {
    id integer primary key autoincrement,
    name varchar(16) not null
}
