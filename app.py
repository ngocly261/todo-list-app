 # Thêm công việc vào danh sách
def add_task(task_list, task_name):
    task = {'name': task_name, 'completed': False}
    task_list.append(task)
    return task_list

# Đánh dấu công việc hoàn thành
def complete_task(task_list, task_index):
    if 0 <= task_index < len(task_list):
        task_list[task_index]['completed'] = True
    else:
        print("Chỉ số không hợp lệ.")

# Hiển thị danh sách công việc
def list_tasks(task_list):
    print("Danh sách công việc:")
    for index, task in enumerate(task_list, start=1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{index}. {status} {task['name']}")

# Xóa công việc theo chỉ số
def delete_task(task_list, task_index):
    if 0 <= task_index < len(task_list):
        deleted = task_list.pop(task_index)
        print(f"Đã xóa: {deleted['name']}")
    else:
        print("Chỉ số không hợp lệ.")

# Phần chạy chính
if __name__ == "__main__":
    tasks = []
    tasks = add_task(tasks, "Học Git")
    tasks = add_task(tasks, "Làm bài tập Python")
    tasks = add_task(tasks, "Viết báo cáo")

    complete_task(tasks, 1)   # Đánh dấu công việc thứ 2 là hoàn thành
    delete_task(tasks, 0)     # Xóa công việc đầu tiên

    list_tasks(tasks)
