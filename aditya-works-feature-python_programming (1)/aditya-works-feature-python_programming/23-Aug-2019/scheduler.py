import webbrowser
google = input("Enter a text to search : ")
webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)