/*global $, console, alert*/
$(function () {
    'use strict';
    
    $(".delete_button").click(function (event) {
        
        event.preventDefault();
        var lin_show = $(this).attr('href'),
            url1 = "/api" + lin_show;

        console.log(lin_show);
        console.log(url1);
        $(this).parents('tr').remove();
        $.ajax({
            type: "DELETE",
            url: url1,
            success: function (response) {
                alert("Added topic successfully !");
            }
        });


    });
});






$(function () {
    'use strict';
    function callPage(pagereinput) {
        
        $.ajax({
            url: pagereinput,
            type: "GET",
            dataType: 'text',
            success: function (response) {
                $('body').html(response);
                
            }
        });
    }
    $('a').on('click', function (e) {
        e.preventDefault();
        var pagRe = $(this).attr('href');
        callPage(pagRe);
    });
    

    
});

