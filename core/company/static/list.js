$(function ()  {
    tblType = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        searching: false,
        paging: false,
        info: false,
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
            {'data': 'companyName'},
            {'data': 'companyNit'},
            {'data': 'companyAddress'},
            {'data': 'companyCity'},
            {'data': 'companyAddress'},
        ],
        columnDefs: [
            {
                targets: [4],
                orderable: false,
                className: 'td-actions text-center',
                render: function (data, type, row) {
                    return  '<a href="/company/update/' + row.id + '/" type="button" rel="tooltip" class="btn btn-warning btn-xs btn-just-icon btn-simple"><i class="material-icons">edit</i</a></a>';
                }
            },
            {
                targets: [3,2,1,0],
                className: 'td-actions text-center',
                orderable: false,
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});
