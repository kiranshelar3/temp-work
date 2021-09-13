$(document).ready(function () {

    console.log("im in new file now");

    // $('selector').action() syntax
    // function for single click 
    $('p').click(function () {
        console.log('you clicked on p', this);
    })

    // function for double click   
    // element selector    
    $('p').dblclick(function () {
        console.log('you double clicked on p');
    })

    // for hover function  
    // $('p').hover(function(){
    // console.log('you hover on p')
    // },
    // function (){
    // console.log("thanks for coming")
    // })

    // id selector 
    $('#second').click(function () {
        console.log('clicked on second para by id selector');
    })

    // Events in jQuery
    // Mouse events = click, dblclick, mouseenter, mouseleave
    // KeyboardEvent = keypress, keydown, MediaKeyStatusMap
    // form events = submit, change, focus, blur
    // document/window events = load, resize, scroll, unload
    // there are three main types of selectors in jQuery 
    // 1. element selector
    // 2. id selector
    // 3. class selector
    // other selectors
    // $('*').click() // clicks on all the elements
    // $('p.odd').click() // clicks on all the elements
    // $('p:first').click() // clicks on all the elements


    // class selector for hiding
    $('.jar').click(function () {
        $('.jar').hide();
    })

    // the on() is an inbuilt method in jQuery which is used to attach one or more event handlers for the selected elements and child elements in the DOM tree.

    $('p').on(
        {
            click: function () {
                console.log('mouse-in');
            },
            mouseleave: function () {
                console.log('mouseleave');
            }
        })

    // hide and show function hides hide/show done in specified time 
    // $('#info').hide(12000, function () {
        // console.log("hidden");
    // })
    // $('#info').show(10000, function () {
        // console.log("show");
    // })

    //fadeIn()
    // fadeOut()
    // fadeToggle()
    // fadeTo()

    $("#but").click(function () {
    $('#info').fadeOut(4000);
    })

    // Slide methods - speed and callback parameters are optional
    // $('#wiki').slideUp(1000, function(){
    //     console.log('done');
    $('#info').slideUp();
    $('#info').slideDown(2000);
    // $('#info').slideToggle(2000);

    // animate function in jquery
    $('#info2').animate({
        opacity: 0.5,
        height:'150px',
        width: '550px',
    },"fast")

 // $('#wiki').animate({ opacity: 0.3 }, 4000);
    // $('#wiki').animate({ opacity: 0.9 }, 1000);
    // $('#wiki').animate({ width: '350px' }, 12000);

    $('#info').css('background-color', 'red')

})
