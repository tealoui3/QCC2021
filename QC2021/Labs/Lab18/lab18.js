<script>
$(document).ready(function(){
  $("#start").click(function()){
      $("div").animate({left:'100px'}, 5000);
      $("div").animate({fontSize:'3em'}, 5000);
  });

  $("#stop").click(function()){
      $("div").stop();
  });

  $("#stop2").click(function()){
      $("div").stop(true);
  });

  $("#stop3").click(function()){
      $("div").stop(true, true);
  });
});

/*$(document).ready(function(){
  $("#test").click(function()){
    $("p").hide();
  });
});

/*$("#test").click(function()){
    $("div").animate({left:'250px'});
});


$(document).ready(function(){
  $("button").click(function()){
    $("#test").hide();
  });
});


$(document).ready(function(){
  $("button").click(function()){
    $(".test").hide();
  });
});*/
</script>