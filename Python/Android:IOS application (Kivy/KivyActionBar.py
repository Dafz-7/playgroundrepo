from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious, ActionButton, ActionGroup
from kivy.uix.label import Label

class ActionBarApp(App):
    def build(self):
        #* Main layout for the app
        layout = BoxLayout(orientation = "vertical")

        #* Making the action bar
        action_bar = ActionBar(size_hint = (1, 0.1))

        #* Making the action view
        action_view = ActionView()

        #* Button to navigate to the previous action
        action_previous = ActionPrevious(title = "My App", with_previous = False)

        #* Adding the button to the action view
        action_view.add_widget(action_previous)

        #* Adding several buttons to the action bar
        action_view.add_widget(ActionButton(text = "Home", on_press = self.on_home))
        action_view.add_widget(ActionButton(text = "Settings", on_press = self.on_settings))

        #* Adding action group for additional buttons
        more_actions = ActionGroup(text = "More", mode = "spinner")
        more_actions.add_widget(ActionButton(text = "About", on_press = self.on_about))
        more_actions.add_widget(ActionButton(text = "Help", on_press = self.on_help))

        #* Adding the action group to action view
        action_view.add_widget(more_actions)

        #* Adding the action view ot action bar
        action_bar.add_widget(action_view)

        #* Adding action bar to the main layout
        layout.add_widget(action_bar)

        #* Adding label underneath the app
        self.content_label = Label(text = "Welcome to my App!")
        layout.add_widget(self.content_label)

        return layout
    
    def on_home(self, instance):
        self.content_label.text = "Home clicked!"

    def on_settings(self, instance):
        self.content_label.text = "Settings clicked!"
    
    def on_about(self, instance):
        self.content_label.text = "About clicked!"

    def on_help(self, instance):
        self.content_label.text = "Help clicked!"

#* Running the app
if __name__ == "__main__":
    ActionBarApp().run()