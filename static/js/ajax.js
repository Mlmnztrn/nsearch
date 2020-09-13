$('#button').on('click', function(){
    $('#resultGET').html('<div class="s">検索中...</div>');
    // Ajax通信を開始

    //menuの格納先へのアクセス
    const selected_menu = document.input_form.menu;
    console.log(selected_menu);
    const selected_pref = document.input_form.pref;
    console.log(selected_pref);

    
    //インデックス取得
    const selected_menu_index = selected_menu.selectedIndex; //そのとき選択されているインデックス番号
    console.log(selected_menu_index);
    const selected_pref_index = selected_pref.selectedIndex; //そのとき選択されているインデックス番号
    console.log(selected_pref_index);
    
    //インデックスを使ってvalueを取得
    const selected_menu_value = selected_menu.options[selected_menu_index].value;　//選択されているインデックスに対応するvalue
    console.log(selected_menu_value);
    const selected_pref_value = selected_pref.options[selected_pref_index].value;　//選択されているインデックスに対応するvalue
    console.log(selected_pref_value);
    


    $.ajax({
        url: '/exec/',
        method: "GET",
        // プレーンテキストを受信
        dataType: 'text',
        // リクエストパラメータ
        data: {
            menu : selected_menu_value,
            pref : selected_pref_value
            
        },
        timeout: 5000,
        
    })
    
    .done(function(data) {
        // 通信成功時の処理を記述
        $('#resultGET').html(data);
    })
    .fail(function(data) {
        // 通信失敗時の処理を記述
        $('#resultGET').html(data);
    });

});

