var d = document.getElementById("dibujito");
var lienzo = d.getContext("2d");
var texto = document.getElementById("lineas");
var botton = document.getElementById("boton");

botton.addEventListener("click", dibujoPorClick);

function dibujarLinea(color, xinicial, yinicial, xfinal, yfinal)
{
  lienzo.beginPath();
  lienzo.strokeStyle = color;
  lienzo.moveTo(xinicial,yinicial);
  lienzo.lineTo(xfinal,yfinal);
  lienzo.stroke();
  lienzo.closePath();
}


function contorno()
{
  dibujarLinea("black", 1,1,1,300);
  dibujarLinea("black", 1,299,299,299);
  dibujarLinea("black", 299,299,299,1);
  dibujarLinea("black", 1,1,299,1);

}

function dibujoPorClick()
{
  var lineas = parseInt(texto.value);
  var ancho = d.width;
  var l = 0;
  var yi,xf;
  for (l=0; l < lineas; l++) 
    {
      var espacio = parseInt(ancho/lineas);
      yi = espacio * l;
      xf = espacio * (l + 1);
      console.log(yi, xf);
      dibujarLinea("purple",0, yi, xf, 300); 
      dibujarLinea("purple",300, yi, xf, 0); 
      dibujarLinea("purple",300-xf, 0, 0, xf);
      dibujarLinea("purple",300, 300-xf, xf, 300);  
    }

  contorno();
  console.log(texto.value);
}



