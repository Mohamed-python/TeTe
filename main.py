import flet as ft

def main(page: ft.Page):
    def on_view_click(e):
        print("تم الضغط على زر المشاهدة!")

    # إنشاء زر مع نص وأيقونة
    view_button = ft.ElevatedButton(
        text="مشاهدة",
        icon=ft.Icons.VISIBILITY,  # أيقونة العين
        on_hover=on_view_click    # الحدث عند الضغط
    )

    page.add(view_button)

ft.app(target=main)
