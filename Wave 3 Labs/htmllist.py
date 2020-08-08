items = ['first string', 'second string']
html_str = "<ul>\n"
for i in items:
    html_str += "<li>" + i + "</li>\n"
html_str += "</ul>"
print(html_str)