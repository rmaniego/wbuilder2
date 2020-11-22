"""
    wBuilder Tuts
    (c) 2020 Rodney Maniego Jr.
"""
from wbuilder2.wbuilder import WebBuilder


## tests
html = WebBuilder()

## head
html.at("head").title().text("WebBuilder").done()
html.at("head").meta().charset("UTF-8").done()
html.at("head").meta().name("viewport").content("width=device-width, initial-scale=1, shrink-to-fit=no").done()
## html.at("head").link().rel("icon").href("icon.png").Type("image/png").sizes("96x96").done(static=True)
## html.at("head").link().rel("stylesheet").href("reset.css").done(static=True)
html.at("head").link().rel("stylesheet").href("design.css").done()


## no css
html.at("body").div("prompt-msg", "popup").done()

## css as string
html.at("#prompt-msg").div(Class="header").text("Welcome!").css(".header", "font-size: 14px; font-weight: bold; color: #333;").done()

## css as dictionary
design = { "font-size": "12px",
           "color": "#222",
           "background-color": "#f0f0f0" }
html.at("#prompt-msg").div(Class="message").text("Lorem ipsum...").css(".message", design).done()
print(html.build())

## save to file
html.save_to_html("gen", "")
html.save_stylesheet("gen", "")