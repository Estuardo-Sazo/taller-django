    var idCliente=0;
    var idVehiculo=0;
    
    /* Campo de Busqueda de cliente  */
    $('#search').keyup(function() {
        let search=$('#search').val();

            /* Consulta a nuestra url */
        fetch('/clientes/q/'+search, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then((response) => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Request failed!');
        }, networkError => console.log(networkError.message))
        .then((data) => {
            let template='';
            let resp=data.clientes;
            resp.forEach(d => {
                let nombre=d.nombre+' '+d.apellido;
                template+=`
                <tr>
                    <td scope="col">${d.nombre}</td>
                    <td scope="col">${d.apellido}</td>
                    <td scope="col">${d.correo}</td>
                    <td scope="col"><a href="#" class="btn btn-info btn-circle btn-sm" onClick="getVehiculos(${d.id},'${nombre}')">
                        <i class="fas fa-edit"></i> Selectcionar
                    </a></td>
                </tr>
                
                `;
            });

            $('#lista').html(template);
        });
     
    });


    function getVehiculos(id,nombre){
        idCliente=id;
        $('#clienteNombre').html(nombre);

        fetch('/vehiculos/q/'+id, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then((response) => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Request failed!');
        }, networkError => console.log(networkError.message))
        .then((data) => {
            $('#card1').addClass('d-none');
            $('#card2').removeClass('d-none');

            console.log(data);

            let template='';
            let resp=data.vehiculos;
            resp.forEach(d => {
                template+=`
                <tr>
                    <td scope="col">${d.placa}</td>
                    <td scope="col">${d.modelo}</td>
                    <td scope="col">${d.color}</td>
                    <td scope="col">${d.linea}</td>
                    <td scope="col">${d.chasis}</td>
                    <td scope="col"><a href="#" class="btn btn-info btn-circle btn-sm" >
                        <i class="fas fa-edit"></i> Selectcionar
                    </a></td>
                </tr>
                
                `;
            });

            $('#lista2').html(template);
        });
    }


    $(document).on("click", ".listaClientes", function() {
        $('#card2').addClass('d-none');
        $('#card1').removeClass('d-none');
    })