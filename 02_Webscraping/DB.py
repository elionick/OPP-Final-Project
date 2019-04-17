import pymysql
import pypyodbc


def wrongInsert():
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `movies_directors` (`director_id`, `movie_id`) VALUES (%s, %s)"
            cursor.execute(sql, [7, 10920])

        with connection.cursor() as cursor:
            sql = "INSERT INTO `directors` (`id`, `first_name`, `last_name`) VALUES (%s, %s, %s)"
            cursor.execute(sql, [8, "benji", "müller"])
    finally:
        cursor.close()


def genreInsert():
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `movies_directors` (`director_id`, `movie_id`) VALUES (%s, %s)"
            cursor.execute(sql, [1, 10920])
    finally:
        connection.commit()


def rightInsert():
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `directors` (`id`, `first_name`, `last_name`) VALUES (%s, %s, %s)"
            cursor.execute(sql, [9, "sebastian", "kuhn"])
        with connection.cursor() as cursor:
            sql = "INSERT INTO `movies_directors` (`director_id`, `movie_id`) VALUES (%s, %s)"
            cursor.execute(sql, [9, 10920])

    finally:
        connection.commit()


if __name__ == '__main__':
    import pypyodbc

    connection = pypyodbc.connect("Driver={SQL Server};"
                            "Server=OOP-2019.mssql.somee.com;"
                            "Database=OOP-2019;"
                            "uid=LEichhorn_SQLLogin_1;pwd=u18arbwshr")