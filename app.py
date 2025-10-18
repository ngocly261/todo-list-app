# Hàm thêm công việc
def add_task(task_list, task):
    task_list.append(task)
    return task_list

# Hàm liệt kê công việc
def list_tasks(task_list):
    print("Danh sách công việc:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")

# Phần chạy chính
if __name__ == "__main__":
    tasks = []
    tasks = add_task(tasks, "Học Git")
    tasks = add_task(tasks, "Làm bài tập Python")
    list_tasks(tasks)
