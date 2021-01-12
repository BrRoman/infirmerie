$(document).ready(function () {
    url = new URL(window.location);

    // Agenda: click on 'previous week':
    $('#previous_week').click(function () {
        regex = /agenda\/(\d{2})\/(\d{2})\/(\d{4})/;
        result = regex.exec(url);
        date = new Date(parseInt(result[3]), parseInt(result[2]) - 1, parseInt(result[1]));
        previous_date = new Date(date.getTime() - (7 * 24 * 3600 * 1000));

        previous_day = previous_date.getDate();
        previous_day = previous_day < 10 ? '0' + previous_day : previous_day;

        previous_month = previous_date.getMonth() + 1;
        previous_month = previous_month < 10 ? '0' + previous_month : previous_month;

        previous_year = previous_date.getYear() + 1900;

        window.location.href = '/infirmerie/billets/agenda/' + previous_day + '/' + previous_month + '/' + previous_year;
    });


    // Agenda: click on 'next week':
    $('#next_week').click(function () {
        regex = /agenda\/(\d{2})\/(\d{2})\/(\d{4})/;
        result = regex.exec(url);
        date = new Date(parseInt(result[3]), parseInt(result[2]) - 1, parseInt(result[1]));
        next_date = new Date(date.getTime() + (7 * 24 * 3600 * 1000));

        next_day = next_date.getDate();
        next_day = next_day < 10 ? '0' + next_day : next_day;

        next_month = next_date.getMonth() + 1;
        next_month = next_month < 10 ? '0' + next_month : next_month;

        next_year = next_date.getYear() + 1900;

        window.location.href = '/infirmerie/billets/agenda/' + next_day + '/' + next_month + '/' + next_year;
    });


    // Agenda's calendar:
    $('#datepicker').datetimepicker({
        format: 'L',
    });
    $('#datepicker').on('hide.datetimepicker', function (e) {
        date = e.date._d;
        day = date.getDate();
        day = day < 10 ? '0' + day : day;
        month = date.getMonth() + 1;
        month = month < 10 ? '0' + month : month;
        year = date.getYear() + 1900;
        window.location.href = '/infirmerie/billets/agenda/' + day + '/' + month + '/' + year;
    });


    // List of toubibs: search (fired on "Enter"):
    $('#search_input').keyup(function (key) {
        if (key.keyCode == 13) {
            search = $('#search_input').val();
            if (search == ''){
                window.location.href = '/infirmerie/toubibs/page=1';
            }
            else{
                window.location.href = '/infirmerie/toubibs/search=' + search + '/page=1';
            }
        }
    });
});