/* Google API for Map */
function initMap() {
    let uluru = {lat: 50.4501, lng: 30.5234};
    let map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        scrollwheel: false,
        center: uluru,
        fullscreenControll: true
    });
    let marker = new google.maps.Marker({
        position: uluru,
        map: map
    });
}