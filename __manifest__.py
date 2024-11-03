{
    'name': 'POS Factura Fiscal RENACE',
    'version': '16.0.1.0.0',
    'summary': 'Facturación Fiscal en el POS de RENACE, con opciones B01 y B02.',
    'description': """
        Este módulo permite la generación de facturas fiscales en el punto de venta (POS) de RENACE,
        con opciones de NCF B01 (Factura Fiscal) y B02 (Factura Consumidor Final). El tipo de NCF
        y la secuencia de cada uno son configurables en el menú de ajustes del POS.
    """,
    'author': 'RENACE',
    'website': 'https://renace.tech',
    'category': 'Point of Sale',
    'depends': ['point_of_sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequences.xml',
        'views/pos_config_views.xml',
        'views/pos_order_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_factura_fiscal_renace/static/src/js/pos.js',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}