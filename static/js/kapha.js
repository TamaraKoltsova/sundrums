$(document).ready(function(){
    // находим форму
    var form = $('#kapha_test');
    //выводим в консоль должно высветится:  a.fn.init [form#password_test.form-inline]
    console.log(form);
    
    
    
    
    //функция для rendom
    function myRandom (from,to){
    return Math.floor(Math.random()*(to - from + 1)+from);
}
var rand = myRandom(0,50);
var rand2 = myRandom(0,10);
var resalt = rand + rand2 
 
 $('.two_number').html(rand+' и '+rand2+' (подсказка это равно '+ resalt+')')
//document.write(' первое число: ',  rand , ' второе число: ', rand2, ' их сумма: ' , resalt);
    
    
    
    // назначаем действие на отправку 
    form.on('submit', function(e){ //e блокируем перезагрузку
        e.preventDefault();
        //alert(rand);
        var password_from_input = $('#answer').val();
        var submit_btn = $('#submit_btn');
        var password_from_bd = rand;
        
        console.log(password_from_input);
        if (password_from_input == resalt){$('#add_button').html('<button  type="submit">отправить сообщение</button>');
        alert('сложено правильно, вы можете отправлять сообщение');
        $('.kapha_test').addClass('del');

        }
        else {alert('не верно попробуйте еще раз');}
        });
        
});