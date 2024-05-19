from odoo import http
from odoo.http import request

import base64
import logging

_log = logging.getLogger(__name__)


class WebController(http.Controller):
    @http.route('/', auth='public', type='http', website=True, sitemap=True)
    def get_home(self):
        logging.info('---Cupones ')
        cupones = request.env['dm.cupon'].sudo().search([('cantidad', '>', 0)], order='create_date desc', limit= 8)
        is_authenticated = request.session.uid  # Verificar si el usuario está autenticado
        categorias = request.env['dm.categoria'].sudo().search([])

        logging.info(cupones)
        logging.info(cupones)



        logging.info('---Pueba cupones')
        logging.info(cupones[:4])
        values = {
            'list_cupons': cupones,
            'is_authenticated': bool(is_authenticated),
            'list_categorias': categorias,
            'list_cupons_limited': cupones[:4],
        }
        return request.render('voucher_ch.home_view', values)




    @http.route('/discount_qty', auth='public', type='json')
    def discount_qty(self, **kwargs):
        logging.info('.-----------Cupon id------------')
        logging.info(kwargs)
        cupon_id = kwargs.get('params', {}).get('cupon_id')
        user_id = kwargs.get('params', {}).get('user_id')

        cupon = request.env['dm.cupon'].sudo().browse(int(cupon_id))

        usuario = request.env['res.users'].sudo().browse(int(user_id))
        partner_id = usuario.partner_id
        logging.info(f'---------Partner {partner_id} {partner_id.cupones_ids}')

        partner_id.sudo().write({'cupones_ids': [(4, cupon_id)]})

        for voucher in cupon.vaucher_ids:
            if voucher.estado == 'activo':
                voucher.sudo().write({'user_id': int(user_id)})
                voucher.sudo().write({'estado': 'asignado'})
                break
        logging.info(cupon)


    @http.route('/my_cupons', auth='user', type='http', website=True, sitemap=True, )
    def get_cupons(self):


        user_id = request.env.user.id

        logging.info('--------test')
        cupones = request.env['dm.cupon.vaucher'].sudo().search([('user_id', '=', user_id)])
        logging.info('----Cupones desde mycupons  ---')
        logging.info(cupones)


        values = {
            'list_cupons': cupones,

        }

        return request.render('voucher_ch.my_cupon',values)

    @http.route('/beneficiario-post', type='http', auth='user', website=True, csrf=False, methods=['POST'])
    def send_benefic(self, **post):

        logging.info('-...............')
        logging.info(post)

        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'apellido': post.get('address'),
            'vat': post.get('documento'),
            'street': post.get('direccion'),
            'provincia': post.get('provincia'),
            'phone': post.get('telefono'),
        })
        logging.info('-----Creo un partner')

        logging.info(partner)
        return request.redirect('/')

    @http.route('/empresa-post', type='http', auth='user', website=True, csrf=False, methods=['POST'])
    def send_empresa(self, **post):

        logging.info('-...............')
        logging.info(post)

        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'apellido': post.get('address'),
            'vat': post.get('documento'),
            'street': post.get('direccion'),
            'provincia': post.get('provincia'),
            'phone': post.get('telefono'),
            'email': post.get('telefono'),
        })
        logging.info('-----Creo un partner')

        logging.info(partner)
        return request.redirect('/')

    @http.route('/click_coupon', auth='public', type='json', website=True)
    def click_coupon(self, **kwargs):
        cupon_id = kwargs.get('params', {}).get('cupon_id')

        logging.info('----Clicl cupon')
        logging.info(kwargs)
        if request.session.uid:
            logging.info('---------------')
            user_id = request.session.uid
            usuario = request.env['res.users'].sudo().browse(user_id)

            partner_id = usuario.partner_id
            logging.info(partner_id)
            cupon = request.env['dm.cupon'].sudo().browse(int(cupon_id))
            logging.info(cupon)

            for rec in partner_id.cupones_ids:
                logging.info(rec)
                if rec == cupon:
                    logging.info('---REc cupon')
                    return True

                else:
                    return False
        else:
            return False