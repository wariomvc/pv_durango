/* var mapa_dinamico = document.querySelector('.mapa');
var mapa_estatico = document.querySelector('.mapa_estatico');
var contenedor_mapa = document.querySelector('.contenedor_mapa')



function mostrar_mapa() {
    console.log("Se eejcuto mostrar mapa")
    contenedor_mapa.style.visibility = 'visible'
    contenedor_mapa.style.display = 'inline'

}
function ocultar_mapa(e) {
    console.log(e.target)
    if(e.target.className == 'contenedor_mapa')
    {
        contenedor_mapa.style.visibility = 'hidden'
        contenedor_mapa.style.display = 'none'
    }
    
}
mapa_estatico.addEventListener("click", mostrar_mapa)
contenedor_mapa.addEventListener("click", ocultar_mapa);

console.log(contenedor_mapa)
console.log(mapa_dinamico)
console.log(mapa_estatico)


$(document).ready(function() {
    $('a[href^="#"]').click(function() {
      var destino = $(this.hash);
      if (destino.length == 0) {
        destino = $('a[name="' + this.hash.substr(1) + '"]');
      }
      if (destino.length == 0) {
        destino = $('html');
      }
      $('html, body').animate({ scrollTop: destino.offset().top }, 500);
      return false;
    });
  }); */

  