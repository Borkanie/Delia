<template>
    <div class="item">
      <div class="item-background" :style="{ background: backgroundColor }">
        <div class="item-content">
            <div class="title-container" ref="titleContainer">
                <div class="rectangleTitle" :style="{ width: rectangleTitleWidth + 'px' }"></div>
                <h3 class="item-title" ref="itemTitle">{{ title }}</h3>               
            </div>
            <div class="description-container" ref="descriptionContainer">
                <div class="rectangleDescription" :style="{ width: rectangleDescriptionWidth + 'px' }"></div>
                <p class="item-description" ref="itemDescription">{{ description }}</p>             
                <div v-if="hasImage">
                  <img v-if="backgroundImage" :src="backgroundImage" class="item-image" />
                </div>
             </div>            
        </div>
    </div>
    </div>
  </template>
  
  <script>

  export default {
    name: 'ItemComponent',
    props: {
      title: {
        type: String,
        required: true,
      },
      description: {
        type: String,
        required: true,
      },
      hasImage: {
        type: Boolean,
        required: true
      },     
      backgroundImage: {
        type: String,
        required: true,
      },
      backgroundColor:{
        type: String,
        required: true
      }
    },
    data() {console.log(this.backgroundImage);

    return {
        
        rectangleTitleWidth: 0,
        rectangleDescriptionWidth: 0,
    };
  },
  methods: {
    mounted() {
    // Calculate the title width and apply it to the rectangle
    this.rectangleTitleWidth = this.$refs.itemTitle.clientWidth;
    this.rectangleDescriptionWidth = this.$refs.itemDescription.clientWidth;
    },

  },
};
  </script>
  
  <style>
  .item {
    display: flex;
    flex-direction: column;
    width: 700px;
    margin: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    overflow: hidden;
    box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.4); /* Add the shadow effect */
    transition: transform 0.3s ease-in-out; /* Apply transition effect to the transform property */
}

.item:hover {
  transform: translateY(-5px); /* Apply the floating effect on hover */
  box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.4); /* Add a stronger shadow effect on hover */
}

  
  .item-image {
    height: 200px;
    background-size: cover;
    background-position: center;
  }
  
  .item-content {
    padding: 10px;
  }
  
  .item-title {
    font-size: 1.2rem;
    margin-bottom: 5px;
    display: inline-block; /* Ensure the title width is measured correctly */
    background: transparent; /* Make the title background transparent */
    position: relative; /* Required to adjust z-index */
    z-index: 2; /* Set the title above the rectangle */
  }
  .title-container {
  position: relative;
  display: inline-block;
}
  .rectangleTitle {
  height: 50px;
  background-color: #bebebe8a; /* Adjust the color as needed */
  position: absolute;
  bottom: -10px; /* Position the rectangle beneath the title */
  margin: 10px;
  left: -10px;
  z-index: 1; /* Set the rectangle below the title */
    }


  .description-container {
  position: relative;
  }
  .item-description {
    font-size: 1rem;;
    margin-top: 30px;
    display: inline-block; /* Ensure the title width is measured correctly */
    background: transparent; /* Make the title background transparent */
    position: relative; /* Required to adjust z-index */
    z-index: 2; /* Set the title above the rectangle */
  } 
  .rectangleDescription {
  height: 50px;
  background-color: #bebebe8a; /* Adjust the color as needed */
  position: absolute;
  bottom: -10px; /* Position the rectangle beneath the title */
  margin: 10px;
  left: -10px;
  z-index: 1; /* Set the rectangle below the title */
    }

  /* Media query for responsiveness */
@media (max-width: 767px) {
  .item {
    width: 100%; /* Set width to 100% on small screens */
  }
}
@media (min-width: 768px) and (max-width: 1023px) {
  .item {
    width: 65%; /* Set width to 45% on medium-sized screens */
  }
}
@media (min-width: 1024px) {
  .item {
    width: 45%; /* Set width to 30% on larger screens */
  }
}
  </style>