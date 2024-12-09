from typing import List, Dict, Any
from datetime import datetime

def schedule_tasks(task_hierarchy: Dict[str, Any], level: int = 0) -> List[Dict[str, Any]]:
    """
    Recursively schedules tasks based on their hierarchy, dependencies, and priorities.
    
    Args:
        task_hierarchy (Dict): Dictionary containing task information
        level (int): Current recursion level (used for indentation in printing)
        
    Returns:
        List[Dict]: List of scheduled tasks in order of execution
    """
    # Base case: if no task or no subtasks
    if not task_hierarchy:
        return []
    
    scheduled_tasks = []
    
    # Process current task
    current_task = {
        'id': task_hierarchy['id'],
        'name': task_hierarchy['name'],
        'priority': task_hierarchy.get('priority', 0),  # Default priority 0 if not specified
        'level': level
    }
    
    # Add current task to scheduled tasks
    scheduled_tasks.append(current_task)
    
    # Process subtasks if they exist
    if 'subtasks' in task_hierarchy and task_hierarchy['subtasks']:
        # Sort subtasks by priority (if specified)
        sorted_subtasks = sorted(
            task_hierarchy['subtasks'],
            key=lambda x: x.get('priority', 0),
            reverse=True  # Higher priority first
        )
        
        # Recursively schedule each subtask
        for subtask in sorted_subtasks:
            scheduled_tasks.extend(schedule_tasks(subtask, level + 1))
    
    return scheduled_tasks

def print_scheduled_tasks(scheduled_tasks: List[Dict[str, Any]]) -> None:
    """
    Prints the scheduled tasks in a formatted way.
    
    Args:
        scheduled_tasks (List[Dict]): List of scheduled tasks
    """
    print("\nScheduled Tasks:")
    print("-" * 50)
    for task in scheduled_tasks:
        indent = "  " * task['level']
        priority_str = f"(Priority: {task['priority']})" if 'priority' in task else ""
        print(f"{indent}Task ID: {task['id']} - {task['name']} {priority_str}")

def main():
    # Test case 1: Simple hierarchy with priorities
    test_hierarchy_1 = {
        'id': 1,
        'name': 'Project Setup',
        'priority': 3,
        'subtasks': [
            {
                'id': 2,
                'name': 'Install Dependencies',
                'priority': 2,
                'subtasks': []
            },
            {
                'id': 3,
                'name': 'Configure Environment',
                'priority': 1,
                'subtasks': []
            }
        ]
    }
    
    # Test case 2: Complex hierarchy with nested subtasks
    test_hierarchy_2 = {
        'id': 1,
        'name': 'Website Development',
        'priority': 5,
        'subtasks': [
            {
                'id': 2,
                'name': 'Frontend Development',
                'priority': 4,
                'subtasks': [
                    {
                        'id': 4,
                        'name': 'UI Design',
                        'priority': 3,
                        'subtasks': []
                    },
                    {
                        'id': 5,
                        'name': 'Implementation',
                        'priority': 2,
                        'subtasks': []
                    }
                ]
            },
            {
                'id': 3,
                'name': 'Backend Development',
                'priority': 4,
                'subtasks': [
                    {
                        'id': 6,
                        'name': 'API Development',
                        'priority': 3,
                        'subtasks': []
                    },
                    {
                        'id': 7,
                        'name': 'Database Setup',
                        'priority': 4,
                        'subtasks': []
                    }
                ]
            }
        ]
    }
    
    # Test both hierarchies
    print("\nTest Case 1: Simple Hierarchy")
    scheduled_tasks_1 = schedule_tasks(test_hierarchy_1)
    print_scheduled_tasks(scheduled_tasks_1)
    
    print("\nTest Case 2: Complex Hierarchy")
    scheduled_tasks_2 = schedule_tasks(test_hierarchy_2)
    print_scheduled_tasks(scheduled_tasks_2)
    
    # Time and Space Complexity Analysis
    print("\nTime and Space Complexity Analysis:")
    print("-" * 50)
    print("Time Complexity: O(n log n) where n is the total number of tasks")
    print("- The algorithm needs to visit each task once: O(n)")
    print("- Sorting subtasks by priority at each level: O(log n)")
    print("\nSpace Complexity: O(n)")
    print("- Space needed to store all tasks in the scheduled_tasks list")
    print("- Recursive call stack depth is proportional to the maximum nesting level")

if __name__ == "__main__":
    main()
