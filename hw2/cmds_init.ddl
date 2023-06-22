CREATE TABLE if not exists events (
    id int generated always as identity primary key,
	event TEXT,
	date_s date,
	description TEXT,
	location TEXT
);

insert INTO events (event, date_s, description, location)
values ('Chess club', '04.01.2024', 'For chess lovers', 'Lyceum'),
     ('Table tennis', '04.02.2024', 'Playing table tennis', 'Arena'),
     ('Football club', '04.03.2024', 'For football fans', 'Arena'),
     ('Beading Circle', '04.04.2024', 'Weave Beaded Bracelets', 'Sigma Sirius'),
     ('Cooking together', '04.05.2024', 'Learning to cook pizza', 'Sigma Sirius'),
     ('Basketball', '04.06.2024', 'For basketball lovers', 'Lyceum');

CREATE TABLE IF NOT EXISTS token (
    username text NOT NULL primary key,
    token uuid);
    
INSERT INTO token (username, token) VALUES ('admin', '73f8c463-ff76-4f95-bba9-5a07284d5059');
