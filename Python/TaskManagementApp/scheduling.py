import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QComboBox, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QFont
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="tmastorage",
        password="jonggol",
        database="TaskManagementApp"
    ) 

class TaskScheduler(QWidget):
    def __init__(self, user_id, nickname):
        super().__init__()
        self.user_id = user_id  # Store user ID for database queries
        self.nickname = nickname

        self.setWindowTitle("Task Scheduling - TSS")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Title
        self.label_title = QLabel(f"User's task scheduling space - {self.nickname} (please save before exiting)", self)
        self.label_title.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(self.label_title)

        # Task Table
        self.task_table = QTableWidget()
        self.task_table.setColumnCount(4)
        self.task_table.setHorizontalHeaderLabels(["Task", "Deadline (numbers)", "Priority", "Occurrence"])
        layout.addWidget(self.task_table)

        # Load tasks from database
        self.load_tasks()

        # Buttons
        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Add Task")
        self.btn_add.clicked.connect(self.add_task)
        btn_layout.addWidget(self.btn_add)

        self.btn_delete = QPushButton("Delete Task")
        self.btn_delete.clicked.connect(self.delete_task)
        btn_layout.addWidget(self.btn_delete)

        self.btn_save = QPushButton("Save")
        self.btn_save.clicked.connect(self.save_tasks)
        btn_layout.addWidget(self.btn_save)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def load_tasks(self):
        """ Load tasks from database and display in the table """
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT task_name, deadline, priority, occurrence FROM tasks WHERE user_id = %s", (self.user_id,))
            tasks = cursor.fetchall()
            conn.close()

            self.task_table.setRowCount(len(tasks))
            for row, task in enumerate(tasks):
                for col, data in enumerate(task):
                    self.task_table.setItem(row, col, QTableWidgetItem(str(data)))

    def add_task(self):
        """ Add a new empty row in the table """
        row_count = self.task_table.rowCount()
        self.task_table.insertRow(row_count)

    def delete_task(self):
        """ Delete the selected task from table and database """
        selected_row = self.task_table.currentRow()
        if selected_row != -1:
            task_name = self.task_table.item(selected_row, 0).text()

            conn = connect_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM tasks WHERE task_name = %s AND user_id = %s", (task_name, self.user_id))
                conn.commit()
                conn.close()

            self.task_table.removeRow(selected_row)
            QMessageBox.information(self, "Success", "Task deleted successfully!")

    def save_tasks(self):
        """ Save tasks from table to database """
        conn = connect_db()
        if conn:
            cursor = conn.cursor()

            # Delete existing tasks before saving
            cursor.execute("DELETE FROM tasks WHERE user_id = %s", (self.user_id,))

            # Insert updated tasks
            for row in range(self.task_table.rowCount()):
                task_name = self.task_table.item(row, 0).text().strip() if self.task_table.item(row, 0) else ""
                deadline = self.task_table.item(row, 1).text().strip() if self.task_table.item(row, 1) else None
                priority = self.task_table.item(row, 2).text().strip() if self.task_table.item(row, 2) else "Medium"
                
                # ✅ Fix: Ensure occurrence is properly stored
                occurrence_item = self.task_table.item(row, 3)
                occurrence = occurrence_item.text().strip() if occurrence_item and occurrence_item.text() else ""

                # ✅ Fix: Ensure occurrence is not None before inserting
                occurrence = occurrence if occurrence else "One-time"

                # ✅ Fix: Print debug output to verify occurrence is being read correctly
                print(f"Saving Task: {task_name}, Deadline: {deadline}, Priority: {priority}, Occurrence: {occurrence}")

                cursor.execute("""
                    INSERT INTO tasks (user_id, task_name, deadline, priority, occurrence)
                    VALUES (%s, %s, %s, %s, %s)
                """, (self.user_id, task_name, deadline, priority, occurrence))

            conn.commit()
            conn.close()
            QMessageBox.information(self, "Success", "Tasks saved successfully!")

# Run the App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskScheduler(user_id=1, nickname="User")  # Test with dummy user
    window.show()
    sys.exit(app.exec_())