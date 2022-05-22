$(function () {

    

    chrome.runtime.onMessage.addListener(
        function (request, sender, sendResponse) {
            if (request.action == "fillForm") {
                fillForm();
            }
        }
    );


    function fillForm() {

        if ($('.jira-dialog-heading>h2').text() == "Create Issue") {
            $('#summary').focusout(function () {

                txt = $('#summary').val();
                
                mx = 5;
                if (txt.length > 5) {
					
                    
                    $.get("http://127.0.0.1:5000/get_jira/"+txt+"/"+mx, function(data, status){

                       
                        url='https://jira.internal.synopsys.com/issues/?jql=key in('
                        table = ''
                
                        data.forEach(element => {
                            table += '<tr class="clickable-row" data-href="https://jira.internal.synopsys.com/browse/'+element.key+'"> \
                                    <td>'+element.key+'</td> \
                                    <td>'+element.summary+'</td> \
                                    </tr>'
                            url += element.key + ',' ;
                            
                        });
                
                        jiralink = url.replace(/.$/,")")
                        table = '<table><tr class="clickable-row" data-href="'+jiralink+'"><th>Key</th><th>Summary</th></tr>' + table + '</table>'
                
                        $('#simmilerissues').remove();
                        $('.content > :first-child').after('<div id="simmilerissues" class="field-group">   \
                        <label style="color: green;"> Simmiler Issues </label>\
                        <div style=" width: 100%;"> \
                        <style>\
                        table {\
                        font-family: arial, sans-serif;\
                        border-collapse: collapse;\
                        width: 100%;\
                        }\
                        \
                        td, th {\
                        border: 1px solid #dddddd;\
                        text-align: left;\
                        padding: 8px;\
                        }\
                        \
                        tr:nth-child(even) {\
                        background-color: #dddddd;\
                        }\
                        </style>'
                        +table+ 
                            '</div>\
                        \
                        </div>' );


                        $(".clickable-row").click(function() {
                            window.open( $(this).data("href"), '_blank');
                        });
                        
                      });
                    
                }

            });


        } else {

            chrome.storage.sync.get("autoFill", function (data) {
                if (!data.autoFill) { alert("You havent Open Jira Create Form") }
            });

        }

    }







});