from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty #* This allows python objects links to the .kv file
from kivy.lang import Builder #* Manually load the .kv file (because the name is not main, so to avoid filename confusion with the python file)

#! Main screen class
class MainScreen(TabbedPanel):
    pass #* There will be no codes here since the .kv file with take care of the codes

#! To-Do list tab class
class ToDoList(BoxLayout):
    #* Linking components using ObjectProperty
    task_input = ObjectProperty(None) #* Link to the text input on .kv
    task_grid = ObjectProperty(None) #* Link to the grid layout on .kv
    priority_spinner = ObjectProperty(None) #* Link to the spinner on .kv

    #! Function to add tasks to the task grid
    def add_task(self):
        task = self.task_input.text #* Get the taks entered by the user
        priority = self.priority_spinner.text #* Get the selected priority from the spinner

        #* Only add the task if the task input is not empty
        if task != "":
            task_row = self.create_task_row(task, priority) #* Create task row with task and priority
            self.task_grid.add_widget(task_row) #* Add the created task row to the grid
            self.task_input.text = "" #* Clear the input field after adding the task

    #! Function to create a row in the task grid
    def create_task_row(self, task, priority):
        #* Create BoxLayout for each task row
        task_layout = BoxLayout(size_hint_y=None, height=80)

        #* Create labels to display task and priority
        task_label = Label(text=task, size_hint_x=0.6) #* Label for task name
        priority_label = Label(text=priority, size_hint_x=0.2) #* Label for task priority

        #* Create a delete button for each task
        delete_button = Button(text="Delete", size_hint_x=0.2, width=180)

        #* Bind the delete button to remove the task row when pressed
        delete_button.bind(on_press=lambda x: self.task_grid.remove_widget(task_layout))

        #* Add the task label, priority label, and delete button to the task row layout
        task_layout.add_widget(task_label)
        task_layout.add_widget(priority_label)
        task_layout.add_widget(delete_button)

        return task_layout #* Return the complete task row
    
    #! Function to sort tasks by priority
    def sort_tasks(self):
        #* Priority sorting order: Easy --> Normal --> Hard
        priority_order = {"Easy": 1, "Normal": 2, "Hard": 3}

        #* Retrieve all task rows (BoxLayouts) from the task_grid
        tasks = list(self.task_grid.children)

        #* Sort tasks by priority (children[1] represents the priority label), reverse=True means higher priority comes first
        tasks_sorted = sorted(tasks, key=lambda x: priority_order[x.children[1].text])

        #* Clear the current task grid and add again the sorted tasks
        self.task_grid.clear_widgets()
        for task_row in tasks_sorted:
            self.task_grid.add_widget(task_row)

#! Habit Tracker tab
class HabitTracker(BoxLayout):
    #* Linking components using ObjectProperty
    habit_input = ObjectProperty(None) #* Link to the text input on .kv
    habit_grid = ObjectProperty(None) #* Link to the grid layout on .kv
    repeat_spinner = ObjectProperty(None) #* Link to the spinner on .kv

    #! Function to add a habit to the habit grid
    def add_habit(self):
        habit = self.habit_input.text #* Get the habit entered by the user
        repeat = self.repeat_spinner.text #* Get the selected repetition from the spinner

        #* Only add the habit if the habit input is not empty
        if habit != "":
            habit_row = self.create_habit_row(habit, repeat) #* Create a habit row with habit and repetition
            self.habit_grid.add_widget(habit_row) #* Add the created habit row to the grid
            self.habit_input.text = "" #* Clear the input field after adding the habit

    #! Function to create a row in the habit grid
    def create_habit_row(self, habit, repeat):
        #* Create a BoxLayout for each habit row
        habit_layout = BoxLayout(size_hint_y=None, height=80)

        #* Create labels to display habit and repetition
        habit_label = Label(text=habit, size_hint_x=0.6) #* Label for habit name
        repeat_label = Label(text=repeat, size_hint_x=0.2) #* Label for habit repetition

        #* Create a delete button for each habit
        delete_button = Button(text="Delete", size_hint_x=0.2, width=180)

        #* Bind the delete button to remove the habit row when pressed
        delete_button.bind(on_press=lambda x: self.habit_grid.remove_widget(habit_layout))

        #* Add the habit label, repetition label, and delete button to the habit row layout
        habit_layout.add_widget(habit_label)
        habit_layout.add_widget(repeat_label)
        habit_layout.add_widget(delete_button)

        return habit_layout #* Return the complete habit row
    
    #! Function to sort habits by repetition
    def sort_habits(self):
        #* Priority sorting order: Daily --> Weekly --> Monthly --> Yearly
        repeat_order = {"Daily": 1, "Weekly": 2, "Monthly": 3, "Yearly": 4}

        #* Get all habit row (BoxLayouts) from the habit grid
        habits = list(self.habit_grid.children)

        #* Sort habits by repetition (children[1] represents the repetition label), reverse=True means higher repetition comes first
        habits_sorted = sorted(habits, key=lambda x: repeat_order[x.children[1].text])

        #* Clear the current habit grid and add again the sorted habits
        self.habit_grid.clear_widgets()
        for habit_row in habits_sorted:
            self.habit_grid.add_widget(habit_row)

#! Main application class
class MainApp(App):
    #* Build function that returns the MainScreen (with To-Do list tab and Habit tracker tab)
    def build(self):
        #* Load the .kv file manually
        Builder.load_file('DafzAppKivy-Extend.kv')
        return MainScreen()
    
#! Run the application
if __name__ == '__main__':
    MainApp().run()