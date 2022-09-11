create table if not exists public.users
(
    id int,
    name          varchar(256),
    first_name    varchar(256),
    last_name     varchar(256),
    bachelor_year varchar(256),
    magister_year varchar(256),
    country       varchar(256),
    city          varchar(256),
    company       varchar(256),
    position      varchar(256),
    linkedin      varchar(256),
    instagram     varchar(256),
    hobbies       varchar(256),
    primary key (id)
);