function initMap(){
    var map = new GMaps({
        div: '#map',
        lat: 47.245384,
        lng: 5.989679
    });

    map.addMarker({
        lat: 47.245384,
        lng: 5.989679,
        title: "Nanomedicine Laboratory",
        click: function(e) {
            alert('clicked marker!');
        }
    });
    map.setZoom(16);
}
