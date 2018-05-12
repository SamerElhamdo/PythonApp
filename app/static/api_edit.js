/*global $, console, alert*/

$(function () {
    'use strict';
    $("form").submit(function (event) {
        event.preventDefault();
        var topicTitle = $("input[name='title']").val(),
            topicContent = $("input[name='content']").val(),
            topiceditID = $(this).attr('action').slice(-1),
            urlhome = '/',
            topicData = {
                "title": topicTitle,
                "content": topicContent
            };
        console.log(topiceditID);
        
        
        
      // function SPA-----------------------------------------------------  
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
     // function SPA-----------------------------------------------------  
        
        
        $.ajax({
            type: "PUT",
            url: "/api/topic/update/" + topiceditID,
            data: JSON.stringify(topicData),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) {
                console.log(topiceditID);
                callPage(urlhome);
            }
        });
        
        
        
        


    });
});