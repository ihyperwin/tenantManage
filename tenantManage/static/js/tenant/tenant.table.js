function getObjectClass(obj) {   
     if (obj && obj.constructor && obj.constructor.toString) {   
         var arr = obj.constructor.toString().match(   
             /function\s*(\w+)/);   
   
         if (arr && arr.length == 2) {   
             return arr[1];   
         }   
     }   
   
     return undefined;   
}

//for reload a datatable
$.fn.dataTableExt.oApi.fnReloadAjax = function ( oSettings, sNewSource, fnCallback, bStandingRedraw )
{
    if ( typeof sNewSource != 'undefined' && sNewSource != null ) {
        oSettings.sAjaxSource = sNewSource;
    }
 
    // Server-side processing should just call fnDraw
    if ( oSettings.oFeatures.bServerSide ) {
        this.fnDraw();
        return;
    }
 
    this.oApi._fnProcessingDisplay( oSettings, true );
    var that = this;
    var iStart = oSettings._iDisplayStart;
    var aData = [];
  
    this.oApi._fnServerParams( oSettings, aData );
      
    oSettings.fnServerData.call( oSettings.oInstance, oSettings.sAjaxSource, aData, function(json) {
        /* Clear the old information from the table */
        that.oApi._fnClearTable( oSettings );
          
        /* Got the data - add it to the table */
        var aData =  (oSettings.sAjaxDataProp !== "") ?
            that.oApi._fnGetObjectDataFn( oSettings.sAjaxDataProp )( json ) : json;
          
        for ( var i=0 ; i<aData.length ; i++ )
        {
            that.oApi._fnAddData( oSettings, aData[i] );
        }
          
        oSettings.aiDisplay = oSettings.aiDisplayMaster.slice();
          
        if ( typeof bStandingRedraw != 'undefined' && bStandingRedraw === true )
        {
            oSettings._iDisplayStart = iStart;
            that.fnDraw( false );
        }
        else
        {
            that.fnDraw();
        }
          
        that.oApi._fnProcessingDisplay( oSettings, false );
          
        /* Callback user function - for event handlers etc */
        if ( typeof fnCallback == 'function' && fnCallback != null )
        {
            fnCallback( oSettings );
        }
    }, oSettings );
};

;(function( $, window, document, undefined ) {

    $(document).ready(function() {

        // Data Tables
        if( $.fn.dataTable ) {
            
            //tenant
            var $tenant_selectrow = null;
            
            $("#tenants").dataTable({
                "iDisplayLength": 10,
                "aLengthMenu": [[10, 15, 20], [10, 15, 20]],
                sPaginationType: "full_numbers",
                "bAutoWidth": false,
                "sScrollX": "100%",
                "bDeferRender": true,//Deferred rendering
                "bProcessing": true,
                "bStateSave": false,
                "sScrollXInner": "100%",
                "sDom": 'T<"top"f>rt<"bottom"lpi><"clear">',
                "bServerSide": true,
                "sAjaxSource": "/ajax/get_tenants_list/",
                "fnServerData":function(sSource,aoData,fnCallback){
                	$.getJSON(sSource,aoData, function (json) { 
                        // Do whatever additional processing you want on the callback, then tell DataTables 
                        $tenant_selectrow = null;
                        fnCallback(json);
                    });  
                },
                "aoColumns": [
                    { "bSearchable": false},
                    { "bSearchable": true},
                    { "bSearchable": false},
                    { "bSearchable": true},
                    { "bSearchable": true},
                    { "bSearchable": false},
                    { "bSearchable": false},
                    { "bSearchable": false},
                ],
                "oTableTools":{
                    "sRowSelect": "single",             
                    "fnRowSelected":function(node){
                        $tenant_selectrow = $(node).children();
                    },
                    "aButtons":[],
                }
            });

            $('#tenants_filter').attr('style','height:25px;');
        
            $("<a href='#' class='btn' id='deletetenant'  style='float:right;width:66px;margin-right:2px;'><i class='icon-remove'></i>删除</a> \
            <a href='#' class='btn' id='edittenant'style='float:right;width:66px;margin-right:2px;'><i class='icon-edit'></i>修改</a>\
            <a href='#' class='btn' id='addtenant' style='float:right;width:66px;margin-right:2px;'><i class='icon-plus'></i>添加</a><a href='#' class='btn' id='viewtenant'style='float:right;width:66px;margin-right:2px;'><i class='icon-envelope'></i>查看详情</a>").appendTo('#tenants_filter');
          
            
            //delete one row tenant
            $("#deletetenant").bind("click", function (event) {
                event.preventDefault();
                if($tenant_selectrow == null){
                    $("#select-tenant-dialog").dialog("open");
                }else{
                    $('#delete_tenant_id').val($($tenant_selectrow[0]).text());
                    $("#delete-tenant-dialog").dialog("open");
                }
            });
            
            //edit one row tenant
            $("#edittenant").bind("click", function (event) {
            	event.preventDefault();
                if($tenant_selectrow == null){
                    $("#select-tenant-dialog").dialog("open");
                }else{
                	$('#id').val($($tenant_selectrow[0]).text());
                	$('#editName').val($($tenant_selectrow[1]).text());
                    $('#editMobileNumber').val($($tenant_selectrow[3]).text());
                    $('#editRemindDate').val($($tenant_selectrow[6]).text());
                    $('#editRentMoney').val($($tenant_selectrow[7]).text());
                    $("#edit-tenant-dialog").dialog("open");
                }
            });
            
            //view one row tenant
            $("#viewtenant").bind("click", function (event) {
            	event.preventDefault();
                if($tenant_selectrow == null){
                    $("#select-tenant-dialog").dialog("open");
                }else{
                	
                	url='/ajax/tenantprofile/';
                	data={id:$($tenant_selectrow[0]).text()}
                	 $.ajax({
                         type: "GET",
                         url: url,
                         data: data,
                         dataType: "json",
                         success: function(data){
                                  $('#viewname').val(data.name);
                                  $('#viewsex'+data.sex).attr("checked","checked");
                                  
                                  $('#labelsex0').removeClass("ui-state-active");
                                  $('#labelsex1').removeClass("ui-state-active");
                                  
                                  $('#labelsex'+data.sex).addClass("ui-state-active");
                                  $('#viewMobileNumber').val(data.mobileNumber);
                                  $('#viewCommunity').val(data.community);
                                  $('#viewUnit').val(data.unit);
                                  $('#viewHouseNumber').val(data.houseNumber);
                                  $('#viewRentMoney').val(data.rentMoney);
                                  $('#viewRentDate').val(data.rentDate);
                                  $('#viewRemindDate').val(data.remindDate);
                                  
                   		          $("#tenant-detail-dialog").dialog("open");
                        }
                     });
                	
                	
                }
            });
     
        }
    });        

}) (jQuery, window, document);
