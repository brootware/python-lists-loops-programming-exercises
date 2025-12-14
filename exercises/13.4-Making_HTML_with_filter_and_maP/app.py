all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here

def generate_li(color:dict) -> str:
    return f"<li>{color['label']}</li>"

def filter_colors(color:dict) -> str:
    if color['sexy'] == True:
        return color['label']

filtered_colors = list(filter(filter_colors, all_colors))
resulting_html = list(map(generate_li,filtered_colors))
print(resulting_html)