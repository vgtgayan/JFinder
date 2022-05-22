$(function(){

    jiralink = 'https://jira.internal.synopsys.com/issues/?jql='

    chrome.storage.sync.get("autoFill", function (data) {
        $('#autoFill').prop('checked',data.autoFill);
    });


    $('#autoFill').on('change',function(){
        chrome.storage.sync.set({"autoFill":$('#autoFill').prop('checked')}, function () {
        });
    });


    $('#about').click(function() {
        chrome.tabs.create({
            url: "about.html"
        });
    });


    $('#search').click(function() {

        txt = $('#search_box').val();
        mx = $('#mx').val();

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
            table = '<table><tr class="clickable-row" data-href="'+jiralink+'" ><th >Key</th><th>Summary</th></tr>' + table + '</table>'
            

            $('#data_table').empty();
            $('#data_table').append(table);
            $('#data_table').show();


            $(".clickable-row").click(function() {
                window.open( $(this).data("href"), '_blank');
            });
            
        });
    });
});