MOBILE_MAX_WIDTH = 640
import flet as ft
from components.mobile_view import MobileView
from components.web_view import WebView


def main(page: ft.Page):
    # page.width = 500 # Initial layout is "mobile"

    web_view = WebView()
    mobile_view = MobileView()

    def get_page_design():
        size = page.width
        print("Page size:", page.width, page.height)
        if (size != None) and (size > MOBILE_MAX_WIDTH):
            return "web"
        else:
            return "mobile"

    def switch_view():
        # the last view in the list will be shown on the page
        temp = page.views[1]
        page.views[1] = page.views[2]
        page.views[2] = temp
        page.update()

    # Initial layout
    page.design = get_page_design()
    page.views.append(mobile_view)
    page.views.append(web_view)
    if page.design == "mobile":
        switch_view()

    page.update()

    def page_resize(e):
        new_design = get_page_design()
        # check if if page layout needs to be changed
        if page.design != new_design:
            switch_view()
            page.design = new_design

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_resize = page_resize
    page.on_view_pop = view_pop  # triggered when clicking on "X" for New Message view

    def get_route_list(route):
        route_list = [item for item in route.split("/") if item != ""]
        return route_list

    def route_change(e):
        route_list = get_route_list(page.route)

        if len(route_list) == 0:
            page.go("/inbox")

    page.on_route_change = route_change
    print(f"Initial route: {page.route}")
    page.go(page.route)


ft.app(main)
