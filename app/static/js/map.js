$description = $(".description");

//selecting individual states
$("path").click(function() {
  var string = $(this).attr("id");
  var state = string
  var id = "#" + $(this).attr("id");
  var labelvar = document.getElementById("selected").value;
  if ($(id).hasClass("enabled")) {
    $(id).removeClass("enabled");
    if (labelvar.indexOf(state) != -1) {
      var index = labelvar.indexOf(state);
      if (index != 0) {
        var charArray = labelvar.split('');
        var test = charArray.splice(index - 1, 3, '', '', '');
        var newString = charArray.join('');
        document.getElementById("selected").value = newString
      } else {
        var charArray = labelvar.split('');
        var test = charArray.splice(index, 3, '', '', '');
        var newString = charArray.join('');
        document.getElementById("selected").value = newString
      }

    }
  } else {
    $(id).addClass("enabled");
    var labelvar = document.getElementById("selected");
    if (labelvar.value === '') {
      labelvar.value = string;
    } else {
      labelvar.value = labelvar.value + "," + string;
    }
  }
});
