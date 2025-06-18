$(function ()  {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        language: {
            url: "//cdn.datatables.net/plug-ins/1.10.21/i18n/Spanish.json"
        },
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {'data': 'zone'},
            {'data': 'temperature_inf'},
            {'data': 'humidity_inf'},
            {'data': 'id'},
        ],
        columnDefs: [
            {
                targets: [0],
                class: 'td-actions text-center'
            },
            {
                 targets: [1],
                 className: 'td-actions text-center',
                 render: function (data, type, row) {
                     return row['temperature_inf'] + ' - ' +row['temperature_sup'] + ' °C';
                 }
             },
            {
                 targets: [2],
                 className: 'td-actions text-center',
                 render: function (data, type, row) {
                     return row['humidity_inf'] + ' - ' +row['humidity_sup'] + ' %';
                 }
             },
            {
                targets: [3],
                class: 'td-actions text-center',
                orderable: false,
                render: function (data, type, row) {
                    let edition
                    edition = '<a href="/update/' + row.id + '/" type="button" rel="tooltip" class="btn btn-info btn-xs btn-just-icon btn-simple"><i class="material-icons">edit</i</a>';
                    return edition;
                }
            },
            // {
            //     targets: [-2],
            //     className: 'td-actions text-center',
            //     render: function (data, type, row) {
            //         var estado = null
            //         switch (row.is_active) {
            //             case true:
            //                 estado = 'Activo'
            //                 break;
            //             case false:
            //                 estado = 'Inactivo'
            //                 break;
            //         }
            //         return estado;
            //     }
            // },
        ],
        initComplete: function (settings, json) {
        }
    });
});