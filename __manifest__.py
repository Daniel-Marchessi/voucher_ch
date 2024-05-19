{
    'name': 'Vouchera',
    'version': '1.0.0',
    'summary': 'Vouchera ',
    'autor': 'Daniel Marchessi',
    'description': """
        Modulo destinado a la gestion de vouchers
    """,
    'category': 'Sales',
    'assets': {
        'web.assets_frontend': [
            'voucher_ch/static/src/css/style.css',
            'voucher_ch/static/src/js/components/main.js',
            'voucher_ch/static/src/js/components/cuponPortal.js',

        ],

    },

    'depends': ['web','website', 'base', 'contacts', 'account',],

    'data': [
        # 'security/groups.xml',
        'security/ir.model.access.csv',

        # views

        'views/pages/home.xml',
        'views/pages/form_benef.xml',
        'views/pages/form_negocio.xml',
        'views/cupon_view.xml',
        'views/voucher_views.xml',
        'views/footer.xml',
        'data/data_initial.xml',
        'views/portal_home_view.xml',
        'views/pages/cupon_web.xml',
        'wizards/wz_cupon_views.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
