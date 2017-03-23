/* Google API for Map */

function initMap() {

    let uluru = {
            lat: 50.4501,
            lng: 30.5234
        },
        mapOptions = {
            zoom: 15,
            scrollwheel: false,
            center: uluru,
            fullscreenControll: true
        },
        map = new google.maps.Map(document.getElementById('map'), mapOptions),
        labels = 'ABCDEFGIJKLMNOPQRSTUVWXYZ';


    var markers = filteredMark.map(function (location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    let markerCluster = new MarkerClusterer(map, markers,
        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});








    // abruvgalp
    var mapEventOnClick = document.getElementById('map');
    mapEventOnClick.onclick = function () {
        let url = "http://localhost:8000/api/office/";
        showMoreEvent(url);
    };
}
