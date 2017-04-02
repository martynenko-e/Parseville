/* Google API for Map */

var markers = [];

function initMap() {
    $.ajax({
        url: window.location.protocol + '//' + window.location.hostname + ":" + window.location.port + '/api/office/',
        type: 'post',
        dataType: 'json',
        cache: false,
        success: postProcessing,
        async: false
    });

    let uluru = {
            lat: 50.4501,
            lng: 30.5234
        },
        mapId = document.getElementById('map'),
        mapOptions = {
            zoom: 10,
            scrollwheel: false,
            center: uluru,
            fullscreenControll: true
        },
        map = new google.maps.Map(mapId, mapOptions);

    markers = markersFromOffices(globalMarkers);

    let markerCluster = new MarkerClusterer(map, markers,
        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});

    map.fitBounds(boundMap(globalMarkers));

    //todo create event listeners onDruged and onZommChanged (smthing like that)..firstly create fundtions itself with "Draft data" (min and max lat lng) to be viewed in console

    map.addListener('zoom_changed', function () {
        console.log('zoom');
        // границы карты 1 точки по диагонали
        console.log(map.getBounds().getNorthEast().lat());
        console.log(map.getBounds().getNorthEast().lng());
        // границы карты 2 точки по диагонали
        console.log(map.getBounds().getSouthWest().lat());
        console.log(map.getBounds().getSouthWest().lng());
    });

    map.addListener('dragend', function () {
        console.log('dragend');
        // // 3 seconds after the center of the map has changed, pan back to the
        // // marker.
        // window.setTimeout(function () {
        //     map.panTo(marker.getPosition());
        // }, 3000);
    });
}

function boundMap(officesArray) {
    var bounds = getBoundsOfMap();
    for (var key in officesArray) {
        var latLng = new google.maps.LatLng(officesArray[key].lat, officesArray[key].lng);
        bounds.extend(latLng);
    }
    return bounds;
}

function getBoundsOfMap() {
    return new google.maps.LatLngBounds({
        lat: 50.4501,
        lng: 30.5234
    });
}

function markersFromOffices(officesArray) {
    return officesArray.map(function (marker) {
        return new google.maps.Marker({
            position: {
                lat: marker.lat,
                lng: marker.lng
            }
        });
    });
}

function fetchNewBounds(neLat, neLng, swLat, swLng) {
    $.ajax({
        url: window.location.protocol + '//' + window.location.hostname + ":" + window.location.port + '/api/get/office/',
        type: 'post',
        dataType: 'json',
        data: {
            neLat: neLat,
            neLng: neLng,
            swLat: swLat,
            swLng: swLng
        },
        cache: false,
        success: postProcessing,
        async: true
    });
}

function clearMarkers(markers) {
    if (markers) {
        for (var i = 0; i < markers.length; i++) {
            markers[i].setMap(null);
        }
    }
    markers.length = 0;
}