--1 search by sample (шаблон)
CREATE OR REPLACE FUNCTION search_pattern(pattern TEXT)  --создаем функ, если уже есть перезаписываем; патт текст: что именно ищем
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR)    --возвращаем таблицу с этими строками
AS $$   --начало функ
BEGIN
    RETURN QUERY   --возвр результат sql запроса
    SELECT * FROM phonebook   --берем все записи из табл
    WHERE first_name ILIKE '%' || pattern || '%'   --поиск по имени; % = любой текст; || = склеивание строк
       OR phone LIKE pattern || '%';   --поиск по тел, начинается с патт
END;
$$ LANGUAGE plpgsql;


--2 pagination
CREATE OR REPLACE FUNCTION get_contacts(limit_val INT, offset_val INT)  --параметры (сколько показать, с какого места)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    LIMIT limit_val OFFSET offset_val;    -- limit = сколько строк; offset = пропустиь
END;
$$ LANGUAGE plpgsql;