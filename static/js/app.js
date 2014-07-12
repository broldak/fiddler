$(document).ready(function(){
  $('#create-event-nav').on('click', function(evt){
    evt.stopPropagation();
    $('#create-event-popup').addClass('active');
    $('#create-event-popup, #create-event-input').on('click', function(evt){
      evt.stopPropagation();
    });
    $('body').on('click', function(){
      $('#create-event-popup').removeClass('active');
    });
  });

  $('#add-a-video').on('click', function(evt){
    evt.stopPropagation();
    $('#upload-video-popup').addClass('active');
    $('#upload-video-popup').on('click', function(evt){
      evt.stopPropagation();
    })
    $('body').on('click', function(){
      $('#upload-video-popup').removeClass('active');
    })
  });

  $('#add-video-btn').on('click', function(evt){
    evt.preventDefault();
    $.ajax({url: $('#upload-video-form').attr('action'), data:$('#upload-video-form').serialize()});
  })
});