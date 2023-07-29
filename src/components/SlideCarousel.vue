<template>
    <div class="slide-carousel">
      <vue-carousel :per-page="3" :autoplay="true" :autoplay-timeout="5000">
        <slide v-for="slide in slides" :key="slide.id">
          <div class="slide-item">
            <!-- Your slide content here -->
            <img :src="slide.image" alt="Slide Image" />
            <h3>{{ slide.title }}</h3>
            <p>{{ slide.description }}</p>
          </div>
        </slide>
      </vue-carousel>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        slides: [
          {
            id: 1,
            image: 'C:\\Users\\Acer-Ocpi\\Desktop\\delia\\vue\\vueapp\\src\\assets\\t1.jpg',
            title: 'Slide 1',
            description: 'Description for Slide 1',
          },
          {
            id: 2,
            image: '../assets/t2.jpg',
            title: 'Slide 2',
            description: 'Description for Slide 2',
          },
          {
            id: 3,
            image: './../assets/t3.jpg',
            title: 'Slide 3',
            description: 'Description for Slide 3',
          },
          // Add more slides as needed
        ],
      };
    },
  };
  </script>
  
  <style>
  .my-component {
  /* Set the background image using the url() function and the relative path to the image */
  background-image: url('../assets/1a.jpg');

  /* Set the background size and other properties as needed */
  background-size: cover;
  background-position: center;
  /* Add more styles here to customize the background appearance */

  /* Set the height of the component to display the background image */
  /* For example, if you want the component to cover the entire viewport */
  height: 100vh;
  }
  .slide-carousel {
    max-width: 800px;
    margin: 0 auto;
  }
  
  .slide-item {
    text-align: center;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .slide-item img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
  }
  
  h3 {
    margin-top: 10px;
  }
  
  p {
    margin-top: 5px;
  }


  </style>
  