<script setup lang="ts">
import axios from 'axios'
import { ref, onMounted } from 'vue'

// Function to initialize Axios with authentication
const initializeAxios = (username: string, password: string, baseUrl: string) => {
  return axios.create({
    baseURL: baseUrl,
    auth: {
      username: username,
      password: password
    }
  });
}

// Login information
const username = import.meta.env.VITE_APP_BACKEND_USERNAME
const password = import.meta.env.VITE_APP_BACKEND_PASSWORD
const baseUrl = import.meta.env.VITE_APP_BACKEND_URL

// Initialize Axios instance
const axiosInstance = initializeAxios(username, password, baseUrl)

// Init of variables type
type TaskStatus = 'todo' | 'done'

const items = ref<any[]>([])
const description = ref<String>('')
const status = ref<TaskStatus>('todo')

// Function to fetch all the tasks from the database
const getTasks = async () => {
  try {
    const response = await axiosInstance.get('/tasks/')
    items.value = response.data;
  } catch(error) {
    console.error('Error fetching data:', error)
    items.value = [error]
  }
};

// Call getTasks function when the page is loading
onMounted(() => {
  getTasks()
})

// Function to add a task to the database and refresh it
const addTask = async () => {
  try {
    const response = await axiosInstance.post('tasks/', {
      description: description.value,
      status: status.value
    })
    
    items.value.push(response.data)
    description.value = ''
    status.value = 'todo'

  } catch(error) {
    console.error('Error adding task', error)
  }
}

const deleteTask = async (taskId : number) => {
  try {
    await axiosInstance.delete(`/tasks/${taskId}`)

    items.value = items.value.filter(task => task.id != taskId)
  } catch(error) {
    console.error('Error deleting task', error)
  }
}

const updateTaskStatus = async (taskId: number, newStatus: string) => {
  try {
    const modifiedTask = items.value.find(item => item.id === taskId)
    if (modifiedTask) {
      modifiedTask.status = newStatus
      const response = await axiosInstance.put(`/tasks/${taskId}`, {
      status: newStatus
    })
    }
  }catch(error){
  console.error('Error: task status not modified: ', error)
  }
}

</script>


<template>
  <div class="container">
    <!-- Box for adding a task -->
    <div class="task-box-container">
      <div class="task-box">
        <h2 class="subtitle">Add Task</h2>
        <div class="task-box-content">
          <!-- Form for adding a new task -->
          <form v-on:submit.prevent="addTask">
            <div class="field">
              <label class="label">Description</label>
              <div class="control">
                <input class="input" type="text" v-model="description">
              </div>
            </div>

            <div class="field">
              <label class="label">Status</label>
              <div class="control">
                <div class="select">
                  <select v-model="status">
                    <option value="todo">To Do</option>
                    <option value="done">Done</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="field">
              <div class="control">
                <button class="button is-link">Submit</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- Columns for To Do and Done tasks -->
    <div class="columns-container">
      <div class="columns">
        <div class="column is-half">
          <h2 class="subtitle">To Do</h2>
          <div class="todo">
            <div class="card">
              <template v-for="item in items" :key="item.id">
                <li v-if="item.status === 'todo'">
                  <!-- Task item with action buttons -->
                  <div class="task-item">
                    <div class="task-description">{{ item.description }}</div>
                    <div class="action-buttons">
                      <!-- Red cross for deleting task -->
                      <button class="delete-button" @click="deleteTask(item.id)">&#10060;</button>
                      <!-- Checkmark for marking task as done -->
                      <button class="checkmark-button" @click="updateTaskStatus(item.id, 'done')">&#10004;</button>
                    </div>
                  </div>
                </li>
              </template>
            </div>
          </div>
        </div>
        <div class="column is-half">
          <h2 class="subtitle">Done</h2>
            <div class="done">
              <div class="card">
                <template v-for="item in items" :key="item.id">
                  <li v-if="item.status === 'done'">
                    <!-- Task item with delete button -->
                    <div class="task-item">
                      <div class="task-description">{{ item.description }}</div>
                        <div class="action-buttons">
                          <!-- Red cross for deleting task -->
                          <button class="delete-button" @click="deleteTask(item.id)">&#10060;</button>
                        </div>
                      </div>
                  </li>
                </template>
              </div>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  padding: 1rem;
}

.task-box-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.task-box {
  border: 1px solid #ccc;
  padding: 1rem;
}

.task-box-content {
  width: 100%; /* Ensure the content takes full width */
  max-width: 400px; /* Limit the width of the content */
}

.task-box-content form {
  display: flex;
  flex-direction: column;
}

.task-box-content .field {
  margin-bottom: 1rem; /* Add some spacing between fields */
}

.select, select {
  width: 100%;
}

.columns-container {
  margin-top: 2rem; /* Add some space between the task box and the columns */
}

.columns {
  display: flex;
  justify-content: space-between;
}

.columns .column {
  width: 49%; /* Adjust width for two columns with a small gap in between */
}

.todo, .done {
  margin-top: 1rem;
}

.card {
  margin-bottom: 20px;
}

.task-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  border: 1px solid #ccc;
}

.task-description {
  flex-grow: 1;
}

.action-buttons {
  display: flex;
}

.delete-button, .checkmark-button {
  background: none;
  border: none;
  cursor: pointer;
}
</style>