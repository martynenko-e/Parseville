/* Google API for Map */

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
        map = new google.maps.Map(mapId, mapOptions),
        labels = 'ABCDEFGIJKLMNOPQRSTUVWXYZ';

    var markers = globalMarkers.map(function (marker, i) {
        console.log(marker);
        return new google.maps.Marker({
            position: {
                lat: marker.lat,
                lng: marker.lng
            },
            label: labels[i % labels.length]
        });
    });

    let markerCluster = new MarkerClusterer(map, markers,
        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});

    map.fitBounds(markers);


    //todo create event listeners onDruged and onZommChanged (smthing like that)..firstly create fundtions itself with "Draft data" (min and max lat lng) to be viewed in console
    //zoom_changed
    //drag
    map.addListener('zoom_changed', function () {
        // // 3 seconds after the center of the map has changed, pan back to the
        // // marker.
        // window.setTimeout(function () {
        //     map.panTo(marker.getPosition());
        // }, 3000);
    });
    map.addListener('drag', function () {
        // // 3 seconds after the center of the map has changed, pan back to the
        // // marker.
        // window.setTimeout(function () {
        //     map.panTo(marker.getPosition());
        // }, 3000);
    });
}
