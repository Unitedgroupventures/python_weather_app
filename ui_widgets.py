from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class WeatherUI(QWidget):
    def __init__(self):
        super().__init__()

        self.city_label = QLabel("Enter A City Name: ", self)
        self.city_label.setObjectName("city_label")

        self.city_input = QLineEdit(self)
        self.city_input.setObjectName("city_input")

        self.get_weather_button = QPushButton("Get Weather", self)
        self.get_weather_button.setObjectName("get_weather_button")

        self.temperature_label = QLabel(self)
        self.temperature_label.setObjectName("temperature_label")

        self.emoji_label = QLabel(self)
        self.emoji_label.setObjectName("emoji_label")
        # Explicitly set emoji font for clarity
        self.emoji_label.setFont(QFont("Apple Color Emoji"))
        self.emoji_label.setMinimumSize(100, 120)

        self.description_label = QLabel(self)
        self.description_label.setObjectName("description_label")

        self.setup_temperature_label()

        self.setup_ui()

    def setup_ui(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignHCenter)
        self.city_input.setAlignment(Qt.AlignHCenter)
        self.temperature_label.setAlignment(Qt.AlignHCenter)
        self.emoji_label.setAlignment(Qt.AlignHCenter)
        self.description_label.setAlignment(Qt.AlignHCenter)

    def setup_temperature_label(self):
        # In your UI class, after creating the temperature_label widget:
        self.temperature_label.setWordWrap(True)  # Enable multi-line wrap
        self.temperature_label.setMaximumWidth(400)  # Limit max width in pixels
        self.temperature_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)  # Fix vertical size
        self.temperature_label.setMaximumHeight(150)  # Optional, limit height


    def apply_styles(self):
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: Arial;          
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
                padding: 10px;
                min-height: 50px;
            }
            QPushButton#get_weather_button{
                font-size: 20px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: 'Apple Color Emoji';
            }
        """)
