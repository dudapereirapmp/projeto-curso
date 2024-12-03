document.addEventListener("DOMContentLoaded", () => {
    const taskInput = document.getElementById("task-input");
    const addTaskButton = document.getElementById("add-task");
    const taskList = document.getElementById("task-list");

    // Carregar tarefas
    fetch("/tasks")
        .then(response => response.json())
        .then(tasks => {
            tasks.forEach(addTaskToList);
        });

    // Adicionar nova tarefa
    addTaskButton.addEventListener("click", () => {
        const task = { id: Date.now(), text: taskInput.value };
        fetch("/tasks", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(task)
        }).then(response => {
            if (response.ok) addTaskToList(task);
        });
        taskInput.value = "";
    });

    // Adicionar tarefa à lista
    function addTaskToList(task) {
        const li = document.createElement("li");
        li.className = "task-item";
        li.innerHTML = `${task.text} <button onclick="deleteTask(${task.id})">Excluir</button>`;
        taskList.appendChild(li);
    }

    // Excluir tarefa
    window.deleteTask = (id) => {
        fetch(`/tasks/${id}`, { method: "DELETE" }).then(() => {
            taskList.innerHTML = "";
            fetch("/tasks")
                .then(response => response.json())
                .then(tasks => {
                    tasks.forEach(addTaskToList);
                });
        });
    };
});
