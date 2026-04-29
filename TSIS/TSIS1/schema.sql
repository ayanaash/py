--groups
CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,     --автоматически увеличивает id
    name VARCHAR(50) UNIQUE NOT NULL
);

--contacts
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,   --уникальный id контакта
    name VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100),
    birthday DATE,
    group_id INTEGER REFERENCES groups(id),  --внешний ключ - связь с группой
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   --дата добавления
);

--phones 
CREATE TABLE IF NOT EXISTS phones (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,  --если удалить контакт - удалятся его телефоны
    phone VARCHAR(20) NOT NULL,
    type VARCHAR(10) CHECK (type IN ('home','work','mobile'))
);