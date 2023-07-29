<template>
  <div class="app" :style="{ backgroundImage: 'url(' + backgroundImage + ')' }">
    <div class="title-section">
      <h1>Welcome to My Awesome Website</h1>
      <p>Explore our amazing items below:</p>
    </div>

    <item-component
      v-for="item in items"
      :key="item.id"
      :background-image="item.image"
      :title="item.title"
      :description="item.description"
    />
  </div>
</template>

<script>
import ItemComponent from './components/ItemComponent.vue';

export default {
  name: 'App',
  components: {
    ItemComponent,
  },
  data() {
    return {
      items: [
        {
          id: 1,
          image: require('@/assets/t1.jpg'),
          title: 'Item 1',
          description: 'Description for Item 1',
        },
        {
          id: 2,
          image: require('@/assets/t2.jpg'),
          title: 'Item 2',
          description: 'Description for Item 2',
        },
        {
          id: 3,
          image: require('@/assets/t3.jpg'),
          title: 'Item 3',
          description: 'Description for Item 3',
        },
        {
          id: 4,
          image: require('@/assets/t4.jpg'),
          title: 'Item 4',
          description: 'Description for Item 4',
        },
      ],
    };
  },
};
</script>

<style>
.app {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  background-size: cover;
  background-position: center;
  padding-top: 60px; /* Add some top padding to create space for the title section */
}

.title-section {
  text-align: center;
  padding: 20px;
  color: #fff;
  background-color: rgba(0, 0, 0, 0.7); /* Add a semi-transparent background to the title section */
}

.title-section h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.title-section p {
  font-size: 1.2rem;
}

.items-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>