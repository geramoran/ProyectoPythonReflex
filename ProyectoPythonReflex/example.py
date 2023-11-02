import reflex as rx

def example(Contador) -> rx.Component:
	return rx.hstack(
		rx.button(
			"Incrementa",
			color_scheme="green",
			on_click=Contador.increment
		),
		rx.heading(Contador.count, font_size="2em", padding="0 20px"),
  		rx.button(
			"Disminuye",
			color_scheme="red",
   			on_click=Contador.decrement
		)
	)