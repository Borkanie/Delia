<template>
    <div>
      <input v-model="query" placeholder="Search events in Cluj" />
      <button @click="search">Search</button>
      <div v-if="events.length">
        <h2>Events</h2>
        <ul>
          <li v-for="event in events" :key="event.link">
            <a :href="event.link" target="_blank">{{ event.title }}</a>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        query: '',
        events: [],
        apiKey: 'AIzaSyAwE4cqVZCvAqd3e4oCFcXsc-Q99KNSRLA',
        searchEngineId: 'a2ab5f24f3c31440a',
      };
    },
    methods: {
      async search() {
        try {
          const response = await axios.get('https://www.googleapis.com/customsearch/v1', {
            params: {
              key: this.apiKey,
              cx: this.searchEngineId,
              q: `party in Cluj today`,
            },
          });
          this.events = response.data.items || [];
        } catch (error) {
          console.error('Error fetching events:', error);
        }
      },
    },
  };
  </script>
  