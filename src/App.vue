<template>
  <div class="app">
    <div class="title-region">
      <video class="video" autoplay loop muted>
        <source :src="videoSrc" type="video/mp4" />
          <!-- Add additional source elements for different video formats if needed -->
      </video>  
      <!-- Your content goes here (e.g., other components, text, etc.) -->
      <div class="title-section">
        <h1>EventSpotter</h1>
        <p>Enhancing Event Discovery since 2023</p>
        <LocationSearchBar @search="performSearch"
         class="locationBar"
         @facebook-result-ok="handleFacebookResultOK"
         @facebook-result-error="handleFacebookResultError"
         @instagram-result-ok="handleInstagramResultOK"
         @instagram-result-error="handleInstagramResultError"/>
        <!-- Rest of your content -->      
      </div>
    </div>
    <div class="component-region">
      <item-component
      v-for="item in items"
      :key="item.id"
      :background-image="item.image"
      :title="item.title"
      :description="item.description"
      :hasImage="item.hasImage"
      :background-color="item.backgroundColor"
      />
    </div>    
  </div>
</template>

<script>
import ItemComponent from './components/ItemComponent.vue';
import LocationSearchBar from './components/LocationSearchBar.vue';

const faceBookColor = "linear-gradient(to bottom, rgba(142, 142, 142, 0.8), rgba(231, 231, 231, 0.8))";
const instagramColor = "linear-gradient(to right, rgba(142, 142, 142, 0.8), rgba(231, 231, 231, 0.8))";
export default {
  name: 'App',
  components: {
    ItemComponent,
    LocationSearchBar,    
  },
  data() {
    return {
      items: [
        {
          id: 1,
          backgroundImage: require('@/assets/t1.jpg'),
          title: 'Item 1',
          description: 'Description for Item 1',
          hasImage: true,
          backgroundColor: faceBookColor
        },
        {
          id: 2,
          backgroundImage: require('@/assets/t2.jpg'),
          title: 'Item 2',
          description: 'Description for Item 2',
          hasImage: false,
          backgroundColor: faceBookColor
        },
        {
          id: 3,
          backgroundImage: require('@/assets/t3.jpg'),
          title: 'Item 3',
          description: 'Description for Item 3',
          hasImage: true,
          backgroundColor: instagramColor
        },
        {
          id: 4,
          backgroundImage: require('@/assets/t4.jpg'),
          title: 'Item 4',
          description: 'Description for Item 4',
          hasImage: false,
          backgroundColor: instagramColor
        },
      ],
      videoSrc: require('@/assets/bgvid.mp4'),
    };
  },
  methods: {
    performSearch(){
      this.items = [];
    },
    handleFacebookResultOK(data) {
      
      const posts = data.posts;
      
      var id = this.items.length-1;
      posts.forEach(item => {
        
        // Perform any logic you need here
        if(item.image!="None")
        {
          this.items.push({
          id: id++,
          image: item.image,
          title: item.title,
          description: item.text,
          hasImage: true,
          backgroundColor: faceBookColor
        });
        }else{
          
          this.items.push({
          id: id++,
          image: require('@/assets/t3.jpg'),
          title: item['title'],
          description: item['text'],
          hasImage: false,
          backgroundColor: faceBookColor});
          
        }
       });
    },
    handleFacebookResultError() {
      
    },

    handleInstagramResultOK(data) {
      
      const posts = data.posts;

      var id = this.items.length-1;
      posts.forEach(item => {
          this.items.push({
          id: id++,
          image: item.image,
          title: item.title,
          description: item.text,
          hasImage: true,
          backgroundColor: faceBookColor
        });
        
       });

      // Update the items array with new data
      this.items = newitems;
    },
    handleInstagramResultError() {
      
    },
  },
};
</script>

<style>
.app {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  padding-top: 100px; /* Add some top padding to create space for the title section */
}
.title-region{
   /* Set the child div to take up full width of its parent */
   width: 100%;
  height: 500px; /* Optionally set the height to 100% as well */
}
.video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1; /* Ensure the video is behind the content */
}
.title-section {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  text-align: center;  
  padding: 20px;
  color: #ffffff00;
}
.title-section h1 {
  font-size: 8rem;
  color: rgb(0, 0, 0);
}
.title-section p {
  font-size: 2rem;
  color: rgb(0, 0, 0);
}
.locationBar {
  width: 50%;
  padding-left: 25%;
  align-items: center;
  align-items: center;
}
.component-region{
  width: 100%;
  height: 100%; /* Optionally set the height to 100% as well */
  background-size: cover;
  background-position: center;
  background-image: url('@/assets/l7.jpg');
  background-size: cover; /* Adjust as needed */
  background-position: center; /* Adjust as needed */
  /* Center the child horizontally using flexbox */
  display: flex;
  flex-direction: column; /* Stack items vertically */
  justify-content: center;
  align-items: center;
}
</style>