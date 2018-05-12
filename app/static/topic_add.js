/*global $, console, alert*/

$(function () {
    'use strict';
    $("form").submit(function (event) {
        event.preventDefault();
        var topicTitle = $("input[name='title']").val(),
            topicContent = $("input[name='content']").val(),
            urlhome = '/',
            topicData = {
                "title": topicTitle,
                "content": topicContent
            };
        
        
        
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
            type: "POST",
            url: "/api/topic/add",
            data: JSON.stringify(topicData),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) {
                console.log('done');
                callPage(urlhome);
            }
        });
        
        
        
        


    });
});