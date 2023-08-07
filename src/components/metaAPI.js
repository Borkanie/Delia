async function getEventsInArea(accessToken, latitude, longitude, distance = 1000, keyword = '') {
  try {
    const url = `https://graph.facebook.com/v12.0/search?type=event&q=${encodeURIComponent(keyword)}&center=${latitude},${longitude}&distance=${distance}&access_token=${accessToken}`;
    
    const response = await fetch(url);
    const data = await response.json();
    
    if (data.data && data.data.length > 0) {
      return data.data;
    } else {
      return [];
    }
  } catch (error) {
    throw new Error('Error fetching events: ' + error.message);
  }
}

// Usage example
const accessToken = 'YOUR_ACCESS_TOKEN'; // Replace with your Facebook access token
const latitude = 37.7749;
const longitude = -122.4194;
const distance = 1000;
const keyword = 'music';

getEventsInArea(accessToken, latitude, longitude, distance, keyword)
  .then(events => {
    console.log('Events found:', events);
  })
  .catch(error => {
    console.error('Error:', error);
  });
