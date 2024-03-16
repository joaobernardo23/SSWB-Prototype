"""Frontend code for the SSWB prototype."""

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QDialog
from PyQt5.QtGui import QIcon


class MyMainWindow(QMainWindow):
    """Creates the main GUI.

    This class creates the graphical user interface that aims to control
    the prototype's compactor function.
    """

    def __init__(self):
        super().__init__()

        # Create a toolbar for the day/dark mode toggle and for
        # the control buttons.
        toolbar_mode = self.create_toolbar("Toolbar")
        toolbar_control = self.create_toolbar("Toolbar1")

        # Create start button
        self.start = QPushButton('Start')
        self.start.setIcon(QIcon("images/Start-icon.png"))
        self.start.clicked.connect(self.start_clicked)
        toolbar_control.addWidget(self.start)

        # Create a dark/light mode toggle button
        self.day_icon = QIcon("images/day_mode.png")
        self.night_icon = QIcon("images/dark_mode.png")
        self.choose_color_action = QPushButton(self)
        self.choose_color_action.setGeometry(150, 100, 100, 50)
        self.choose_color_action.setIcon(self.day_icon)
        self.choose_color_action.setIconSize(self.choose_color_action.size())
        self.choose_color_action.setFlat(True)
        self.choose_color_action.setStyleSheet("border: none;")
        self.choose_color_action.clicked.connect(self.toggle_light)
        toolbar_mode.addWidget(self.choose_color_action)

        # Create a button to pull back the compactor
        self.pullback = QPushButton('Retrieve')
        self.pullback.setIcon(QIcon("images/retrieve_icon.png"))
        self.pullback.clicked.connect(self.retrieve)
        toolbar_control.addWidget(self.pullback)

        # Create exit button
        self.exit = QPushButton('Exit')
        self.exit.clicked.connect(self.show_popup)
        toolbar_control.addWidget(self.exit)

        # Set the default background color
        self.setStyleSheet("background-color: white;")

    def create_toolbar(self, name):
        """Creates a toolbar with a specific name.
        
        Args:
            name (str): Name of the toolbar.
            
        Returns:
            Toolbar object.
        """

        return self.addToolBar(name)

    def toggle_light(self):
        """Toggles to light mode."""

        self.choose_color_action.setIcon(self.night_icon)
        self.setStyleSheet("background-color: rgb(54,57,62); color: white;")
        self.choose_color_action.clicked.disconnect()
        self.choose_color_action.clicked.connect(self.toggle_dark)

    def toggle_dark(self):
        """Toggles to dark mode."""

        self.choose_color_action.setIcon(self.day_icon)
        self.setStyleSheet("background-color: white; color: black;")
        self.choose_color_action.clicked.disconnect()
        self.choose_color_action.clicked.connect(self.toggle_light)

    def start_clicked(self):
        """Starts the compacting action.
        
        When the start button is pushed it toggles to the pause button.
        """
        self.start.setText('Pause')
        self.start.setIcon(QIcon("images/pauseicon.png"))
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.pause_clicked)
        print("5")

    def pause_clicked(self):
        """Pauses the compacting action.
        
        When the pause button is pushed it toggles to the start button.
        """
        self.start.setText('Start')
        self.start.setIcon(QIcon("images/Start-icon.png"))
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.start_clicked)
        print("8")

    def retrieve(self):
        """Pulls back the compactor until the starting position."""
        print("10")

    def show_popup(self):
        """Pop-up to verify if the exit button was pressed on purpose."""
        dialog = QDialog()
        dialog.setWindowTitle("Warning")
        label = QLabel("Are you sure you want to exit?")
        yes_button = QPushButton("Yes")
        yes_button.setIcon(QIcon("images/yes.png"))
        yes_button.clicked.connect(app.quit)
        no_button = QPushButton("No")
        no_button.setIcon(QIcon("images/no.png"))
        no_button.clicked.connect(dialog.close)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(yes_button)
        layout.addWidget(no_button)
        dialog.setLayout(layout)
        dialog.exec_()


# Runs the program
app = QApplication([])
win = MyMainWindow()
win.show()
app.exec_()
