
/* @odoo-module */
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { jsonrpc } from "@web/core/network/rpc_service";
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.PortalCOmponent = publicWidget.Widget.extend({
    selector: '.button-portal',
    setup(){
         this.popup = useService("popup");
        this.notification = useService("notification");

    },

     start: function () {
        this._super.apply(this, arguments);
        console.log("My custom action started!");
        this.$el.on('click', this.printTicket.bind(this));  // Manejar el evento click directamente


    },



     printTicket: function (ev) {

             var $clickedButton = $(ev.target);
            var padre = $clickedButton.closest('.ticket-box')
            var divContent = padre.html();
        window.print()
//   var printWindow = window.open('',);
//    printWindow.document.write('<html><head><title>Print</title></head><body>');
//printWindow.document.write("<div style='background-image: url(\"/voucher_ch/static/src/img/Ticket.png\"); margin-top: 20px; min-width:250px; max-width: 300px; padding: 10px 30px 10px 30px; min-height:150px; margin-right: 30px;'>");
//
//
//    printWindow.document.write(divContent);
//        printWindow.document.write('</>"');
//
//    printWindow.document.write('</body></html>');
//    printWindow.document.close();
//    printWindow.print();
    },



});

