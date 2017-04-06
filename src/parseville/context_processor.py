from parseville.models import UsefulLink


def init(request):
    greeting_text = "<h4>Resources that inspire us:</h4>"
    for link in UsefulLink.objects.filter(show=True):
        greeting_text += '<h5><a href="' + link.url + '" target="_blank">' + link.name + '</a> - ' + link.short_text + '</h5>'
    return {
        "caption": "IT life catalog",
        "greeting_caption": "Hello world!",
        "greeting_logo": "Logo will be here",
        "greeting_text": greeting_text
    }
