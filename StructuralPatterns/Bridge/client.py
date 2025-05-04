from abstraction import Platform, WindowsUI, LinuxUI, MacUI
from implementation import DBConnectionPostgres, DBConnectionMySQL, DBConnectionMongoDB


def client(platform: Platform) -> None:
    print(platform.display())


if __name__ == "__main__":
    # Windows + PostgreSQL
    win = WindowsUI(DBConnectionPostgres())
    client(win)

    # Linux + MySQL
    linux = LinuxUI(DBConnectionMySQL())
    client(linux)

    # Mac + MongoDB
    mac = MacUI(DBConnectionMongoDB())
    client(mac)
