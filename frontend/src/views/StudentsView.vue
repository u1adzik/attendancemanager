<template>
    <div class="student-details">
      <h2>Информация о студенте</h2>
      <div v-if="student">
        <p><strong>Имя студента:</strong> {{ student.student_name }}</p>
        <p><strong>ID студента:</strong> {{ student.student_id }}</p>
        <!-- Другие детали студента -->
      </div>
      <div v-else>
        <p>Студент не найден или загружается...</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { useRoute } from 'vue-router';
  
  const studentId = ref(null);
  const student = ref(null);
  const route = useRoute();
  
  // Получение ID студента из маршрута
  studentId.value = route.params.id;
  
  // Функция для загрузки информации о студенте
  const fetchStudent = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/api/students/${studentId.value}`);
      student.value = response.data;
    } catch (error) {
      console.error(error);
      student.value = null;
    }
  };
  
  onMounted(fetchStudent);
  </script>
  
  <style>
  /* Стили для компонента, если необходимо */
  </style>
  