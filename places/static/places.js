// This part could not be completed at time.

function initMap() { 
  let defaultMapOptions = { 
    center: 'latutude = 41 , longitude  = 29', 
    zoom: 6,
  } 
  map = new google.maps.Map(document.getElementById('map'), defaultMapOptions);

  mapMarker = new google.maps.Marker({
      position: defaultcoordinates,
      map: map
  });
}