<template>
  <div class="location-search-bar">
    <input type="text" v-model="searchQuery" placeholder="Enter a location..." @input="handleInput" />
    <button @click="search">Search</button>
    <button class="location-button" @click="getUserLocation">Get My Location</button>
  </div>
</template>
  
<script>
export default {
  name: 'LocationSearchBar',
  data() {
    return {
      searchQuery: '',
    };
  },
  methods: {
    handleInput() {
      // Handle input changes if needed
    },
    GetElementsAtLocation(locationQuery) {

      fetch(`http://localhost:5000/search?query=${locationQuery}`)
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          this.$emit('resultGood', data);
        })
        .catch(error => {
          // Handle errors
          console.error('Error:', error);
        });
    },
    async search() {
      result = GetElementsAtLocation("events+in+cluj")
      
      this.$emit('resultOK', result);
      //this.$emit('search', this.searchQuery);
      },
      getUserLocation() {
        if ('geolocation' in navigator) {
          navigator.geolocation.getCurrentPosition(
            (position) => {
              const latitude = position.coords.latitude;
              const longitude = position.coords.longitude;
              console.log('User location:', latitude, longitude);

              // Use the user's location for further actions (e.g., search)
            },
            (error) => {
              console.error('Error getting user location:', error.message);
            }
          );
        } else {
          console.error('Geolocation is not available in this browser.');
        }
      },
    },
  };
</script>
  
<style>
.location-search-bar {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.location-search-bar input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.location-search-bar button {
  padding: 8px 12px;
  margin-left: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.location-search-bar button:hover {
  background-color: #0056b3;
}

.location-search-bar .location-button {
  padding: 8px 12px;
  margin-left: 10px;
  background-color: #28a745;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.location-search-bar .location-button:hover {
  background-color: #1e7e34;
}
</style>
  