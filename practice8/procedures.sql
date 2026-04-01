-- 1 upsert (insert or update)
CREATE OR REPLACE PROCEDURE upsert_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_name) THEN   --есть ли
        UPDATE phonebook
        SET phone = p_phone
        WHERE first_name = p_name;    --обновляем
    ELSE
        INSERT INTO phonebook(first_name, phone)  --добпавляем
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


-- 2 вставка с проверкой
CREATE OR REPLACE PROCEDURE bulk_insert(names TEXT[], phones TEXT[])  --принимаем массивы
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1)
    LOOP
        IF phones[i] LIKE '87%' THEN   --begins w 87
            INSERT INTO phonebook(first_name, phone)
            VALUES (names[i], phones[i]);
        ELSE
            RAISE NOTICE 'Invalid phone: %', phones[i];   --выводим ошибку
        END IF;
    END LOOP;
END;
$$;


--3 deleting by name or phone
CREATE OR REPLACE PROCEDURE delete_user(p_value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = p_value OR phone = p_value;  
END;
$$;