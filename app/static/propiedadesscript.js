
/* *** funcion locali
*/
var map = null
function localizacion() {
  mapboxgl.accessToken = 'pk.eyJ1Ijoid2FyaW9tdmMiLCJhIjoiY2wyZXJ6NXdvMDA4YTNqbXdsOXJxNnloYiJ9.mjiy2sqN-nB0DIKp9LZpkQ';
  map = new mapboxgl.Map({
    container: 'mapbox',
    style: 'mapbox://styles/mapbox/outdoors-v11',
    center: [-104.458801, 24.778616],
    attributionControl: true,
    zoom: 14,
  });
  map.addControl(new mapboxgl.NavigationControl());
  console.log(map)

}


function setMarcadoresPopups(propiedades, imagenes) {


  let marcadores = []
  let coordenadas = []
  propiedades.forEach(function (prop, i) {
    i = imagenes.findIndex((e) => prop['id'] == e['id_propiedad'])
    if (i != -1) {
      url_pic = imagenes[i].url
    }
    else { url_pic = "" }
    var popup = new mapboxgl.Popup({
      offset: 25,
      closeButton: false,
      closeOnMove: true,
      className: "popupclass"
    })
      .setHTML("<strong>" + prop['whq'] + "</strong><br>" + prop['nombre'] + "<br>" + prop['titulo'] + ": " + prop['frase'] +
        "<img src='./static/galeria/" + url_pic + "'></img>");
    //console.log("i: "+prop['id']);
    
    
    i = imagenes.findIndex((e) => prop['id'] == e['id_propiedad'])
    console.log("i= " + i)
    if (i != -1) {
      //console.log("Imagen:" + imagenes[i].url);
    }
    console.log(prop['id']);
    const xMarker = new mapboxgl.Marker().setLngLat([parseFloat(prop['longitud']), parseFloat(prop['latitud'])]).setPopup(popup).addTo(map);
    let info = xMarker.getElement();
    info.addEventListener('click',()=>{
      let t = document.getElementById('infoPropiedad');
      infoPropiedad = getInfoPropiedaById(prop['id']);
      console.log(infoPropiedad);
      t.innerHTML= "<h3>"+infoPropiedad[0]['titulo'] + "</h3> "+infoPropiedad[0]['nombre']+"<br><br><h4>"+infoPropiedad[0]['frase']+"</h4>"+
      "<br><strong>Servicios: </strong>"+infoPropiedad[0]['servicios']+"<br>"+
      infoPropiedad[0]['lugares']+
      "<br><br><a href='./"+prop['id']+"/show'>más información...</a>"
    })
    marcadores.push(xMarker)
    coordenadas.push([parseFloat(prop['longitud']), parseFloat(prop['latitud'])])
  });



  let bounds = coordenadas.reduce(function (bounds, coord) {
    console.log("Bounds: " + bounds);
    console.log("Coordenadas:" + coord);
    return bounds.extend(coord);
  }, new mapboxgl.LngLatBounds(coordenadas[0], coordenadas[0]));

  console.log(bounds)
  map.fitBounds(bounds, {
    padding: 50,
    linear: true,
  })

}

function getInfoPropiedaById(id){
  let res = $.ajax({
    url: "/getinfobyid/"+id,
    type: "POST",
    async: false,
    contentType: "application/json"
  })
  infoPropiedad = JSON.parse(res.responseText);
  return infoPropiedad;
}



function getUbicacionesSuccess(resultado) {
  console.log(resultado);
  jreturn = $.ajax({
    url: "/getimagenes",
    type: "POST",
    async: false,
    contentType: "application/json"
  })
  imagenes = JSON.parse(jreturn.responseText);
  console.log(imagenes)
  colocar_marcadores(resultado, imagenes);

}


window.onload = function  () {
  console.log("Windows.load cargado");
  json_ubicaciones_propiedades = $.ajax({
    url: "/getubicaciones",
    type: "POST",
    contentType: "application/json",
    async: false,

  });
  json_imagenes_propiedades = $.ajax({
    url: "/getimagenes",
    type: "POST",
    async: false,
    contentType: "application/json"
  })
  objImagenes = JSON.parse(json_imagenes_propiedades.responseText);
  objPropiedades = JSON.parse(json_ubicaciones_propiedades.responseText);
  localizacion();
  setMarcadoresPopups(objPropiedades, objImagenes)




}

