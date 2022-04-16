import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.title('San Juan Swell Forecast')
    plt.xlabel("Dates")
    plt.ylabel("Swell Height (ft.)")
    plt.plot(x, y, marker='.')
    plt.ylim([0, 10])
    plt.tight_layout()
    graph = get_graph()
    return graph