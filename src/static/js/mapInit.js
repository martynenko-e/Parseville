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

    markers = markersFromOffices(globalMarkers, addInfoWindow());

    /*for (var i = 0; i < markers.length; i++) {
        google.maps.event.addListener(markers[i], 'click', function () {
            addInfoWindow().open(map, markers[i]);
        })
    }*/

    let markerCluster = new MarkerClusterer(map, markers,
        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});

    map.fitBounds(boundMap(globalMarkers));

    map.addListener('zoom_changed', function () {
        /*console.log('zoom');
         // границы карты 1 точки по диагонали
         console.log(map.getBounds().getNorthEast().lat());
         console.log(map.getBounds().getNorthEast().lng());
         // границы карты 2 точки по диагонали
         console.log(map.getBounds().getSouthWest().lat());
         console.log(map.getBounds().getSouthWest().lng());*/
    });

    map.addListener('dragend', function () {

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

function addInfoWindow(obj) {
    console.log(obj);
    var infoWindow = {};
    var sContent = '<h2>' + obj.company + '</h2>' +
        '<bt/>' +
        '<p>' +
        obj.phone + ' ' +
        '<bt/>' +
        obj.name + ' ' +
        '<bt/>' +
        obj.address +
        '</p>';
    infoWindow = new google.maps.InfoWindow({
        content: sContent
    });

    return infoWindow;
}

function markersFromOffices(officesArray, func) {
    return officesArray.map(function (marker) {
        return new google.maps.Marker({
            position: {
                lat: marker.lat,
                lng: marker.lng
            },
            info: func(marker)
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