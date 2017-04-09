/* Google API for Map */
'use strict';
var markers = [];

function initMap() {
    // as prior task is to query server in order to fill in GlobalMarkets(Array of JSON Objects) with a values
    $.ajax({
        url: window.location.protocol + '//' + window.location.hostname + ":" + window.location.port + '/api/office/',
        type: 'post',
        dataType: 'json',
        cache: false,
        success: postProcessing,
        async: false
    });

    // variables
    var uluru = {
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
        map = new google.maps.Map(mapId, mapOptions),
        infowindow = null;

    // converting Array of JSON objects to Array of Google API Marker objects
    markers = markersFromOffices();

    // info Window google API for each Marker (infowindow is empty for now.....)
    for (var i = 0; i < markers.length; i++) {
        var marker = markers[i];
        console.log('---------------------------------------------------> marker');
        console.log(marker);
        var sContent = '<div class="marker-info">' +
            '<p>' + globalMarkers[i].company +
            '</br>' +
            globalMarkers[i].phone +
            '</br>' +
            globalMarkers[i].name +
            '</br>' +
            globalMarkers[i].address +
            '</p>' + '</div>';
        console.log('-----------------------------------------------------------------> S Content below');
        console.log(sContent);

        infowindow = new google.maps.InfoWindow({
            // its empty for some reason
            content: sContent
        });

        google.maps.event.addListener(marker, 'click', function () {
            infowindow.setContent(this.html);
            infowindow.open(map, this);
        });
    }

    let markerCluster = new MarkerClusterer(map, markers,
        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});

    //pass map into function is necessity otherwise it takes 'map' as come class from Python
    AutoCenter(map);

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

function AutoCenter(map) {
    var bounds = new google.maps.LatLngBounds();
    $.each(markers, function(index, marker) {
        bounds.extend(marker.position);
    });
    map.fitBounds(bounds);
}

//agree that we need this function????
function getBoundsOfMap() {
    return new google.maps.LatLngBounds({
        lat: 50.4501,
        lng: 30.5234
    });
}

/*function addInfoWindow(obj) {
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
 }*/

function markersFromOffices() {
    return globalMarkers.map(function (marker) {
        return new google.maps.Marker({
            position: {
                lat: marker.lat,
                lng: marker.lng
            }
        });
    });
}
// check wtf below
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
//future functionality. Disabled for now
function clearMarkers(markers) {
    if (markers) {
        for (var i = 0; i < markers.length; i++) {
            markers[i].setMap(null);
        }
    }
    markers.length = 0;
}