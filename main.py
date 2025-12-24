from gui.main_window import MainWindow
from system.shutdown import ShutdownController

def main():
    shutdown = ShutdownController()
    app = MainWindow(shutdown)
    app.run()

if __name__ == "__main__":
    main()
