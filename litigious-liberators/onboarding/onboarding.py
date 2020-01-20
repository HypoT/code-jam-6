from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation

lorem = ""
sentences = [
    "Dino Tinder is a Tinder Clone adapted\n for the middle ages.",
    "my",
    "friends",
]
images = [
    "https://placekitten.com/g/1080/1920",
    "https://placekitten.com/g/200/300",
    "https://placekitten.com/g/300/400",
]


class MyOnboardWidget(FloatLayout):
    steps = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for index, image_url in enumerate(images):
            image_object = AsyncImage(source=image_url, size_hint=(1, 1))
            image_object.opacity = 1 if index == 0 else 0
            setattr(self, f"image_{index}", image_object)
            self.add_widget(image_object)

        for index, sentence in enumerate(sentences):
            label_object = Label(
                text=lorem,
                pos_hint={"center_x": 0.50, "center_y": 0.2},
                color=[1, 0, 0, 1],
                halign="left",
                valign="middle",
                font_size="15sp",
                text_size=(400, 600),
            )
            label_object.opacity = 1 if index == 0 else 0
            setattr(self, f"description_{index}", label_object)
            self.add_widget(label_object)

        self.add_widget(
            Label(
                text="Welcome to DinoTinder",
                pos_hint={"center_x": 0.40, "center_y": 0.3},
                color=[1, 0, 0, 1],
                halign="left",
                valign="middle",
                font_size="25sp",
            )
        )

    def animate(self, obj_out, obj_in):
        appear = Animation(opacity=1, duration=1)
        disappear = Animation(opacity=0, duration=1)
        appear.start(obj_in)
        disappear.start(obj_out)

    def on_touch_down(self, touch):
        if self.steps == 0:
            self.animate(obj_out=self.image_0, obj_in=self.image_1)
            self.animate(obj_out=self.description_0, obj_in=self.description_1)
        if self.steps == 1:
            self.animate(obj_out=self.image_1, obj_in=self.image_2)
            self.animate(obj_out=self.description_1, obj_in=self.description_2)

        self.steps += 1

        return True


class OnboardingScreen(Screen):
    pass


class OnboardingApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(OnboardingScreen(name="onboarding"))
        return sm


if __name__ == "__main__":
    OnboardingApp().run()


# def ola():
#     print("HELLLOOO")
#
#
# class CarouselApp(App):
#     def build(self):
#        #  carousel = Carousel(direction="right", loop=True)
#        #  src = "https://placekitten.com/g/1080/1920"
#        #  src_1 = "https://placekitten.com/g/1080/1920"
#        #  image = AsyncImage(source=src)
#        #  image1 = AsyncImage(source=src_1)
#        #  carousel.add_widget(image)
#        #  carousel.add_widget(image1)
#        #  return carousel
#
#
# CarouselApp().run()
