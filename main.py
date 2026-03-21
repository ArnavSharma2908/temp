from kivy.app import App
from kivy.uix.button import Button

# Android vibration support
try:
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Context = autoclass('android.content.Context')
except:
    PythonActivity = None


class MyApp(App):
    def build(self):
        btn = Button(text="Vibrate", font_size=40)
        btn.bind(on_press=self.vibrate_twice)
        return btn

    def vibrate_twice(self, instance):
        if PythonActivity:
            activity = PythonActivity.mActivity
            vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)

            # Vibrate twice (pattern: wait, vibrate, wait, vibrate)
            pattern = [0, 300, 200, 300]  # milliseconds
            vibrator.vibrate(pattern, -1)
        else:
            print("Not running on Android")


if __name__ == "__main__":
    MyApp().run()
