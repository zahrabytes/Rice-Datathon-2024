from taipy.gui import Gui
from math import cos, exp

content = ""
img_path = "placeholder_image.png"
prob = 0
pred = ""
chevron_path = r"Chevron_Logo.svg.png"
plots = r"plots.png"
graph1 = r"graph1.png"
graph2 = r"graph2.png"
page = """
Markdown
<|text-center|
# Rice Datathon *2024* 

<|{chevron_path}|image|>
>
<|{content}|file_selector|extensions=.csv|>
Select a CSV file from your file system.

### Prediction
<|{pred}|text|>
Prediction Probability: <|{prob}|text|>

"""

def compute_data(decay: int) -> list:
    return [cos(i/6) * exp(-i*decay/600) for i in range(100)]

value = 0
data = compute_data(value)

def slider_changed(state):
    state.data = compute_data(state.value)

Gui(page).run(use_reloader=True, port=5001)

