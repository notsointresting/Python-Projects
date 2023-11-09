import webbrowser as wb

def webauto():
    chrome_path = "C://Program Files//Google//Chrome//Application//chrome.exe %s"
    URLs = {
        'stackoverflow.com',
        'github.com/notsointresting',
        'google.com',
        'youtube.com'
    }

    for url in URLs:
        print("Opening---> "+ url)
        wb.get(chrome_path).open(url)

webauto()
