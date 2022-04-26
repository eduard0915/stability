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
            {'data': 'code_product'},
            {'data': 'description_product'},
            {'data': 'brand_product'},
            {'data': 'sanitary_license'},
            {'data': 'product_enabled'},
            {'data': 'product_enabled'},
        ],
        columnDefs: [
            {
                targets: [5],
                class: 'td-actions text-center',
                orderable: false,
                render: function (data, type, row) {
                    let product
                    product = '<a href="/products/update/'+row.id+'/" type="button" rel="tooltip" class="btn btn-warning btn-round"><i class="material-icons">edit</i></a>&nbsp';
                    product +='<a href="/products/detail/'+row.id+'/" type="button" rel="tooltip" class="btn btn-info btn-round"><i class="material-icons">info_outline</i></a></a>';
                    return product
                }
            },
            {
                targets: [1],
                class: 'td-actions text-center',
                render: function (data, type, row) {
                    return row.description_product + ' ' +row.pharma_form+ ','+' '+row.presentation_prod;
                }
            },
            {
                targets: [0,2,3],
                class: 'td-actions text-center'
            },
            {
                targets: [4],
                className: 'td-actions text-center',
                render: function (data, type, row) {
                    var estado = null
                    switch (row.product_enabled) {
                        case true:
                            estado = 'Activo'
                            break;
                        case false:
                            estado = 'Inactivo'
                            break;
                    }
                    return estado;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});