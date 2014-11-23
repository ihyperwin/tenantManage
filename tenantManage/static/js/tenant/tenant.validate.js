;(function( $, window, document, undefined ) {

    $(document).ready(function() {

        if( $.validator ) {
            jQuery.validator.addMethod("username", function( value, element ) {
                var result = this.optional(element) || /^([\w]{9}|[a-zA-Z]{1}[\w]+?)$/.test(value);

                return result;
            }, "Your username is invalid.");

            jQuery.validator.addMethod("password", function( value, element ) {
                var result = this.optional(element) || /^[\w]+?$/.test(value);

                return result;
            }, "Your password is invalid.");
            
            jQuery.validator.addMethod("tenantName", function( value, element ) {
                var result = this.optional(element) || /^[\u4e00-\u9fa5]{2,6}$/.test(value);

                return result;
            }, "tenant's name is invalid.");

            /*login*/
            $('#login-form').validate({
                errorPlacement:function(label,elem){
                    elem.closest('.mws-form-row').find('.error-messages').append(label);
                },
                rules:{
                    username:{
                        required:true,
                        minlength:3,
                        maxlength:12,
                        username:true,
                    },
                    password:{
                        required:true,
                        minlength:6,
                        maxlength:12,
                        password:true,
                    },
                },
                messages:{
                    username:{
                        required:"用户名必须要填",
                        minlength:"用户名至少为3位",
                        maxlength:"用户名至多为12位",
                        username:'3-12位,由字母数字下划线组成,首字母为字母',
                    },
                    password:{
                        required:"密码必须要填(由字母数字下划线组成的字符串，最少为6位)", 
                        minlength:"密码至少为6位",
                        maxlength:"密码至多为12位",
                        password:"密码由字母数字下划线组成的字符串，最少为6位",
                    },
                },
                invalidHandler: function(form, validator) {
                    if($.fn.effect) {
                        $("#mws-login").effect("shake", {distance: 6, times: 2}, 35);
                    }
                }
            });

            /*changepassword*/
            $('#change-password-form').validate({
                errorPlacement:function(label,elem){
                    elem.closest('.mws-form-row').find('.error-messages').append(label);
                },
                rules:{
                    newpassword:{
                        required:true,
                        minlength:6,
                        maxlength:12,
                        password:true,
                    },
                    renewpassword:{
                        required:true,
                        equalTo:'#newpassword',
                    },
                },
                messages:{
                    newpassword:{
                        required:"密码必须要填(由字母数字下划线组成的字符串，最少为6位)", 
                        minlength:"密码至少为6位",
                        maxlength:"密码至多为12位",
                        password:"密码由字母数字下划线组成的字符串，最少为6位",
                    },
                    renewpassword:{
                        required:'重复密码必须要填',  
                        equalTo:'此处必须输入和上栏密码相同的内容',
                    },
                },
                invalidHandler: function(form, validator) {
                    ;
                }
            });
            
            
            
            /*add tenant*/
            $('#add-tenant-form').validate({
                errorPlacement:function(label,elem){
                    elem.closest('.mws-form-row').find('.error-messages').append(label);
                },
                rules:{
                	name:{
                        required:true,
                    },
                    sex:{
                        required:true,
                    },
                    mobileNumber:{
                        required:true,
                        minlength:11,
                        maxlength:11,
                    },
                    community:{
                        required:true,
                        minlength:1,
                        maxlength:512,
                    },
                    unit:{
                        required:true,
                        minlength:1,
                        maxlength:512,
                    },
                    houseNumber:{
                        required:true,
                        minlength:1,
                        maxlength:11,
                    },
                    rentMoney:{
                        required:true,
                    },
                    remindDate:{
                        required:true,
                    },
                    rentDate:{
                        required:true,
                    },
                },
                messages:{
                	name:{
                        required:'租客姓名必须要填（2-4个汉字）',  
                    },
                    sex:{
                        required:"请选择性别",
                    },
                    mobileNumber:{
                        required:"手机号必须要填(11为数字)", 
                        minlength:"手机号应为11位",
                        maxlength:"手机号应为11位",
                    },
                    community:{
                        required:"小区名必须要填", 
                        minlength:"小区名至少为1位",
                        maxlength:"小区名至多为512位",
                    },
                    unit:{
                        required:"单元号必须要填", 
                        minlength:"单元号至少为1位",
                        maxlength:"单元号至多为512位",
                    },
                    houseNumber:{
                        required:"房间号必须要填", 
                        minlength:"手机号至少为1位",
                        maxlength:"手机号至多为11位",
                    },
                    rentMoney:{
                        required:"租金必须要填", 
                        minlength:"租金至少为1位",
                        maxlength:"租金号至多为4位",
                    },
                    remindDate:{
                        required:"提醒日期必须要填", 
                    },
                    rentDate:{
                        required:"入住日期必须要填", 
                    },
                },
                invalidHandler: function(form, validator) {
                  
                }
            });

            
            
            
            
        }
    });
}) (jQuery, window, document);

