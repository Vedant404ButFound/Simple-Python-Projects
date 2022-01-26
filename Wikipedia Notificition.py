import wikipedia,time
from plyer import notification
searchName = input('Enter A Valid Name : ')
search = wikipedia.search(searchName)
info = wikipedia.summary(search[0])
notification.notify(
    title=f'About {searchName}',
    message=info[:256],
    timeout=10,
    app_icon='C:/Users/MUDRA/Downloads/2.ico',
    app_name='VS Code'
)