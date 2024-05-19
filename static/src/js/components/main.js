
/* @odoo-module */
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { jsonrpc } from "@web/core/network/rpc_service";
import publicWidget from "@web/legacy/js/public/public_widget";
console.log('-test')
publicWidget.registry.MainComponent = publicWidget.Widget.extend({
    selector: '.btn-add',
    setup(){
         this.popup = useService("popup");
        this.notification = useService("notification");

    },

     start: function () {
        this._super.apply(this, arguments);
        console.log("My custom action started!");
        this.$el.on('click', this.onClick.bind(this));  // Manejar el evento click directamente

    },

      onClick: function (ev) {
       if (odoo.session_info){
       console.log('Es usuario----------------')

       }
        var popUp = $('#popup')
        var cupon_id = this.$el.data('oe-id');
        var $clickedButton = $(ev.target);

        var cantidad_cupon = this.$el.data('oe-cantidad');
        var data = { cupon_id: cupon_id };
//        var $qtyCupon = $('#qtyCupon' + cupon_id); // Seleccionar el elemento <p> específico por ID
        var $qtyCupon = $clickedButton.closest('.ticket-box').find('#qtyCupon' );
        var $user = $('#currentUser')
        var cantidad_reduc = $qtyCupon.text().trim();
        var qty = parseInt(cantidad_reduc)
        var res = qty - 1

        var user_id = $user.text().trim()

           jsonrpc('/click_coupon', {
        params: {
            cupon_id: cupon_id
        }
        }).then(function(response) {
            if (response === true) {
                // El cupón está asociado al socio, abrir un popup de alerta
                alert('¡Este cupón ya está asociado a tu cuenta!');
            }
        }).catch(function(error) {
            console.error('Error al llamar al controlador:', error);
        // Mostrar un popup de error genérico
            alert('Ocurrió un error al procesar la solicitud');
        });


       jsonrpc('/discount_qty', {
         // Pasa el cupon_id en los datos de la solicitud
        params: {
            cupon_id: cupon_id,
            user_id : user_id
        }
        }).then(function(response) {
            console.log('----Ok-------');
        }).catch(function(error) {
            console.error('Error al llamar al controlador:', error);
        });

        popUp.modal('show');

        $qtyCupon.text(res)
        var closeButton = $('#close_popUp');
        closeButton.on('click', function() {
            $('#popup').modal('hide');

             if (res == 0){

                var $ticketBox = $clickedButton.closest('.ticket-box');
                 $ticketBox.delay(500).fadeOut();
              }

                 location.reload();
        });


        console.log('Cupón ID:', cupon_id);
    },
});

