create table utilisateur (
    id_utilisateur text primary key not null,
    email text unique not null
);

create table liste (
    id_liste int not null primary key,
    nom text not null,
    id_utilisateur text,
    foreign key (id_utilisateur) references utilisateur
);

create table contient(
    id_utilisateur text not null ,
    id_liste int not null,
    primary key (id_utilisateur,id_liste),
    foreign key (id_utilisateur) references utilisateur,
    foreign key (id_liste) references liste
);

create table message(
    id_message int primary key not null ,
    heureMsg timestamp not null,
    texteMsg text not null,
    id_utilisateur text not null,
    foreign key (id_utilisateur) references utilisateur
);

create table destinataire(
    id_liste int not null,
    id_message int not null ,
    primary key (id_liste,id_message),
    foreign key (id_liste) references liste,
    foreign key (id_message) references  message
);

insert into utilisateur
values
('samuel','samuel20@)gmail.com'),
('leilla','leilla@gmail.com');

insert into liste
values
(1,'samuel','famille'),
(2,'leilla','amis');

insert into contient
values
('leilla',2),
('samuel',1);

insert into message
values
(3,'2026-11-26 12:02:56','salut samuel','leilla'),
(4,'2026-11-26 12:02:56','salue leilla','samuel');

insert into destinataire
values
(2,3),
(1,4);


alter table liste add column nom text not null ;

select  * from utilisateur






