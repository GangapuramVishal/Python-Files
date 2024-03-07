from win10toast import ToastNotifier
toast = ToastNotifier()
toast.show_toast(
    "Drink water",
    "Hey it's time to drink water!!",
    duration = 20,
    icon_path = "icon.ico",
    threaded = True,
)