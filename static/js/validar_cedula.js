
var div = document.createElement("div");  // Create with DOM
div.setAttribute('style', 'display:none; color:red;');
div.setAttribute('id', 'div_msg');
div.setAttribute('maxlength', '10');
div.setAttribute('pattern', '\\d{10}');
$('#id_cedula').after(div);

function validar(cedula, e) {
	var cad = document.getElementById(cedula).value.trim();
	var total = 0;
	var longitud = cad.length;
	var longcheck = longitud - 1;

	if (cad !== "" && longitud === 10){
		for(i = 0; i < longcheck; i++){
			if (i%2 === 0) {
				var aux = cad.charAt(i) * 2;
				if (aux > 9) aux -= 9;
				total += aux;
			} else {
              total += parseInt(cad.charAt(i)); // parseInt o concatenará en lugar de sumar
          }
      }

      total = total % 10 ? 10 - total % 10 : 0;

      if (cad.charAt(longitud-1) == total) {
      	console.log('Cedula Valida');
        e.preventDefault();
      	// document.getElementById("salida").innerHTML = ("Cedula Válida");
      }else{
      	console.log('Cedula InValida');
      	$('#div_msg').text('Cedula Invalida');
    	$('#div_msg').show(500);
    	$( "#btn_guardar" ).prop( "disabled", true );
        e.preventDefault();
      	// document.getElementById("salida").innerHTML = ("Cedula Inválida");
      }
  }
}
$("#id_cedula").keydown(function (e) {
    	$('#div_msg').hide(500);
    	$( "#btn_guardar" ).prop( "disabled", false );

        // Allow: backspace, delete, tab, escape, enter and .
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
             // Allow: Ctrl/cmd+A
            (e.keyCode == 65 && (e.ctrlKey === true || e.metaKey === true)) ||
             // Allow: Ctrl/cmd+C
            (e.keyCode == 67 && (e.ctrlKey === true || e.metaKey === true)) ||
             // Allow: Ctrl/cmd+X
            (e.keyCode == 88 && (e.ctrlKey === true || e.metaKey === true)) ||
             // Allow: home, end, left, right
            (e.keyCode >= 35 && e.keyCode <= 39)) {
                 // let it happen, don't do anything
                 return;
        }
        // Ensure that it is a number and stop the keypress
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
        	$('#div_msg').text('Solo numeros por favor');
        	$('#div_msg').show(500);
            e.preventDefault();
        }

        // Validamos que sean solo 10 digitos
        var cedula = $(this).val();
        if (cedula.length > 9) {
        	console.log('No permitido');
        	$('#div_msg').text('Solo 10 digitos');
        	$('#div_msg').show(500);
	    	$( "#btn_guardar" ).prop( "disabled", true );
        	
        }

    });