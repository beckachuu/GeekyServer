
-- -----------------------------------------------------
-- Schema w22g7_geek
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `w22g7_geek` ;

-- -----------------------------------------------------
-- Schema w22g7_geek
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `w22g7_geek` DEFAULT CHARACTER SET utf8 ;
USE `w22g7_geek` ;

-- -----------------------------------------------------
-- Table `authors`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `authors` ;

CREATE TABLE IF NOT EXISTS `authors` (
  `author_id` INT NOT NULL AUTO_INCREMENT,
  `author_name` VARCHAR(70) NOT NULL,
  `profile_pic` TEXT NULL,
  `bio` TEXT NULL DEFAULT NULL,
  `social_account` TEXT NULL DEFAULT NULL,
  `website` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`author_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `authorsQuotes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `authorsQuotes` ;

CREATE TABLE IF NOT EXISTS `authorsQuotes` (
  `quote_id` INT NOT NULL AUTO_INCREMENT,
  `author_id` INT NOT NULL,
  `quote` TEXT NOT NULL,
  PRIMARY KEY (`quote_id`, `author_id`),
  CONSTRAINT `fk_authors_quotes_authors`
    FOREIGN KEY (`author_id`)
    REFERENCES `authors` (`author_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `states`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `states` ;

CREATE TABLE IF NOT EXISTS `states` (
  `state` VARCHAR(100) NOT NULL,
  `created_date` DATETIME NULL,
  PRIMARY KEY (`state`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `users` ;

CREATE TABLE IF NOT EXISTS `users` (
  `username` VARCHAR(20) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `name` VARCHAR(70) NULL,
  `phone` VARCHAR(10) NULL,
  `profile_pic` TEXT NULL,
  `theme_preference` INT UNSIGNED NOT NULL DEFAULT 1,
  `user_role` INT UNSIGNED NOT NULL DEFAULT 0,
  `login_state` VARCHAR(100) NULL,
  `recieve_email` INT NOT NULL DEFAULT 1,
  `restrict_due` DATETIME NULL,
  PRIMARY KEY (`username`),
  CONSTRAINT `fk_users_states1`
    FOREIGN KEY (`login_state`)
    REFERENCES `states` (`state`)
    ON DELETE SET NULL
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `books`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books` ;

CREATE TABLE IF NOT EXISTS `books` (
  `book_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(70) NOT NULL,
  `translator` VARCHAR(70) NULL,
  `cover` TEXT NULL,
  `page_count` INT NOT NULL,
  `public_year` INT NOT NULL,
  `content` TEXT NOT NULL,
  `descript` TEXT NOT NULL,
  `republish_count` INT NULL,
  `current_rating` FLOAT NULL,
  PRIMARY KEY (`book_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bookmark`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `bookmark` ;

CREATE TABLE IF NOT EXISTS `bookmark` (
  `username` VARCHAR(20) NOT NULL,
  `book_id` INT NOT NULL,
  `bm_name` VARCHAR(20) NOT NULL,
  `line_position` INT NULL,
  `content` TEXT NULL,
  PRIMARY KEY (`username`, `book_id`, `bm_name`),
  CONSTRAINT `fk_bookmark_users1`
    FOREIGN KEY (`username`)
    REFERENCES `users` (`username`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_bookmark_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `books` (`book_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books_authors`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books_authors` ;

CREATE TABLE IF NOT EXISTS `books_authors` (
  `author_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  PRIMARY KEY (`author_id`, `book_id`),
  CONSTRAINT `fk_books_has_authors_authors1`
    FOREIGN KEY (`author_id`)
    REFERENCES `authors` (`author_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_books_has_authors_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `books` (`book_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `collections`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collections` ;

CREATE TABLE IF NOT EXISTS `collections` (
  `username` VARCHAR(20) NOT NULL,
  `coll_name` VARCHAR(50) NOT NULL,
  `book_id` INT NOT NULL,
  PRIMARY KEY (`username`, `coll_name`, `book_id`),
  CONSTRAINT `fk_collections_users1`
    FOREIGN KEY (`username`)
    REFERENCES `users` (`username`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_collections_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `books` (`book_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `notifications`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `notifications` ;

CREATE TABLE IF NOT EXISTS `notifications` (
  `noti_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(20) NOT NULL,
  `noti_date` DATETIME NOT NULL,
  `noti_text` TEXT NOT NULL,
  `trigger_source` TEXT NOT NULL,
  PRIMARY KEY (`noti_id`, `username`),
  CONSTRAINT `fk_notifications_users1`
    FOREIGN KEY (`username`)
    REFERENCES `users` (`username`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ratings`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ratings` ;

CREATE TABLE IF NOT EXISTS `ratings` (
  `username` VARCHAR(20) NOT NULL,
  `book_id` INT NOT NULL,
  `stars` INT NOT NULL,
  `content` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`username`, `book_id`),
  CONSTRAINT `fk_ratings_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `books` (`book_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_ratings_users1`
    FOREIGN KEY (`username`)
    REFERENCES `users` (`username`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `subscription`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `subscription` ;

CREATE TABLE IF NOT EXISTS `subscription` (
  `author_id` INT NOT NULL,
  `username` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`author_id`, `username`),
  CONSTRAINT `fk_subscription_authors1`
    FOREIGN KEY (`author_id`)
    REFERENCES `authors` (`author_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_subscription_users1`
    FOREIGN KEY (`username`)
    REFERENCES `users` (`username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `genres`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `genres` ;

CREATE TABLE IF NOT EXISTS `genres` (
  `genre` VARCHAR(40) NOT NULL,
  `book_id` INT NOT NULL,
  PRIMARY KEY (`genre`, `book_id`),
  CONSTRAINT `fk_genres_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `books` (`book_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



-- -----------------------------------------------------
-- Data for table `users`
-- -----------------------------------------------------
START TRANSACTION;
USE `w22g7_geek`;
INSERT INTO `users` (`username`, `email`, `name`, `phone`, `profile_pic`, `theme_preference`, `user_role`, `login_state`, `recieve_email`, `restrict_due`) VALUES ('20020267', '20020267@vnu.edu.vn', NULL, NULL, 'https://lh3.googleusercontent.com/a/ALm5wu1chSwRUTx6ehK-w-C0Gd3XRufkMLBW_Bzq70Ab=s96-c', 1, 0, NULL, 1, NULL);
INSERT INTO `users` (`username`, `email`, `name`, `phone`, `profile_pic`, `theme_preference`, `user_role`, `login_state`, `recieve_email`, `restrict_due`) VALUES ('beckachu', 'trangmahomies@gmail.com', NULL, NULL, 'https://lh3.googleusercontent.com/a/ALm5wu0CB5cg3CJwugdcMrUB0DIwYDNtAB1h_Am6KZv6dQ=s96-c', 1, 0, NULL, 1, NULL);

COMMIT;

