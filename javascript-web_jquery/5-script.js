$(document).ready(function () {
  $("DIV#add_item").click(function () {
    $("<li>").text("Item").appendto("UL.my_list");
  });
});
