<template>
    <div>
      <h1>Attendance View</h1>
      <table>
        <thead>
          <tr>
            <th>Student ID</th>
            <th>Student Name</th>
            <th>Attendance</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="student in students" :key="student.student_id">
            <td>{{ student.student_id }}</td>
            <td>{{ student.student_name }}</td>
            <td>{{ getAttendance(student.student_id) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    data() {
      return {
        students: [],
        attendance: [],
      };
    },
    mounted() {
      const disciplineId = this.$route.params.disciplineId;
      const groupId = this.$route.params.groupId;
  
      this.fetchStudents(groupId);
      this.fetchAttendance(disciplineId, groupId);
    },
    methods: {
      async fetchStudents(groupId) {
        try {
          const response = await axios.get(`http://127.0.0.1:5000/api/students?group_id=${groupId}`);
          this.students = response.data;
        } catch (error) {
          console.error(error);
        }
      },
      async fetchAttendance(disciplineId, groupId) {
        try {
          const response = await axios.get(`http://127.0.0.1:5000/api/attendance?lesson_id=${disciplineId}&group_id=${groupId}`);
          this.attendance = response.data;
        } catch (error) {
          console.error(error);
        }
      },
      getAttendance(studentId) {
        const studentAttendance = this.attendance.filter(
          (record) => record.student_id === studentId
        );
        const presentCount = studentAttendance.filter((record) => record.present === 1)
          .length;
        return `${presentCount}/${studentAttendance.length}`;
      },
    },
  };
  </script>