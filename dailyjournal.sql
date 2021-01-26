CREATE TABLE `Mood` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL
);

CREATE TABLE `Tag` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `subject`    TEXT NOT NULL
);

CREATE TABLE `Entry` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`datetime`  TIMESTAMP NOT NULL,
	`content` TEXT NOT NULL,
	`tag` TEXT NOT NULL,
	`mood` INTEGER NOT NULL,
	FOREIGN KEY(`tag`) REFERENCES `Tag`(`id`),
	FOREIGN KEY(`mood`) REFERENCES `Mood`(`id`)
);


INSERT INTO 'Mood' VALUES (null, 'Excited');
INSERT INTO 'Mood' VALUES (null, 'Hopeful');
INSERT INTO 'Mood' VALUES (null, 'Confused');
INSERT INTO 'Mood' VALUES (null, 'Frustrated');
INSERT INTO 'Mood' VALUES (null, 'Anxious');
INSERT INTO 'Mood' VALUES (null, 'Despair');
INSERT INTO 'Mood' VALUES (null, 'Jubilation');
INSERT INTO 'Mood' VALUES (null, 'Proud');
INSERT INTO 'Mood' VALUES (null, 'Grateful');

INSERT INTO 'Entry' VALUES (null, '1579996800', 'keep calm and carry on', 1, 5)
INSERT INTO 'Entry' VALUES (null, '1579996800', 'We are making it!', 1, 1)
INSERT INTO 'Entry' VALUES (null, '1579996800', '...nevermind', 1, 6)

DROP TABLE Mood;
DROP TABLE Tag;
DROP TABLE Entry;