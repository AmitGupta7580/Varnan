__app_name__ = "varnan"
__version__ = "0.0.2"

(SUCCESS, DIR_ERROR, FILE_ERROR, DB_READ_ERROR, DB_WRITE_ERROR, JSON_ERROR) = range(6)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
}
