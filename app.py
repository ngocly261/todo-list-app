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
# Thêm công việc vào danh sách (với trạng thái chưa hoàn thành)
def add_task(task_list, task_name):
    task = {'name': task_name, 'completed': False}
    task_list.append(task)
    return task_list

# ✅ Đánh dấu công việc là hoàn thành
def complete_task(task_list, task_index):
    if 0 <= task_index < len(task_list):
        task_list[task_index]['completed'] = True
    else:
        print("Chỉ số không hợp lệ.")

# ✅ Liệt kê công việc, hiển thị trạng thái
def list_tasks(task_list):
    print("Danh sách công việc:")
    for index, task in enumerate(task_list, start=1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{index}. {status} {task['name']}")

# Chạy chương trình
if __name__ == "__main__":
    tasks = []
    tasks = add_task(tasks, "Học Git")
    tasks = add_task(tasks, "Làm bài tập Python")
    complete_task(tasks, 0)  # Đánh dấu công việc đầu tiên là hoàn thành
    list_tasks(tasks)