<template>
  <div class="attendance-view">
    <h1>Посещаемость</h1>
    <p>Дисциплина: {{ selectedDisciplineName }}</p>
    <p>Группа: {{ selectedGroupName }}</p>

    <div v-if="attendanceRecords.length === 0">
      <p>Нет данных о посещаемости для выбранной группы и дисциплины.</p>
    </div>

    <table v-else>
      <thead>
        <tr>
          <th>Студент</th>
          <th>Посещение</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="record in attendanceRecords" :key="record.attendance_id">
          <td>{{ record.student_name }}</td>
          <td>{{ record.present ? 'Присутствовал' : 'Отсутствовал' }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute();

const selectedDisciplineId = ref(route.params.disciplineId);
const selectedGroupId = ref(route.params.groupId);

const selectedDisciplineName = ref('');
const selectedGroupName = ref('');

const attendanceRecords = ref([]);

const fetchAttendance = async () => {
  try {
    const disciplineResponse = await axios.get(`http://127.0.0.1:5000/api/disciplines`);
    const discipline = disciplineResponse.data.find(d => d.discipline_id === selectedDisciplineId.value);
    selectedDisciplineName.value = discipline ? discipline.discipline_name : '';

    const groupResponse = await axios.get(`http://127.0.0.1:5000/api/groups`);
    const group = groupResponse.data.find(g => g.group_id === selectedGroupId.value);
    selectedGroupName.value = group ? group.group_name : '';

    const attendanceResponse = await axios.get(`http://127.0.0.1:5000/api/attendance`);
    attendanceRecords.value = attendanceResponse.data.filter(record =>
      record.lesson_id === selectedDisciplineId.value && record.group_id === selectedGroupId.value
    );

    // Получение имен студентов из других таблиц для удобства отображения
    attendanceRecords.value.forEach(async record => {
      const studentResponse = await axios.get(`http://127.0.0.1:5000/api/students/${record.student_id}`);
      record.student_name = studentResponse.data.student_name;
    });
  } catch (error) {
    console.error(error);
  }
};

onMounted(fetchAttendance);
</script>

<style>
/* Стили для таблицы или других элементов, если необходимо */
</style>
