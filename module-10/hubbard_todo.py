"""Module 10.2 GUI ToDo assignment.

Author: Prince Hubbard
Course: CSD-325 Advanced Python
Assignment: Module 10.2 GUI ToDo

This Tkinter application lets a user add scrolling to-do items, removes an
item with the right mouse button, and exits through the File menu.
"""

import argparse
import tkinter as tk
from tkinter import ttk


class ToDoApplication:
    """Create and manage the Hubbard-ToDo graphical interface."""

    BLUE = "#1F4E78"
    GOLD = "#F4B942"

    def __init__(self, root, tutorial_mode=False):
        """Build the window, menu, input controls, and scrolling task list."""
        self.root = root
        self.tutorial_mode = tutorial_mode
        self.root.title("Scrolling To-Do" if tutorial_mode else "Hubbard-ToDo")
        self.root.geometry("620x500")
        self.root.minsize(500, 380)

        if not tutorial_mode:
            self._build_menu()
        self._build_header()
        self._build_task_list()

    def _build_menu(self):
        """Create the File menu and its Exit command."""
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(
            menu_bar,
            tearoff=False,
            background=self.BLUE,
            foreground="white",
            activebackground=self.GOLD,
            activeforeground="black",
        )
        file_menu.add_command(label="Exit", command=self.root.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.configure(menu=menu_bar)

    def _build_header(self):
        """Create the title, deletion instructions, and task-entry controls."""
        header = tk.Frame(self.root, background="#F5F7FA", padx=20, pady=18)
        header.pack(fill=tk.X)

        tk.Label(
            header,
            text="Scrolling To-Do" if self.tutorial_mode else "Hubbard-ToDo",
            background="#F5F7FA",
            foreground="#222222" if self.tutorial_mode else self.BLUE,
            font=("Segoe UI", 22, "bold"),
        ).pack()

        tk.Label(
            header,
            text=(
                "Enter a task below. Left-click a task to delete it."
                if self.tutorial_mode
                else "Enter a task below. Right-click a task to delete it."
            ),
            background="#F5F7FA",
            foreground="#333333",
            font=("Segoe UI", 10),
        ).pack(pady=(4, 14))

        entry_row = tk.Frame(header, background="#F5F7FA")
        entry_row.pack(fill=tk.X)
        self.task_entry = ttk.Entry(entry_row, font=("Segoe UI", 11))
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.task_entry.bind("<Return>", self.add_task)

        tk.Button(
            entry_row,
            text="Add Task",
            command=self.add_task,
            background=self.BLUE,
            foreground="white",
            activebackground=self.GOLD,
            activeforeground="black",
            relief=tk.FLAT,
            padx=18,
            pady=6,
            font=("Segoe UI", 10, "bold"),
        ).pack(side=tk.RIGHT)

    def _build_task_list(self):
        """Create the scrolling list and bind right-click deletion."""
        body = tk.Frame(self.root, background="white", padx=20, pady=18)
        body.pack(fill=tk.BOTH, expand=True)

        self.task_list = tk.Listbox(
            body,
            activestyle="none",
            selectbackground="#D9E7F3",
            selectforeground="black",
            font=("Segoe UI", 12),
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="#C7CDD4",
        )
        scrollbar = ttk.Scrollbar(body, orient=tk.VERTICAL, command=self.task_list.yview)
        self.task_list.configure(yscrollcommand=scrollbar.set)
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        delete_event = "<Button-1>" if self.tutorial_mode else "<Button-3>"
        self.task_list.bind(delete_event, self.delete_task)

    def add_task(self, event=None):
        """Add a nonempty task and apply alternating complementary colors."""
        task = self.task_entry.get().strip()
        if not task:
            return

        index = self.task_list.size()
        self.task_list.insert(tk.END, task)
        if self.tutorial_mode:
            self.task_list.itemconfig(index, background="#E8EDF2", foreground="black")
        elif index % 2 == 0:
            self.task_list.itemconfig(index, background=self.BLUE, foreground="white")
        else:
            self.task_list.itemconfig(index, background=self.GOLD, foreground="black")
        self.task_entry.delete(0, tk.END)
        self.task_entry.focus_set()

    def delete_task(self, event):
        """Delete the task beneath the pointer when right-clicked."""
        if self.task_list.size() == 0:
            return
        index = self.task_list.nearest(event.y)
        bounds = self.task_list.bbox(index)
        if bounds and bounds[1] <= event.y <= bounds[1] + bounds[3]:
            self.task_list.delete(index)
            self._refresh_colors()

    def _refresh_colors(self):
        """Restore alternating colors after a task is removed."""
        for index in range(self.task_list.size()):
            if self.tutorial_mode:
                self.task_list.itemconfig(index, background="#E8EDF2", foreground="black")
            elif index % 2 == 0:
                self.task_list.itemconfig(index, background=self.BLUE, foreground="white")
            else:
                self.task_list.itemconfig(index, background=self.GOLD, foreground="black")

    def load_demo_tasks(self):
        """Populate sample tasks when the program is launched with --demo."""
        for task in (
            "Finish Python assignment",
            "Review chapter notes",
            "Push module-10 to GitHub",
            "Submit the assignment ZIP",
        ):
            self.task_entry.insert(0, task)
            self.add_task()


def main():
    """Start the Tkinter event loop."""
    parser = argparse.ArgumentParser(description="Run Hubbard-ToDo.")
    parser.add_argument("--demo", action="store_true", help="load sample tasks")
    parser.add_argument(
        "--tutorial",
        action="store_true",
        help="show the unmodified tutorial stage for its required screenshot",
    )
    args = parser.parse_args()

    root = tk.Tk()
    application = ToDoApplication(root, tutorial_mode=args.tutorial)
    if args.demo:
        application.load_demo_tasks()
    root.mainloop()


if __name__ == "__main__":
    main()
