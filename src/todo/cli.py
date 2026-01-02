"""Command-line interface for the Todo application.

This module provides the TodoCLI class for user interaction.
"""

from todo.service import TodoService


class TodoCLI:
    """Command-line interface for todo operations.

    Provides menu-driven interaction for task management.
    """

    MAX_TITLE_LENGTH = 100
    MAX_DESCRIPTION_LENGTH = 500

    def __init__(self, service: TodoService) -> None:
        """Initialize the CLI with service dependency.

        Args:
            service: TodoService instance for business operations.
        """
        self._service = service
        self._running = False

    def run(self) -> None:
        """Start the main application loop."""
        self._running = True
        while self._running:
            self._display_menu()
            choice = input("Enter your choice (1-6): ").strip()
            self._handle_choice(choice)

    def _display_menu(self) -> None:
        """Display the main menu."""
        print("\n=====================================")
        print("       TODO APP - Phase I")
        print("=====================================\n")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Toggle Complete/Incomplete")
        print("6. Exit\n")

    def _handle_choice(self, choice: str) -> None:
        """Route user choice to appropriate handler.

        Args:
            choice: User's menu selection.
        """
        handlers = {
            "1": self._handle_add_task,
            "2": self._handle_view_tasks,
            "3": self._handle_update_task,
            "4": self._handle_delete_task,
            "5": self._handle_toggle_completion,
            "6": self._handle_exit,
        }

        handler = handlers.get(choice)
        if handler:
            handler()
        else:
            print("\nInvalid choice. Please enter 1-6.")

    def _handle_add_task(self) -> None:
        """Handle adding a new task."""
        print("\n--- Add New Task ---")

        title = input("Enter title: ").strip()
        if not title:
            print("\n✗ Title cannot be empty.")
            return
        if len(title) > self.MAX_TITLE_LENGTH:
            print(f"\n✗ Title too long (max {self.MAX_TITLE_LENGTH} characters).")
            return

        description = input("Enter description: ").strip()
        if len(description) > self.MAX_DESCRIPTION_LENGTH:
            print(f"\n✗ Description too long (max {self.MAX_DESCRIPTION_LENGTH} characters).")
            return

        try:
            task = self._service.add_task(title, description)
            print(f"\n✓ Task added successfully! (ID: {task.id})")
        except ValueError as e:
            print(f"\n✗ {e}")

    def _handle_view_tasks(self) -> None:
        """Handle viewing all tasks."""
        print("\n--- All Tasks ---\n")

        tasks = self._service.get_all_tasks()

        if not tasks:
            print("No tasks found. Add a task to get started!")
            return

        for task in tasks:
            status = "[✓] Complete" if task.is_completed else "[ ] Incomplete"
            print(f"ID: {task.id} | Status: {status}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}\n")

        print("---")
        print(f"Total: {len(tasks)} task(s)")

    def _handle_update_task(self) -> None:
        """Handle updating an existing task."""
        print("\n--- Update Task ---")

        task_id = self._get_valid_task_id("Enter task ID to update: ")
        if task_id is None:
            return

        task = self._service.get_task(task_id)
        if task is None:
            print(f"\n✗ Task with ID {task_id} not found.")
            return

        print(f"\nCurrent Task:")
        print(f"Title: {task.title}")
        print(f"Description: {task.description}\n")

        new_title = input("Enter new title (press Enter to keep current): ").strip()
        if new_title and len(new_title) > self.MAX_TITLE_LENGTH:
            print(f"\n✗ Title too long (max {self.MAX_TITLE_LENGTH} characters).")
            return

        new_description = input("Enter new description (press Enter to keep current): ").strip()
        if new_description and len(new_description) > self.MAX_DESCRIPTION_LENGTH:
            print(f"\n✗ Description too long (max {self.MAX_DESCRIPTION_LENGTH} characters).")
            return

        updated_task = self._service.update_task(
            task_id,
            title=new_title if new_title else None,
            description=new_description if new_description else None,
        )

        if updated_task:
            print("\n✓ Task updated successfully!")
        else:
            print(f"\n✗ Task with ID {task_id} not found.")

    def _handle_delete_task(self) -> None:
        """Handle deleting a task."""
        print("\n--- Delete Task ---")

        task_id = self._get_valid_task_id("Enter task ID to delete: ")
        if task_id is None:
            return

        if self._service.delete_task(task_id):
            print("\n✓ Task deleted successfully!")
        else:
            print(f"\n✗ Task with ID {task_id} not found.")

    def _handle_toggle_completion(self) -> None:
        """Handle toggling task completion status."""
        print("\n--- Toggle Task Completion ---")

        task_id = self._get_valid_task_id("Enter task ID: ")
        if task_id is None:
            return

        task = self._service.toggle_completion(task_id)
        if task is None:
            print(f"\n✗ Task with ID {task_id} not found.")
            return

        if task.is_completed:
            print("\n✓ Task marked as complete!")
        else:
            print("\n✓ Task marked as incomplete!")

    def _handle_exit(self) -> None:
        """Handle application exit."""
        print("\nGoodbye! Thank you for using Todo App.")
        self._running = False

    def _get_valid_task_id(self, prompt: str) -> int | None:
        """Get and validate a task ID from user input.

        Args:
            prompt: The input prompt to display.

        Returns:
            Valid task ID or None if invalid.
        """
        try:
            task_id = int(input(prompt).strip())
            if task_id <= 0:
                print("\n✗ Invalid ID. Please enter a valid positive number.")
                return None
            return task_id
        except ValueError:
            print("\n✗ Invalid ID. Please enter a valid number.")
            return None
