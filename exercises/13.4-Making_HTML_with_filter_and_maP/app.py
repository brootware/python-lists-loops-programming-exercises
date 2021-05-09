all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def generate_li(x):
    x["label"] = "<li>" + x["label"] + "</li>"
    return x["label"]

def filter_colors(y):
    if y["sexy"] == True:
        return y

sexyColor = list(filter(filter_colors,all_colors))
sexyHTML = list(map(generate_li,sexyColor))

htmlString = ""
for i in sexyHTML:
    htmlString += i
    
# print(sexyColor)
print(htmlString)
