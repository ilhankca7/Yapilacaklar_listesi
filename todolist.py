class Task: # Task sınıfını tanımlıyoruz. Bu sınıf, her bir görevi temsil eder.
    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.completed = False
class TodoList: # TodoList sınıfını tanımlıyoruz. Bu sınıf, kullanıcının yapılacaklar listesini yönetir.
    def __init__(self):
        self.tasks = [] 

    def add_task(self,title,description):  # Yeni bir görev eklemek için kullanılan metot
        task = Task(title,description)
        self.tasks.append(task)
    def edit_task(self,index,title,description): # Bir görevi düzenlemek için kullanılan metot
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = title
            self.tasks[index].description = description
        else:
            print("geçersiz görev dizini")    

    def mark_completed(self, index): # Bir görevi tamamlandı olarak işaretlemek için kullanılan metot
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            print("Geçersiz görev dizini")
    def delete_task(self,index): # Bir görevi silmek için kullanılan metot
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Geçersiz görev dizini")
    def display_tasks(self):   # Tüm görevleri görüntülemek için kullanılan metot
        if self.tasks:
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task.title} - {'completed' if task.completed else 'Pending'}") 
        else:
            print("Hayir teşekkürler...")

def main():  #Ana programın başlnagıcı
    todo_list  = TodoList()


    while True:
        print("\nTodo App Menu:")
        print("1. Add Task ")
        print("2. Edit Task ")
        print("3. Mark Task as Completed ")
        print("4. Delete Task ")
        print("5. Display Tasks ")
        print("6. Quit ")
        
        choice = input("Seçiminizi  yapin : ")

        if choice == '1':  # Yeni bir görev ekleme işlemi
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == '2':  # Görev düzenleme işlemi
            index = int(input("Enter task index to edit: ")) - 1
            title = input("Enter new title: ")
            description = input("Enter new description: ")
            todo_list.edit_task(index, title, description)
        elif choice == '3':  # Görevi tamamlandı olarak işaretleme işlemi
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == '4':  # Görev silme işlemi
            index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':  # Tüm görevleri görüntüleme işlemi
            todo_list.display_tasks()
        elif choice == '6':  # Programdan çıkma işlemi
            print("Exiting program. Goodbye!")
            break  # Döngüyü sonlandırarak programdan çıkıyoruz.
        else:
            print("Invalid choice. Please enter a valid option.")  # Geçersiz seçim durumunda hata mesajı veriyoruz.

# Programın ana fonksiyonunu çağırıyoruz.
if __name__ == "__main__":
    main()








