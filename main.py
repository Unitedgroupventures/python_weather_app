import sys
from PyQt5.QtWidgets import QApplication
from ui_widgets import WeatherUI
from weather_api import fetch_weather
from helpers import get_weather_emoji


class WeatherApp(WeatherUI):
    def __init__(self):
        super().__init__()
        self.api_key = "NEED_TO_REQUEST_API_KEYS"
        self.get_weather_button.clicked.connect(self.get_weather)
        self.apply_styles()

    def get_weather(self):
        city = self.city_input.text()
        try:
            data = fetch_weather(city, self.api_key)
            if data.get("cod") == 200:
                self.display_weather(data)
            else:
                self.display_error(data.get("message", "An error occurred"))
        except Exception as e:
            self.display_error(str(e))

    def display_weather(self, data):
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]

        self.temperature_label.setText(f"{temperature_c:.1f} ºC")
        self.description_label.setText(description)
        self.emoji_label.setText(get_weather_emoji(weather_id))

    # def display_error(self, message):
    #     self.temperature_label.setText(message)
    #     self.emoji_label.clear()
    #     self.description_label.clear()

    def display_error(self, message):
        self.temperature_label.setText(message)
        self.temperature_label.setStyleSheet(
            "font-size: 15px;"
        )  # smaller font for errors
        self.emoji_label.clear()
        self.description_label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
