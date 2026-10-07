from dataclasses import dataclass
import flet as ft

@dataclass(frozen=True)
class FoodItem:
    name: str
    calories_per_100g: float

    @property
    def calories_per_gram(self) -> float:
        return self.calories_per_100g / 100.0

    def calculate_serving(self, weight_grams: float) -> float:
        if weight_grams <= 0:
            raise ValueError("Serving weight must be greater than zero.")
        return self.calories_per_gram * weight_grams

def main(page: ft.Page):
    page.title = "KcalCore"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 420
    page.window.height = 700
    page.window.resizable = False

    # Aesthetic Design Tokens
    BG_TOP = "#090D16"
    BG_BOTTOM = "#020408"
    SURFACE = "#111827"
    BORDER_DEFAULT = "#1E293B"
    BORDER_FOCUS = "#6366F1"
    ACCENT_INDIGO = "#6366F1"
    SUCCESS_MINT = "#34D399"
    TEXT_MAIN = "#F8FAFC"
    TEXT_MUTED = "#94A3B8"
    ERROR_RED = "#F87171"

    field_border = {
        ft.ControlState.DEFAULT: ft.OutlineInputBorder(
            border_radius=14,
            side=ft.BorderSide(1, BORDER_DEFAULT)
        ),
        ft.ControlState.FOCUSED: ft.OutlineInputBorder(
            border_radius=14,
            side=ft.BorderSide(1.5, BORDER_FOCUS)
        )
    }

    food_name_input = ft.TextField(
        label="Food Name (Optional)",
        border=field_border,
        bgcolor=SURFACE,
        color=TEXT_MAIN,
        label_style=ft.TextStyle(color=TEXT_MUTED),
        prefix_icon=ft.Icons.FASTFOOD_ROUNDED
    )
    
    calories_input = ft.TextField(
        label="Calories per 100g",
        keyboard_type=ft.KeyboardType.NUMBER,
        border=field_border,
        bgcolor=SURFACE,
        color=TEXT_MAIN,
        label_style=ft.TextStyle(color=TEXT_MUTED),
        prefix_icon=ft.Icons.LOCAL_FIRE_DEPARTMENT_ROUNDED
    )
    
    weight_input = ft.TextField(
        label="Serving Weight (g)",
        keyboard_type=ft.KeyboardType.NUMBER,
        border=field_border,
        bgcolor=SURFACE,
        color=TEXT_MAIN,
        label_style=ft.TextStyle(color=TEXT_MUTED),
        prefix_icon=ft.Icons.SCALE_ROUNDED
    )
    
    item_title_text = ft.Text(value="", size=18, weight=ft.FontWeight.BOLD, color=TEXT_MAIN)
    rate_text = ft.Text(value="", size=13, color=TEXT_MUTED)
    total_text = ft.Text(value="", size=22, weight=ft.FontWeight.W_800, color=SUCCESS_MINT)

    empty_placeholder = ft.Container(height=0)

    result_card_content = ft.Container(
        bgcolor=SURFACE,
        border_radius=18,
        border=ft.Border.all(1.5, SUCCESS_MINT),
        padding=22,
        animate=ft.Animation(400, ft.AnimationCurve.EASE_OUT_BACK),
        shadow=ft.BoxShadow(spread_radius=2, blur_radius=25, color="#10B98126"),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Row([
                            ft.Icon(ft.Icons.AUTO_AWESOME, color=SUCCESS_MINT, size=16),
                            ft.Text("RESULT SUMMARY", weight=ft.FontWeight.BOLD, size=11, color=SUCCESS_MINT),
                        ], spacing=6),
                        ft.Icon(ft.Icons.CHECK_CIRCLE_ROUNDED, color=SUCCESS_MINT, size=18)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Divider(color=BORDER_DEFAULT, height=20),
                item_title_text,
                rate_text,
                ft.Container(height=4),
                total_text,
            ],
            spacing=6
        )
    )

    results_switcher = ft.AnimatedSwitcher(
        content=empty_placeholder,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=450,
        reverse_duration=250,
        switch_in_curve=ft.AnimationCurve.EASE_OUT_BACK,
        switch_out_curve=ft.AnimationCurve.EASE_IN_CUBIC
    )

    error_text = ft.Text(value="", color=ERROR_RED, weight=ft.FontWeight.W_600, size=13)

    def calculate_clicked(e):
        error_text.value = ""
        
        try:
            if not calories_input.value or not weight_input.value:
                error_text.value = "Please fill in the required fields."
                page.update()
                return

            # Validate food name if provided (ensure it's not purely a number)
            raw_name = food_name_input.value.strip()
            if raw_name:
                try:
                    float(raw_name)
                    error_text.value = "Food name cannot be a pure number."
                    page.update()
                    return
                except ValueError:
                    pass

            c_100g = float(calories_input.value)
            weight = float(weight_input.value)

            if c_100g < 0 or weight <= 0:
                error_text.value = "Values must be greater than zero."
                page.update()
                return

            name = raw_name or "Custom Item"
            
            item = FoodItem(name=name, calories_per_100g=c_100g)
            total_kcal = item.calculate_serving(weight_grams=weight)

            item_title_text.value = f"{name.upper()}"
            rate_text.value = f"Density: {item.calories_per_gram:.4f} kcal / gram"
            total_text.value = f"{total_kcal:,.2f} kcal"
            
            results_switcher.content = result_card_content
            page.update()

        except ValueError as ex:
            error_text.value = str(ex) if "weight" in str(ex).lower() else "Please enter valid numbers."
            page.update()

    def clear_clicked(e):
        food_name_input.value = ""
        calories_input.value = ""
        weight_input.value = ""
        error_text.value = ""
        results_switcher.content = empty_placeholder
        page.update()

    calc_button = ft.Container(
        content=ft.Text("Calculate Calories", color=TEXT_MAIN, weight=ft.FontWeight.W_600, size=14),
        bgcolor=ACCENT_INDIGO,
        padding=ft.Padding.symmetric(horizontal=24, vertical=14),
        border_radius=14,
        alignment=ft.Alignment.CENTER,
        ink=True,
        on_click=calculate_clicked,
        shadow=ft.BoxShadow(spread_radius=0, blur_radius=12, color="#6366F166"),
        animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT)
    )
    
    clear_button = ft.TextButton(
        content=ft.Text("Clear", color=TEXT_MUTED, weight=ft.FontWeight.W_500),
        on_click=clear_clicked
    )

    scrollable_content = ft.Column(
        [
            ft.Container(height=10),
            ft.Column([
                ft.Text("KcalCore", size=30, weight=ft.FontWeight.W_900, color=TEXT_MAIN),
                ft.Text("Precision macro & calorie tracking engine", size=13, color="#818CF8"),
            ], spacing=2),
            ft.Divider(height=20, color=BORDER_DEFAULT),
            food_name_input,
            calories_input,
            weight_input,
            ft.Container(height=5),
            ft.Row([calc_button, clear_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER),
            error_text,
            results_switcher,
            ft.Container(height=10),
            ft.Column(
                [
                    ft.Text("Developer: Mohib Ashfaq", size=11, color="#475569", italic=True),
                    ft.Row(
                        [
                            ft.TextButton(
                                "GitHub",
                                action=ft.OpenUrl("https://github.com/mohib-ash"),
                            ),
                            ft.Text("•", color="#334155", size=10),
                            ft.TextButton(
                                "LinkedIn",
                                action=ft.OpenUrl("https://www.linkedin.com/in/mohib-ashfaq-4a682b407/"),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=0
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0
            ),
            ft.Container(height=10)
        ],
        spacing=16,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        scroll=ft.ScrollMode.AUTO
    )

    page.add(
        ft.Container(
            content=scrollable_content,
            padding=28,
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_CENTER,
                end=ft.Alignment.BOTTOM_CENTER,
                colors=[BG_TOP, BG_BOTTOM]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main)