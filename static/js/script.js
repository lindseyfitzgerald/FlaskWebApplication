"use strict";
$(document).ready( () => {
    $("#add").submit( evt => {
        let isValid = true;
        const image = $("#image").val().trim();
        if (image == ""){
            $("#image").next().text("Must add image.");
            isValid = false;
        }
        else{
            $("#image").next().text("");
        }
        $("#image").val(image);

        //name validation
        const name = $("#name").val().trim();
        if (name == ""){
            $("#name").next().text("This field is required.");
            isValid = false;
        }
        else{
            $("#name").next().text("");
        }
        $("#name").val(name);

        //console validation
        const console = $("#console").val().trim();
        if (console == ""){
            $("#console").next().text("This field is required.");
            isValid = false;
        }
        else{
            $("#console").next().text("");
        }
        $("#console").val(console);

        //year validation
        const year = $("#year").val().trim();
        if (year == ""){
            $("#year").next().text("This field is required.");
            isValid = false;
        }
        else{
            $("#year").next().text("");
        }
        $("#year").val(year);

        //description validation
        const description = $("#description").val().trim();
        if (description == ""){
            $("#description").next().text("This field is required.");
            isValid = false;
        }
        else{
            $("#description").next().text("");
        }
        $("#description").val(description);

        if (!isValid){
            evt.preventDefault();
        }
    });
});