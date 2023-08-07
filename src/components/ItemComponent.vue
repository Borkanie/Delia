<template>
    <div class="item">
      <div class="item-image" :style="{ backgroundImage: 'url(' + backgroundImage + ')' }">
        <div class="item-content">
            <div class="title-container" ref="titleContainer">
                <div class="rectangleTitle" :style="{ width: rectangleTitleWidth + 'px' }"></div>
                <h3 class="item-title" ref="itemTitle">{{ title }}</h3>               
            </div>
            <div class="description-container" ref="descriptionContainer">
                <div class="rectangleDescription" :style="{ width: rectangleDescriptionWidth + 'px' }"></div>
                <p class="item-description" ref="itemDescription">{{ description }}</p>             
            </div>            
        </div>
    </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'ItemComponent',
    props: {
      backgroundImage: {
        type: String,
        required: true,
      },
      title: {
        type: String,
        required: true,
      },
      description: {
        type: String,
        required: true,
      },
    },
    data() {
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
    async searchEvents(locaiton,radius = 1000) {
      try {
        const accessToken = 'EAAChFqZAWohcBO41u9nUPGHCxCwuAHynyh12sFK7NbpQGdu8OiMYoaD3FjZCZC49YoZBBDtYCVenjvIYErSDjJ4oZBGRRZBiZA9WTB32iQSPQ7HokXkaLPf1Oa3edERVkFlWC3ZCkgNTSnpSy4Yay3FJV0pRqfUGXJYvVdREiZAG3cdDmNilIVotfB2fKAcbPr2ZCQRGOZBvzCc8Hhnez2CBLjZBxzHSzli7UZAGne9gLlicRhnYzX2gM9zM4kNxUHglPedqq8dZC9g0EZD'; // Replace with your Facebook access token
        var latitude;
        var longitude;
        if(this.isListOfTwoIntegers(locaiton))
        {
          latitude = location[0]; // Cluj's latitude
          longitude = location[1]; // Cluj's longitude
        }
        else{
          latitude = 46.7712; // Cluj's latitude
          longitude = 23.6236; // Cluj's longitude
        }
        
        const distance = radius;
        const keyword = 'music'; // You can change the keyword as needed

        const url = `https://graph.facebook.com/v17.0/search?type=event&q=${encodeURIComponent(
          keyword
        )}&center=${latitude},${longitude}&distance=${distance}&access_token=${accessToken}&limit=10&page=${this.page}`;

        const response = await axios.get(url);
        const data = response.data;

        if (data.data && data.data.length > 0) {
          this.events = [...this.events, ...data.data];
          this.page++;
        } else {
          this.hasMoreEvents = false;
        }
      } catch (error) {
        console.error('Error fetching events:', error);
      }
    },

    loadMore($state) {
      if (this.hasMoreEvents) {
        this.searchEvents();
        $state.loaded();
      } else {
        $state.complete();
      }
    },
    isListOfTwoIntegers(element) {
  if (!Array.isArray(element)) {
    return false;
  }

  if (element.length !== 2) {
    return false;
  }

  const [firstValue, secondValue] = element;

  if (
    typeof firstValue !== 'number' ||
    !Number.isInteger(firstValue) ||
    typeof secondValue !== 'number' ||
    !Number.isInteger(secondValue)
  ) {
    return false;
  }

  return true;
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