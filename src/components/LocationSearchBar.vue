<template>
  <!-- Loading overlay with spinner (adjust the markup as needed) -->
  <div v-if="loading" class="loading-overlay">
      <div class="spinner"></div>
    </div>
  <div v-else class="event-search-bar">
    <input type="text" v-model="searchQuery" placeholder="Enter a event..." @input="handleInput" />
    <button @click="search">Search</button>
   </div>
</template>
  
<script>
var lodatingNumber = 0;
//const lock = new Lock();
export default {
  name: 'LocationSearchBar',
  data() {
    return {
      searchQuery: '',
      loading: false
    };
  },
  methods: {
    addLoading(){
      //lock.acquire();
      lodatingNumber+=1;
      if(lodatingNumber > 0){
        this.loading = true;
      }      
      //lock.release();
    },
    substractLoading(){
      //lock.acquire();
      lodatingNumber-=1;
      if(lodatingNumber == 0){
        this.loading = false;
      }
      
      //lock.release();
    },
    handleInput() {
      // Handle input changes if needed
    },
    async fetchWithTimeout(url, timeout = 60000) {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), timeout);

    try {
      const response = await fetch(url, { signal: controller.signal });
      clearTimeout(timeoutId); // Clear the timeout since the request succeeded
      return response;
    } catch (error) {
      clearTimeout(timeoutId); // Clear the timeout on error as well
      throw error;
    }
    },
    StringIntoInstagramFormat(event){
      return event.replace(/\s+/g, "").toLowerCase();
    },
    GetPostsAboutEvent(event) {
      this.addLoading();
      this.fetchWithTimeout(`http://localhost:5000/facebook?query=${event}&posts=10`)
        .then(response => {
          this.substractLoading();
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          this.$emit('facebook-result-ok', data);
        })
        .catch(error => {
          // Handle errors
          console.error('facebook-result-error', error);
        });
      this.addLoading();
      this.fetchWithTimeout(`http://localhost:5000/instagram?query=${this.StringIntoInstagramFormat(event)}`)
        .then(response => {
          this.substractLoading();
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          this.$emit('instagram-result-ok', data);
        })
        .catch(error => {
          // Handle errors
          console.error('instagram-result-error', error);
        });
    },
    async search() {
      console.log(this.searchQuery);
      const result = this.GetPostsAboutEvent(this.searchQuery)
      
      this.$emit('resultOK', result);
      //this.$emit('search', this.searchQuery);
      },
     
    },
  };
</script>
  
<style>
.event-search-bar {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.event-search-bar input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.event-search-bar button {
  padding: 8px 12px;
  margin-left: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.event-search-bar button:hover {
  background-color: #0056b3;
}

.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.spinner {
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-top: 4px solid #ffffff;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

</style>
  