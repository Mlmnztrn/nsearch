 $("form").on("click", "#comment_post", function() {
                let formdata = new FormData($('#form').get(0));
                var form = $(this);
                var csrf_token = getCookie("csrftoken");
                var rslt = window.confirm("Do you really want to do?");

                var image_file = document.getElementById("id_image").files[0];
                var text_data = document.getElementById("id_text").value;

                formdata.append("image_file", image_file);

                $('#resultPOST').text('通信中...');
                if (rslt) {
                    // Ajax通信を開始
                    $.ajax({
                        type: "post",
                        url: "post_comment/",
                        data: formdata,
                        timeout: 5000,
                        contentType: false,
                        processData: false,

                        // 送信前にヘッダにcsrf_tokenを付与。
                        beforeSend: function(xhr, settings) {
                            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                                xhr.setRequestHeader("X-CSRFToken", csrf_token);
                            }
                        }
                    })
                    .done(function(data) {
                        // 通信成功時の処理を記述
                        $('#resultPOST').text('POST処理成功：' + data);
                    })
                    .fail(function() {
                        // 通信失敗時の処理を記述
                        $('#resultPOST').text('POST処理失敗.');
                    });
                }
            });

            // csrf_tokenの取得に使う
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }


        $('.btn_close').click(function(){

            var huga = 0;
            var hoge = setInterval(function() {
                console.log(huga);
                huga++;
                //終了条件
                if (huga == 2) {
                clearInterval(hoge);
                create_comment_view();
                console.log("done");
                }
            }, 500);
           
                
        })
        