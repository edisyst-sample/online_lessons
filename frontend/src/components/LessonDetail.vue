<template>
  <div v-if="lesson">
    <h2>{{ lesson.title }}</h2>
    <p>{{ lesson.description }}</p>
    <p><strong>Insegnante:</strong> {{ lesson.teacher.name }}</p>
    <p><strong>Numero massimo di studenti:</strong> {{ lesson.max_students }}</p>
    <router-link to="/">Torna all'elenco delle lezioni</router-link>
  </div>
  <p v-else>Caricamento dettagli della lezione...</p>
</template>

<script>
import axios from '../axios';

export default {
  props: ['id'],
  data() {
    return {
      lesson: null,
    };
  },
  created() {
    axios.get(`lessons/${this.id}/`)
        .then(response => {
          this.lesson = response.data;
        })
        .catch(error => {
          console.error(error);
        });
  },
};
</script>
