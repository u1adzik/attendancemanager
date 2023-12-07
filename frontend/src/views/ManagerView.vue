<script setup>
import BackToIndex from '../components/BackToIndex.vue'

import { ref, onMounted, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';

const disciplines = ref([]);

const selectedDiscipline = ref(null);

const fetchDisciplines = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:5000/api/disciplines');
        disciplines.value = response.data;
    } catch (error) {
        console.error(error);
    }
};

onMounted(fetchDisciplines);

const selectedDisciplineName = computed(() => {
    const discipline = disciplines.value.find(d => d.discipline_id === selectedDiscipline.value);
    return discipline ? discipline.discipline_name : '';
});

const groups = ref([]);

const selectedGroup = ref(null);

const fetchGroups = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:5000/api/groups');
        groups.value = response.data;
    } catch (error) {
        console.error(error);
    }
};

onMounted(fetchGroups);

const selectedGroupName = computed(() => {
    const group = groups.value.find(g => g.group_id === selectedGroup.value);
    return group ? group.group_name : '';
});

const route = useRoute();
const router = useRouter();

const viewAttendance = () => {
  const selectedDisciplineId = selectedDiscipline.value;
  const selectedGroupId = selectedGroup.value;

  router.push({
    name: 'AttendanceView',
    params: {
      disciplineId: selectedDisciplineId,
      groupId: selectedGroupId
    }
  });

  console.log("Hello");
};
</script>

<template>
    <BackToIndex />

    <div class="management-container">
        <label for="discipline">Выберите дисциплину:</label>
        <select v-model="selectedDiscipline" id="discipline">
            <option v-for="discipline in disciplines" :key="discipline.discipline_id" :value="discipline.discipline_id">
                {{ discipline.discipline_name }}
            </option>
        </select>
        <p>Выбранная дисциплина: {{ selectedDisciplineName }}</p>

        <label for="group">Выберите группу:</label>
        <select v-model="selectedGroup" id="group">
            <option v-for="group in groups" :key="group.group_id" :value="group.group_id">
                {{ group.group_name }}
            </option>
        </select>
        <p>Выбранная группа: {{ selectedGroupName }}</p>

        <!-- Кнопка для перехода к просмотру посещаемости -->
        <button v-if="selectedDiscipline && selectedGroup" @click="viewAttendance">Просмотр посещаемости</button>
    </div>
</template>

<style>
.management-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0 10vw;
    width: 100vw;
    height: 100vh;
    background-color: #0f7bb9;
    color: #E4ECF3;
}

.management-container label, .management-container p {
}
</style>