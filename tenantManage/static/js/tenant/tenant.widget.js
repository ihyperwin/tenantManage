;(function( $, window, document, undefined ) {

    $(document).ready(function() {
        /*change password*/
        if( $.fn.dialog  ) {
            $("#change-password-dialog").dialog({
                autoOpen: false,
                title: "修改密码",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#change-password-form').submit();
                    },
                },
            });     
        }
        
        $("#change-password").bind("click", function (event) {
            $("#change-password-dialog").dialog("open");
            event.preventDefault();
        });


        
        /*add tenant*/
        if( $.fn.dialog  ) {
            $("#add-tenant-dialog").dialog({
                autoOpen: false,
                title: "增加租客",
                modal: true,
                width: "400",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#add-tenant-form').submit();
                    },
                },
            });     
        }

        if( $.fn.button  ) {
            $("#sex").buttonset();
        }

        $("#addtenant").bind("click", function (event) {
            $("#add-tenant-dialog").dialog("open");
            event.preventDefault();
        });

        /*select tenant*/
        if( $.fn.dialog  ) {
            $("#select-tenant-dialog").dialog({
                autoOpen: false,
                title: "注意",
                modal: true,
                width: "400",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $("#select-tenant-dialog").dialog("close");
                    },
                },
            });
        }

        /*edit tenant*/
        if( $.fn.dialog  ) {
            $("#edit-tenant-dialog").dialog({
                autoOpen: false,
                title: "修改租客",
                modal: true,
                width: "400",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#edit-tenant-form').submit();
                    },
                },
            });
        }
        
        
        /*view tenant*/
        if( $.fn.dialog  ) {
            $("#tenant-detail-dialog").dialog({
                autoOpen: false,
                title: "租客详情",
                modal: true,
                width: "400",
                closeText:"hide",
            });
        }
        
        if( $.fn.button  ) {
            $("#viewsex").buttonset();
        }
        
        if( $.fn.datepicker ) {
            $(".mws-datepicker").datepicker({
                showOtherMonths: true,
                dateFormat: "yy-mm-dd",
                constrainInput: true,
                minDate:"-0d",
            });
        }

        if( $.fn.datepicker ) {
            $(".mws-datepicker").datepicker({
                showOtherMonths: true,
                dateFormat: "yy-mm-dd",
                constrainInput: true,
                minDate:"-0d",
            });
        }
        
        
        
        /*delete tenant*/
        if( $.fn.dialog  ) {
            $("#delete-tenant-dialog").dialog({
                autoOpen: false,
                title: "删除租客",
                modal: true,
                width: "350",
                closeText:"hide",
                buttons: {
                    "确定": function (event,ui) {
                        $('#delete-tenant-form').submit();
                    },
                    "取消":function (event,ui) {
                        $("#delete-tenant-dialog").dialog('close');
                    },
                },
            });
        }


    });

}) (jQuery, window, document);
