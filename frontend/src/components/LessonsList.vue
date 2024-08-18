<template>
  <div>
    <h1>Lezioni Disponibili</h1>
    <ul v-if="lessons.length > 0">
      <li v-for="lesson in lessons" :key="lesson.id">
        <router-link :to="{ name: 'LessonDetail', params: { id: lesson.id } }">
          {{ lesson.title }} - {{ lesson.description }}
        </router-link>
      </li>
    </ul>
    <p v-else>Nessuna lezione disponibile al momento.</p>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  data() {
    return {
      lessons: [],
    };
  },
  created() {
    axios.get('lessons/')
        .then(response => {
          this.lessons = response.data;
        })
        .catch(error => {
          console.error(error);
        });
  },
};
</script>
